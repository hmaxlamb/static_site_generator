from textnode import (                                                                                                                                                                          
    text_type_bold,
    text_type_code,
    text_type_image,
    text_type_italic,
    text_type_link,
    text_type_text,
    TextNode
)

import re

def split_node_delimiter(old_nodes, delimiter, text_type_del):
    new_node_list = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_node_list.append(node)
            continue
        split_node = []
        split_text = node.text.split(delimiter)
        if len(split_text) % 2 == 0:
            raise ValueError("Invalid Markdown, delimeter not closed")
        for i in range(0, len(split_text)):
            if split_text[i] == "":
                continue
            if i % 2 == 0:
                split_node.append(TextNode(split_text[i], text_type_text))
            else:
                split_node.append(TextNode(split_text[i], text_type_del))
        new_node_list.extend(split_node)
    return new_node_list

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)

def split_node_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))
            new_nodes.append(
                TextNode(
                    image[0],
                    text_type_image,
                    image[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))
    return new_nodes

def split_node_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))
            new_nodes.append(TextNode(link[0], text_type_link, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))
    return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, text_type_text)]
    nodes = split_node_delimiter(nodes, "**", text_type_bold)
    nodes = split_node_delimiter(nodes, "*", text_type_italic)
    nodes = split_node_delimiter(nodes, "`", text_type_code)
    nodes = split_node_image(nodes)
    nodes = split_node_link(nodes)
    return nodes