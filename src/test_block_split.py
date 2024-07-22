import unittest

from block_split import(
    markdown_to_blocks,
    block_to_block_type,
)

class TestBlockSplit(unittest.TestCase):
    def test_block_split(self):
        markdown_file = open("src/test_html/test1.html")
        markdown = markdown_file.read()
        markdown_file.close()
        list_of_block = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item",
        ]
        self.assertEqual(list_of_block, markdown_to_blocks(markdown))

class TestBlockType(unittest.TestCase):
    def test_block_to_block_order1(self):
        block = "1. hi\n2. mmmm\nhohohoh"
        self.assertEqual("paragraph", block_to_block_type(block))

    def test_block_to_block_order2(self):
        block = "1. hi\n2. mmmm\3. hehe"
        self.assertEqual("ordered_list", block_to_block_type(block))

    def test_block_to_block_unorder1(self):
        block = "* ahhhh\n* ahhhhh\n* eeeeeee"
        self.assertEqual("unordered_list", block_to_block_type(block))
    
    def test_block_to_block_unorder2(self):
        block = "* ahhhh\n* ahhhhh\n eeeeeee"
        self.assertEqual("paragraph", block_to_block_type(block))

    def test_block_to_block_unorder3(self):
        block = "- ahhhh\n- ahhhhh\n- eeeeeee"
        self.assertEqual("unordered_list", block_to_block_type(block))
    
    def test_block_to_block_unorder4(self):
        block = "- ahhhh\n- ahhhhh\n eeeeeee"
        self.assertEqual("paragraph", block_to_block_type(block))

    def test_block_to_block_head1(self):
        block = "# Hello"
        self.assertEqual("heading", block_to_block_type(block))
    