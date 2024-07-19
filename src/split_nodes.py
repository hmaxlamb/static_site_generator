from textnode import (                                                                                                                                                                          
    text_type_bold,
    text_type_code,
    text_type_image,
    text_type_italic,
    text_type_link,
    text_type_text,
    TextNode
)


def split_node_delimiter(old_nodes, delimiter, text_type):
    new_node_list = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_node_list.append(node)
        split_text = node.text.split(delimiter)
        if split_text == node.text:
            raise ValueError("Invalid delimiter")
        new_node_list.extend([
            TextNode(split_text[0], text_type_text)
            TextNode(split_text[1], text_type)
            TextNode(split_text[3], text_type_text)
        ])
