from textnode import TextNode

def main():
    testnode = TextNode("This is a test", "Bold", "www.test.example.com")
    print(testnode.__repr__())

main()