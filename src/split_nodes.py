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

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)

def split_node_image(old_nodes):
    return_list = []
    for node in old_nodes:
        pair_array = extract_markdown_images(node.text)
        for i in range(len(pair_array)):
            if i == 0:
                sections = []
                sections = node.text.split(f"![{pair_array[i][0]}]({pair_array[i][1]})", 1)
                new_array = [
                    TextNode(sections[0], text_type_text),
                    TextNode(pair_array[i][0], text_type_image, pair_array[i][1])
                ]
            elif i != len(pair_array) - 1 and i != 0:
                sections = []
                sections = node.text.split(f"![{pair_array[i][0]}]({pair_array[i][1]})", 1)
                text_before = sections[0].split(f"![{pair_array[(i-1)][0]}]({pair_array[(i-1)][1]})", 1)
                new_array = [
                    TextNode(text_before[1], text_type_text),
                    TextNode(pair_array[i][0], text_type_image, pair_array[i][1])
                ]
            else:
                sections = []
                sections = node.text.split(f"![{pair_array[i][0]}]({pair_array[i][1]})", 1)
                text_before = sections[0].split(f"![{pair_array[i-1][0]}]({pair_array[i-1][1]})", 1)
                if len(sections) == 2 and sections[1] != "":
                    new_array = [
                    TextNode(text_before[1], text_type_text),
                    TextNode(pair_array[i][0], text_type_image, pair_array[i][1]),
                    TextNode(sections[1], text_type_text)
                ]
                else:
                    new_array = [
                    TextNode(text_before[1], text_type_text),
                    TextNode(pair_array[i][0], text_type_image, pair_array[i][1])
                ]
            return_list.extend(new_array)
    return return_list 

def split_node_link(old_nodes):
    return_list = []
    for node in old_nodes:
        pair_array = extract_markdown_links(node.text)
        for i in range(len(pair_array)):
            if i == 0:
                sections = []
                sections = node.text.split(f"[{pair_array[i][0]}]({pair_array[i][1]})", 1)
                new_array = [
                    TextNode(sections[0], text_type_text),
                    TextNode(pair_array[i][0], text_type_link, pair_array[i][1])
                ]
            elif i != len(pair_array) - 1 and i != 0:
                sections = []
                sections = node.text.split(f"[{pair_array[i][0]}]({pair_array[i][1]})", 1)
                text_before = sections[0].split(f"[{pair_array[(i-1)][0]}]({pair_array[(i-1)][1]})", 1)
                new_array = [
                    TextNode(text_before[1], text_type_text),
                    TextNode(pair_array[i][0], text_type_link, pair_array[i][1])
                ]
            else:
                sections = []
                sections = node.text.split(f"[{pair_array[i][0]}]({pair_array[i][1]})", 1)
                text_before = sections[0].split(f"[{pair_array[i-1][0]}]({pair_array[i-1][1]})", 1)
                if len(sections) == 2 and sections[1] != "":
                    new_array = [
                    TextNode(text_before[1], text_type_text),
                    TextNode(pair_array[i][0], text_type_link, pair_array[i][1]),
                    TextNode(sections[1], text_type_text)
                ]
                else:
                    new_array = [
                    TextNode(text_before[1], text_type_text),
                    TextNode(pair_array[i][0], text_type_link, pair_array[i][1])
                ]
            return_list.extend(new_array)
    return return_list  

def text_to_textnodes(text):
    nodes = [TextNode(text, text_type_text)]
    nodes = split_nodes_delimiter(nodes, "**", text_type_bold)
    nodes = split_nodes_delimiter(nodes, "*", text_type_italic)
    nodes = split_nodes_delimiter(nodes, "`", text_type_code)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes