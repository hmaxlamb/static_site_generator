import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def propstest(self):
        node1 = HTMLNode(None, None, None, {"href": "https://www.google.com", "target": "_blank"})
        correct_prop = 'href="https://www.google.com" target="_blank"'
        self.assertEqual(node1.props_to_html(), correct_prop)

    def eq_test(self):
        node2 = HTMLNode("<a>", "test string", None, {"href": "https://www.google.com", "target": "_blank"})
        node3 = HTMLNode("<a>", "test string", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node2, node3)

if __name__ == "__main__":
    unittest.main()
