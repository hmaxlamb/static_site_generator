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
        split_node = []
        split_text = node.text.split(delimiter)
        if len(split_text) % 2 == 0:
            raise ValueError("Invalid Markdown, delimeter not closed")
        for i in range(len(split_text)):
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
    
        
