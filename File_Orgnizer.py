#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File Organizer - أداة لتنظيم الملفات في مجلدات

هذه الأداة تساعد في تنظيم الملفات في مجلدات حسب نوعها أو امتدادها
"""

import os
import sys
import shutil
import argparse
import logging
import time
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

__author__ = "Your Name"
__version__ = "2.0.0"

# تكوين نظام التسجيل
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("file_organizer.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("FileOrganizer")

# تعريف أنواع الملفات
FILE_TYPES = {
    "Documents": ["doc", "docx", "xls", "xlsx", "pdf", "xps", "potx", "pptx", "txt", "rtf", "odt", "csv"],
    "Photos": ["jpg", "jpeg", "gif", "bmp", "png", "tiff", "svg", "webp", "raw", "heic"],
    "Videos": ["avi", "mp4", "mpeg", "wmv", "flv", "mkv", "mov", "webm", "m4v", "3gp"],
    "Audio": ["mp3", "wma", "amp", "wav", "flac", "aac", "ogg", "m4a"],
    "Programs": ["exe", "dmg", "bat", "sh", "msi", "app", "apk", "deb", "rpm"],
    "Archives": ["zip", "rar", "7zip", "7z", "tar", "gz", "bz2", "xz", "iso"],
    "Code": ["py", "js", "html", "css", "java", "c", "cpp", "php", "rb", "go", "ts", "json", "xml"],
    "Fonts": ["ttf", "otf", "woff", "woff2", "eot"],
    "Designs": ["psd", "ai", "xd", "sketch", "fig", "indd", "cdr"]
}


def get_file_type(extension):
    """تحديد نوع الملف بناءً على الامتداد"""
    for file_type, extensions in FILE_TYPES.items():
        if extension.lower() in extensions:
            return file_type
    return "Others"


def process_file(file, source_dir, target_base_dir, organize_method, copy_mode=False):
    """معالجة ملف واحد (نقل أو نسخ)"""
    try:
        # تجاهل الملفات الخاصة
        if file.startswith('.') or file == os.path.basename(sys.argv[0]) or file == "file_organizer.log":
            return None

        source_path = os.path.join(source_dir, file)
        
        # التحقق من أن المسار هو ملف وليس مجلد
        if not os.path.isfile(source_path):
            return None

        # تحديد المجلد الهدف
        if organize_method == "type":
            # التنظيم حسب النوع
            if "." in file:
                file_ext = file.split(".")[-1].lower()
                target_dir = get_file_type(file_ext)
            else:
                target_dir = "No Extension"
        else:
            # التنظيم حسب الامتداد
            if "." in file:
                target_dir = file.split(".")[-1].lower()
            else:
                target_dir = "no_extension"

        # إنشاء المسار الكامل للمجلد الهدف
        target_dir_path = os.path.join(target_base_dir, target_dir)
        
        # إنشاء المجلد إذا لم يكن موجودًا
        if not os.path.exists(target_dir_path):
            os.makedirs(target_dir_path)

        # المسار الكامل للملف الهدف
        target_file_path = os.path.join(target_dir_path, file)
        
        # التعامل مع الملفات المكررة
        if os.path.exists(target_file_path):
            file_name, file_ext = os.path.splitext(file)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            new_file_name = f"{file_name}_{timestamp}{file_ext}"
            target_file_path = os.path.join(target_dir_path, new_file_name)
        
        # نقل أو نسخ الملف
        if copy_mode:
            shutil.copy2(source_path, target_file_path)
            action = "نسخ"
        else:
            shutil.move(source_path, target_file_path)
            action = "نقل"
            
        file_size = os.path.getsize(target_file_path)
        logger.debug(f"تم {action} الملف: {file} ({file_size} بايت) إلى {target_dir}")
        
        return {
            "file": file,
            "size": file_size,
            "target_dir": target_dir
        }
    except Exception as e:
        logger.error(f"خطأ أثناء معالجة الملف {file}: {e}")
        return None


def organize_files(source_dir, target_dir, organize_method, copy_mode=False, max_workers=4):
    """تنظيم الملفات في المجلد المصدر"""
    logger.info(f"بدء تنظيم الملفات في: {source_dir}")
    
    # الحصول على قائمة الملفات
    try:
        files = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f))]
    except Exception as e:
        logger.error(f"خطأ في قراءة المجلد: {e}")
        return
    
    if not files:
        logger.info("لا توجد ملفات للتنظيم")
        return
    
    logger.info(f"تم العثور على {len(files)} ملف")
    
    # إنشاء مجلد الهدف إذا لم يكن موجودًا
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    # إحصائيات
    stats = {
        "total_files": len(files),
        "processed_files": 0,
        "total_size": 0,
        "by_type": {}
    }
    
    # استخدام ThreadPoolExecutor للمعالجة المتوازية
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # إنشاء قائمة المهام
        futures = [executor.submit(
            process_file, file, source_dir, target_dir, organize_method, copy_mode
        ) for file in files]
        
        # عرض شريط التقدم
        with tqdm(total=len(files), desc="تنظيم الملفات", unit="ملف") as pbar:
            for future in futures:
                result = future.result()
                if result:
                    stats["processed_files"] += 1
                    stats["total_size"] += result["size"]
                    
                    # تحديث إحصائيات حسب النوع
                    target_type = result["target_dir"]
                    if target_type not in stats["by_type"]:
                        stats["by_type"][target_type] = {"count": 0, "size": 0}
                    
                    stats["by_type"][target_type]["count"] += 1
                    stats["by_type"][target_type]["size"] += result["size"]
                
                pbar.update(1)
    
    # عرض الإحصائيات
    logger.info(f"اكتمل التنظيم: تمت معالجة {stats['processed_files']} من {stats['total_files']} ملف")
    logger.info(f"الحجم الإجمالي: {format_size(stats['total_size'])}")
    
    # عرض الإحصائيات حسب النوع
    logger.info("الإحصائيات حسب النوع:")
    for file_type, type_stats in stats["by_type"].items():
        logger.info(f"  {file_type}: {type_stats['count']} ملف ({format_size(type_stats['size'])})")


def format_size(size_bytes):
    """تنسيق حجم الملف بشكل قابل للقراءة"""
    if size_bytes < 1024:
        return f"{size_bytes} بايت"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.2f} كيلوبايت"
    elif size_bytes < 1024 * 1024 * 1024:
        return f"{size_bytes / (1024 * 1024):.2f} ميجابايت"
    else:
        return f"{size_bytes / (1024 * 1024 * 1024):.2f} جيجابايت"


def main():
    """الدالة الرئيسية"""
    # إنشاء محلل وسائط سطر الأوامر
    parser = argparse.ArgumentParser(description="أداة لتنظيم الملفات في مجلدات")
    
    parser.add_argument("method", choices=["t", "e"], help="طريقة التنظيم: t للتنظيم حسب النوع، e للتنظيم حسب الامتداد")
    parser.add_argument("-s", "--source", default=".", help="مجلد المصدر (الافتراضي: المجلد الحالي)")
    parser.add_argument("-d", "--destination", help="مجلد الوجهة (الافتراضي: نفس مجلد المصدر)")
    parser.add_argument("-c", "--copy", action="store_true", help="نسخ الملفات بدلاً من نقلها")
    parser.add_argument("-v", "--verbose", action="store_true", help="عرض معلومات تفصيلية")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    
    # تحليل الوسائط
    args = parser.parse_args()
    
    # ضبط مستوى التسجيل
    if args.verbose:
        logger.setLevel(logging.DEBUG)
    
    # تحديد مجلد الوجهة
    target_dir = args.destination if args.destination else args.source
    
    # تحديد طريقة التنظيم
    organize_method = "type" if args.method == "t" else "extension"
    
    # بدء عملية التنظيم
    start_time = time.time()
    organize_files(args.source, target_dir, organize_method, args.copy)
    end_time = time.time()
    
    logger.info(f"استغرقت العملية {end_time - start_time:.2f} ثانية")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.warning("تم إيقاف البرنامج بواسطة المستخدم")
        sys.exit(1)
    except Exception as e:
        logger.error(f"حدث خطأ غير متوقع: {e}")
        sys.exit(1)