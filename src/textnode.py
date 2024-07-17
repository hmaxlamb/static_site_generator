#Types of textnodes (Global)

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

from htmlnode import LeafNode

#Creats textnode class for static site gen

class TextNode:
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url


#Checks if the textnode itself and another are equal

    def __eq__(self, other_node):
        if (self.text == other_node.text and
            self.text_type == other_node.text_type and
            self.url == other_node.url):
            return True
    
#Returns the objects in the textnode instance via string

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    

def text_node_to_html_node(text_node):
    if text_node.text_type == "bold":
        return LeafNode("b", text_node.text)
    if text_node.text_type == "text":
        return LeafNode(None, text_node.text)
    if text_node.text_type == "italic":
        return LeafNode("i", text_node.text)
    if text_node.text_type == "code":
        return LeafNode("code", text_node.text)
    if text_node.text_type == "link":
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if text_node.text_type == "image":
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    else:
        raise ValueError(f"Invalid text type: {text_node.text_type}")