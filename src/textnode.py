#Types of textnodes (Global)

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

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