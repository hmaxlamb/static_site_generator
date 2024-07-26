from htmlnode import HTMLNode

from copy_file import (
    map_files,
    generate_page,
    generate_pages_recursive
)

def main():
    map_files("static", "public")
    generate_pages_recursive("content", "template.html", "public")

main()