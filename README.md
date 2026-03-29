# File Organizer - أداة تنظيم الملفات

أداة احترافية لتنظيم الملفات في مجلدات فرعية حسب النوع أو الامتداد.

<p align="center">
  <img src="https://img.shields.io/badge/version-2.0.0-blue.svg" alt="Version">
  <img src="https://img.shields.io/badge/python-3.6+-green.svg" alt="Python">
  <img src="https://img.shields.io/badge/license-MIT-orange.svg" alt="License">
</p>

## 🌟 المميزات

- ✅ تنظيم الملفات حسب النوع (مستندات، صور، فيديو، إلخ)
- ✅ تنظيم الملفات حسب امتداد الملف
- ✅ إمكانية تحديد مجلد المصدر والوجهة
- ✅ خيار لنسخ الملفات بدلاً من نقلها
- ✅ معالجة متوازية لتحسين الأداء
- ✅ التعامل الذكي مع الملفات المكررة
- ✅ تقارير وإحصائيات مفصلة
- ✅ تسجيل العمليات في ملف سجل

## 📋 المتطلبات

- Python 3.6 أو أحدث
- مكتبة tqdm (للتثبيت: `pip install tqdm`)

## 🚀 التثبيت

### التثبيت المباشر

1. قم بتنزيل الملف `File_Organizer.py`
2. تأكد من تثبيت المتطلبات:

```bash
pip install -r requirements.txt
```

### التثبيت من Git

```bash
git clone https://github.com/username/file-organizer.git
cd file-organizer
pip install -r requirements.txt
```

## 📝 الاستخدام

### الاستخدام الأساسي

```bash
python File_Organizer.py [t|e]
```

حيث:
- `t` - تنظيم الملفات حسب النوع
- `e` - تنظيم الملفات حسب الامتداد

### الخيارات المتقدمة

```bash
python File_Organizer.py [-h] [-s SOURCE] [-d DESTINATION] [-c] [-v] {t,e}
```

#### الوسائط الإلزامية:
- `{t,e}` - طريقة التنظيم (t: حسب النوع، e: حسب الامتداد)

#### الخيارات الاختيارية:
- `-h, --help` - عرض رسالة المساعدة
- `-s SOURCE, --source SOURCE` - تحديد مجلد المصدر (الافتراضي: المجلد الحالي)
- `-d DESTINATION, --destination DESTINATION` - تحديد مجلد الوجهة (الافتراضي: نفس مجلد المصدر)
- `-c, --copy` - نسخ الملفات بدلاً من نقلها
- `-v, --verbose` - عرض معلومات تفصيلية
- `--version` - عرض إصدار البرنامج

## 💡 أمثلة

### تنظيم الملفات في المجلد الحالي حسب النوع
```bash
python File_Organizer.py t
```

### تنظيم الملفات في مجلد محدد حسب الامتداد
```bash
python File_Organizer.py e -s /path/to/source
```

### نسخ الملفات (بدلاً من نقلها) إلى مجلد وجهة محدد
```bash
python File_Organizer.py t -s /path/to/source -d /path/to/destination -c
```

### عرض معلومات تفصيلية أثناء التنظيم
```bash
python File_Organizer.py t -v
```

## 📂 أنواع الملفات المدعومة

| النوع | الامتدادات المدعومة |
|-------|---------------------|
| **المستندات** | doc, docx, xls, xlsx, pdf, xps, potx, pptx, txt, rtf, odt, csv |
| **الصور** | jpg, jpeg, gif, bmp, png, tiff, svg, webp, raw, heic |
| **الفيديو** | avi, mp4, mpeg, wmv, flv, mkv, mov, webm, m4v, 3gp |
| **الصوت** | mp3, wma, amp, wav, flac, aac, ogg, m4a |
| **البرامج** | exe, dmg, bat, sh, msi, app, apk, deb, rpm |
| **الأرشيف** | zip, rar, 7zip, 7z, tar, gz, bz2, xz, iso |
| **الكود** | py, js, html, css, java, c, cpp, php, rb, go, ts, json, xml |
| **الخطوط** | ttf, otf, woff, woff2, eot |
| **التصاميم** | psd, ai, xd, sketch, fig, indd, cdr |

## 📊 مخرجات البرنامج

عند تشغيل البرنامج، سيقوم بعرض:

1. **شريط تقدم** يوضح عملية نقل/نسخ الملفات
2. **ملخص للعملية** يتضمن:
   - عدد الملفات التي تمت معالجتها
   - الحجم الإجمالي للملفات
   - توزيع الملفات حسب النوع
   - الوقت المستغرق للعملية

كما يتم تسجيل كافة العمليات في ملف `file_organizer.log` للرجوع إليه لاحقاً.

## 🛠️ تخصيص البرنامج

يمكنك تخصيص أنواع الملفات المدعومة عن طريق تعديل القاموس `FILE_TYPES` في بداية الكود:

```python
FILE_TYPES = {
    "Documents": ["doc", "docx", ...],
    "Photos": ["jpg", "jpeg", ...],
    # أضف أو عدل الأنواع حسب احتياجاتك
}
```

## 🔄 تحديثات مستقبلية

- [ ] واجهة رسومية للمستخدم (GUI)
- [ ] دعم لتنظيم المجلدات الفرعية
- [ ] خيارات إضافية للتعامل مع الملفات المكررة
- [ ] إمكانية تصفية الملفات قبل التنظيم
- [ ] دعم لتنظيم الملفات حسب تاريخ الإنشاء/التعديل

## 🤝 المساهمة

المساهمات مرحب بها! إذا كنت ترغب في المساهمة:

1. قم بعمل Fork للمشروع
2. أنشئ فرع جديد للميزة (`git checkout -b feature/amazing-feature`)
3. قم بعمل Commit للتغييرات (`git commit -m 'Add some amazing feature'`)
4. ادفع إلى الفرع (`git push origin feature/amazing-feature`)
5. افتح طلب Pull Request

## 📄 الترخيص

هذا المشروع مرخص بموجب رخصة MIT - راجع ملف `LICENSE` للحصول على التفاصيل.

## 📞 الاتصال

إذا كان لديك أي أسئلة أو اقتراحات، لا تتردد في التواصل:

- البريد الإلكتروني: your.email@example.com
- تويتر: [@YourTwitterHandle](https://twitter.com/YourTwitterHandle)
- GitHub: [YourGitHubUsername](https://github.com/YourGitHubUsername)