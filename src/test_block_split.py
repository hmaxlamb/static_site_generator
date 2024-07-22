import unittest

from block_split import markdown_to_blocks

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
