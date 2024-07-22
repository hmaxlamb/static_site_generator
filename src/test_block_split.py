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
        self.assertEqual("heading1", block_to_block_type(block))

    def test_block_to_block_head2(self):
        block = "## Hello"
        self.assertEqual("heading2", block_to_block_type(block))

    def test_block_to_block_head3(self):
        block = "### Hello"
        self.assertEqual("heading3", block_to_block_type(block))

    def test_block_to_block_head4(self):
        block = "#### Hello"
        self.assertEqual("heading4", block_to_block_type(block))

    def test_block_to_block_head5(self):
        block = "##### Hello"
        self.assertEqual("heading5", block_to_block_type(block))

    def test_block_to_block_head6(self):
        block = "###### Hello"
        self.assertEqual("heading6", block_to_block_type(block))

    def test_block_to_block_head7(self):
        block = "####### Hello"
        self.assertEqual("paragraph", block_to_block_type(block))

    def test_block_to_block_quote1(self):
        block = "> ahhhh\n> ahhhhh\n> eeeeeee"
        self.assertEqual("quote", block_to_block_type(block))
    
    def test_block_to_block_quote2(self):
        block = "> ahhhh\n> ahhhhh\n eeeeeee"
        self.assertEqual("paragraph", block_to_block_type(block))

    def test_block_to_block_para(self):
        block = "sdfgksjdhgpwoshg"
        self.assertEqual("paragraph", block_to_block_type(block))

    def test_block_to_block_code1(self):
        block = "``` sdfgksjdhgpwoshg ```"
        self.assertEqual("code", block_to_block_type(block))
    
    def test_block_to_block_code2(self):
        block = "``` sdfgksjdhgpwoshg ``"
        self.assertEqual("paragraph", block_to_block_type(block))


    