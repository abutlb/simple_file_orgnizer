###################
# made by @abutlb #
###################
import sys
import glob
import os


org_method = sys.argv[1].lower()

doc_type = ["doc","docx","xls","xlsx","pdf","xps","potx","pptx"]
photo_type = ["jpg","jpeg","gif","bmp","png"]
video_type = ["avi","mp4","mpeg","wmv","flv","mkv"]
audio_type = ["mp3","wma","amp"]
program_type = ["exe","dmg","bat"]
archive_type = ["zip","rar","7zip","7z"]

def orgnize_by_type():
    print("orgbytype")
    filenames = glob.glob("*")
    filenames.pop(0)
    i = 1
    for file in filenames:
        file_name,file_exe = file.split(".")
        print(f"moving {i} of {len(filenames)}---{file}")
        if file_exe in doc_type:
            if not os.path.exists("Documents"):
                os.makedirs("Documents")
            os.rename(file,f"Documents\\{file}")
        elif file_exe in photo_type:
            if not os.path.exists("Photos"):
                os.makedirs("Photos")
            os.rename(file,f"Photos\\{file}")
        elif file_exe in video_type:
            if not os.path.exists("Videos"):
                os.makedirs("Videos")
            os.rename(file,f"Videos\\{file}")
        elif file_exe in audio_type:
            if not os.path.exists("Audios"):
                os.makedirs("Audios")
            os.rename(file,f"audios\\{file}")
        elif file_exe in program_type:
            if not os.path.exists("Programs"):
                os.makedirs("Programs")
            os.rename(file,f"Programs\\{file}")
        elif file_exe in archive_type:
            if not os.path.exists("Archives"):
                os.makedirs("Archives")
            os.rename(file,f"Archives\\{file}")
        else:
            if not os.path.exists("Others"):
                os.makedirs("Others")
            os.rename(file,f"Others\\{file}")
        i += 1
        


def orgnize_by_extension():
    print("org by extinsion")
    filenames = glob.glob("*")
    filenames.pop(0)
    i = 1
    for file in filenames:
        file_name,file_exe = file.split(".")
        print(f"moving {i} of {len(filenames)}---{file}")
        if not os.path.exists(file_exe):
            os.makedirs(file_exe)
        os.rename(file,f"{file_exe}\\{file}")



if org_method == "t":
    orgnize_by_type()
elif org_method == "e":
    orgnize_by_extension()