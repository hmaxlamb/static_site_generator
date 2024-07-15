class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise Exception(NotImplementedError)
    
    def props_to_html(self):
        return_string = f""
        for key in self.props:
            return_string = return_string + f'''{key}="{self.props[key]}" '''
        if len(return_string) > 1:
            return_string = return_string[:-1]
        return return_string
    
    def __repr__(self):
        return f"{self.tag}, {self.value}, {self.children}, {self.props}"
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super.__init__(tag, value, None, props)
        if self.value == None:
            raise ValueError("No value for 'value' found")
    
    def to_html(self):
        if self.value == None:
            raise ValueError("No value for 'value' found")
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"