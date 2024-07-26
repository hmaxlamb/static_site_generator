import os
import shutil

def map_files(dir, new_dir, i = 1):
    if i == 1:
        shutil.rmtree(f"{new_dir}/*")
    dir_content = os.listdir(dir)
    for item in dir_content:
        if os.path.isfile(item):
            shutil.copy(f"{dir}", f"{new_dir}")
            print(f"{dir}/{item}")
        if os.path.isfile(item) == False:
            shutil.copy(f"{dir}", f"{new_dir}")
            map_files(f"{dir}/{item}", f"{new_dir}/{item}")
    return