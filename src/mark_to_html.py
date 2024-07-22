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


def markdown_to_html(markdown):
    blocks = markdown_to_blocks(markdown)
    parent_block_list = []
    for block in blocks:
        type = block_to_block_type(block)
        if type == 'code':
            parent_block_list.append(ParentNode("pre", ParentNode("code", text_to_children(block))))

        if type == "paragraph":
            parent_block_list.append("p", text_to_children(block))

        if type == "quote":
            parent_block_list.append(ParentNode("blockquote"))

        if type == "unordered_list":
            parent_block_list.append(ParentNode("ul", block_to_leaf(block)))

        if type == "ordered_list":
            parent_block_list.append(ParentNode("ol", block_to_leaf(block)))

        if type == "heading1":
            parent_block_list.append(ParentNode("h1", text_to_children(block)))
        if type == "heading2":
            parent_block_list.append(ParentNode("h2", text_to_children(block)))
        if type == "heading3":
            parent_block_list.append(ParentNode("h3", text_to_children(block)))
        if type == "heading4":
            parent_block_list.append(ParentNode("h4", text_to_children(block)))
        if type == "heading5":
            parent_block_list.append(ParentNode("h5", text_to_children(block)))
        if type == "heading6":
            parent_block_list.append(ParentNode("h6", text_to_children(block)))
    
    return ParentNode("div", parent_block_list)