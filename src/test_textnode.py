import unittest

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

    def test_text_to_html_text(self):
        node14 = LeafNode(None, "this is a test")
        node15 = text_node_to_html_node(TextNode("this is a test", "text"))
        self.assertEqual(node14.tag, node15.tag)
        self.assertEqual(node14.value, node15.value)

    def test_split_node1(self):
        node16 = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_node_delimiter([node16], "`", text_type_code)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" word", text_type_text),
        ])

    def test_image_spliter(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        extracted_list = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(extracted_list, extract_markdown_images(text))

    def test_image_spliter(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"        
        extracted_list = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(extract_markdown_links(text), extracted_list)
    
    def split_node_links_test(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            text_type_text,
        )
        new_node_list = [
            TextNode("This is text with a link ", text_type_text),
            TextNode("to boot dev", text_type_link, "https://www.boot.dev"),
            TextNode(" and ", text_type_text),
            TextNode(
                "to youtube", text_type_link, "https://www.youtube.com/@bootdotdev"     
            ),]
        self.assertEqual(new_node_list, split_node_link([node]))
    
    def split_node_image_test(self):
        node = TextNode(
            "This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",
            text_type_text,
        )
        new_node_list = [
            TextNode("This is text with a link ", text_type_text),
            TextNode("to boot dev", text_type_image, "https://www.boot.dev"),
            TextNode(" and ", text_type_image),
            TextNode(
                "to youtube", text_type_link, "https://www.youtube.com/@bootdotdev"     
            ),]
        self.assertEqual(new_node_list, split_node_image([node]))
        
        
        
if __name__ == "__main__":
    unittest.main()

