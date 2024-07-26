import unittest

from copy_file import (
    extract_title
)

class TestExtractTitle(unittest.TestCase):

    def test_extract_title1(self):
        markdown = '''
##### wrong header

# hello     
normal text

'''
        self.assertEqual(extract_title(markdown), "hello")


    def test_extract_title2(self):
        markdown = '''
##### wrong header

#     hello hi!       
normal text

'''
        self.assertEqual(extract_title(markdown),"hello hi!")



if __name__ == "__main__":
    unittest.main()