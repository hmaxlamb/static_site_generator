from htmlnode import HTMLNode

def main():
    testnode = HTMLNode(None, None, None, {"href": "https://www.google.com", "target": "_blank"})
    print(testnode.props_to_html())

main()