from htmlnode import HTMLNode

from copy_file import (
    map_files,
    generate_page
)

def main():
    map_files("static", "public")
    generate_page("content/index.md", "template.html", "public")

main()