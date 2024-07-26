from textnode import (
    TextNode,
    text_node_to_html_node,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)

from htmlnode import(
    HTMLNode,
    LeafNode,
    ParentNode
)

from split_nodes import(
    split_node_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_node_image,
    split_node_link,
    text_to_textnodes,
)

from block_split import(
    markdown_to_blocks,
    block_to_block_type,
)

def text_to_children(text):
    textnodes = text_to_textnodes(text)
    childrennodes = []
    for textnode in textnodes:
        childrennodes.append(text_node_to_html_node(textnode))
    return childrennodes

def block_to_leaf(block):
    nodelist = []
    lines = block.split("\n")
    for line in lines:
        nodelist.append(ParentNode("li", text_to_children(line)))
    return nodelist

def strip_block_header(block, *args):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        new_line = line
        for arg in args:
            if type(arg) == list:
                for item in arg:
                    if new_line[:len(item)] == item:
                        new_line = new_line[len(item):]
            elif new_line[:len(arg)] == arg:
                new_line = new_line[len(arg):]
        new_lines.append(new_line) 
    new_block = "\n".join(new_lines)
    return new_block
    

def markdown_to_html(markdown):
    blocks = markdown_to_blocks(markdown)
    parent_block_list = []
    for block in blocks:
        type = block_to_block_type(block)
        if type == 'code':
            parent_block_list.append(ParentNode("pre", [ParentNode("code", text_to_children(block))]))

        if type == "paragraph":
            parent_block_list.append(ParentNode("p", text_to_children(block)))

        if type == "quote":
            parent_block_list.append(ParentNode("blockquote", text_to_children(strip_block_header(block, "> "))))

        if type == "unordered_list":
            parent_block_list.append(ParentNode("ul", block_to_leaf(strip_block_header(block, "* ", "- "))))

        if type == "ordered_list":
            lines = block.split("\n")
            del_list = []
            for i in range(len(lines)):
                del_list.append(f"{i + 1}. ")

            parent_block_list.append(ParentNode("ol", block_to_leaf(strip_block_header(block, del_list))))

        if type == "heading1":
            block = block[2:]
            parent_block_list.append(ParentNode("h1", text_to_children(strip_block_header(block,))))
        if type == "heading2":
            block = block[3:]
            parent_block_list.append(ParentNode("h2", text_to_children(block)))
        if type == "heading3":
            block = block[4:]
            parent_block_list.append(ParentNode("h3", text_to_children(block)))
        if type == "heading4":
            block = block[5:]
            parent_block_list.append(ParentNode("h4", text_to_children(block)))
        if type == "heading5":
            block = block[6:]
            parent_block_list.append(ParentNode("h5", text_to_children(block)))
        if type == "heading6":
            block = block[7:]
            parent_block_list.append(ParentNode("h6", text_to_children(block)))
    
    return ParentNode("div", parent_block_list)