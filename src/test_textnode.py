import unittest

from textnode import (
     TextNode,
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

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq_url(self):
        node3 = TextNode("This is a Node", text_type_code, "http://website.xyz")
        node4 = TextNode("This is a Node", text_type_code, "http://website.xyz")
        self.assertEqual(node3, node4)
    
    def test_eq_v2(self):
        node5 = TextNode("This is a Node", "underlined", "")
        node6 = TextNode("This is a Node", "underlined", "")
        self.assertEqual(node5, node6)
    
    def test_nteq(self):
        node7 = TextNode("This is a Node", text_type_bold, "http://website.xyz")
        node8 = TextNode("This is a Node", text_type_link, "http://notawebsite.xyz")
        self.assertNotEqual(node7, node8)

    def test_num(self):
        node9 = TextNode("This is a Node", 7, "http://website.xyz")
        node10 = TextNode("This is a Node", 7, "http://website.xyz")
        self.assertEqual(node9, node10)

    def test_none(self):
        node11 = TextNode("This is a Node", 7, None)
        node12 = TextNode("This is a Node", 7, None)
        self.assertEqual(node11, node12)

    def test_parent(self):
        parentnode1 = ParentNode("p", [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
        ])
        correct_string = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(parentnode1.to_html(), correct_string)


if __name__ == "__main__":
    unittest.main()

