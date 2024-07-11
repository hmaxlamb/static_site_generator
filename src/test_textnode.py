import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq_url(self):
        node3 = TextNode("This is a Node", "underlined", "http://website.xyz")
        node4 = TextNode("This is a Node", "underlined", "http://website.xyz")
        self.assertEqual(node3, node4)
    
    def test_eq_v2(self):
        node5 = TextNode("This is a Node", "underlined", "")
        node6 = TextNode("This is a Node", "underlined", "")
        self.assertEqual(node5, node6)



if __name__ == "__main__":
    unittest.main()

