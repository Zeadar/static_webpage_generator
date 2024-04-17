from textnode import TextNode
from htmlnode import LeafNode
from htmlnode import VoidNode

def main():
    test = TextNode("This is a text node", "bold", "https://boot.dev")
    print(test)

def text_node_to_html_node(text_node):
    if text_node.text_type == "text":
        return LeafNode(text_node.text)
    if text_node.text_type == "bold":
        return LeafNode(text_node.text, tag="b")
    if text_node.text_type == "italic":
        return LeafNode(text_node.text, tag="i")
    if text_node.text_type == "code":
        return LeafNode(text_node.text, tag="code")
    if text_node.text_type == "link":
        return LeafNode(text_node.text, tag="a", props={"href": text_node.url})
    if text_node.text_type == "image":
        return VoidNode("img", props={"src": text_node.url, "alt": text_node.text})
    raise NotImplementedError(f"unknown type \"{text_node.text_type}\"")

main()
