import os
import shutil

from mark_to_html import markdown_to_html

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

def generate_page(from_path, template_path, dest_path):
    file1 = open(from_path)
    mdpage = file1.read()
    file1.close()
    file2 = open(template_path)
    temp = file2.read()
    file2.close()
    htlm_content = markdown_to_html(mdpage)
    title = extract_title(mdpage)
    complete_html = temp.replace("{{ Title }}", title).replace("{{ Content }}", htlm_content.to_html())
    new_file_path = os.path.join(dest_path, os.path.basename(from_path)).replace(".md", ".html")
    new_file = open(new_file_path, "w")
    new_file.write(complete_html)

def generate_pages_recursive(from_path, template_path, dest_path):
    dir_conent = os.listdir(from_path)
    for item in dir_conent:
        if os.path.isfile(os.path.join(from_path, item)) == True:
            generate_page(os.path.join(from_path, item), template_path, dest_path)
        if os.path.isfile(os.path.join(from_path, item)) == False:
            os.mkdir(os.path.join(dest_path, item))
            generate_pages_recursive(os.path.join(from_path, item), template_path, os.path.join(dest_path, item))
    return