import os
import shutil

def map_files(dir, new_dir, i = 1):
    if i == 1:
        shutil.rmtree(new_dir)
        os.mkdir(new_dir)
    dir_content = os.listdir(dir)
    for item in dir_content:
        if os.path.isfile(os.path.join(dir, item)) == True:
            shutil.copy(f"{dir}/{item}", f"{new_dir}/{item}")
        if os.path.isfile(os.path.join(dir, item)) == False:
            os.mkdir(os.path.join(new_dir, item))
            map_files(os.path.join(dir, item), os.path.join(new_dir, item), i + 1)
    return

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line[:2] == "# ":
            new_line = line[2:]
            return new_line.strip(" ")
    raise ValueError("Header in place")
