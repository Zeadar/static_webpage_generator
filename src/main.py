from textnode import TextNode
from htmlnode import LeafNode
from htmlnode import VoidNode

TEXT_TYPE_TEXT = "text"
TEXT_TYPE_BOLD = "bold"
TEXT_TYPE_ITALIC = "italic"
TEXT_TYPE_CODE = "code"
TEXT_TYPE_LINK = "link"
TEXT_TYPE_IMAGE = "image"

def main():
    test = TextNode("This is a text node", "bold", "https://boot.dev")
    print(test)
    node = TextNode("This is text with a `code block` word", TEXT_TYPE_TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TEXT_TYPE_CODE)

def text_node_to_html_node(text_node):
    if text_node.text_type == TEXT_TYPE_TEXT:
        return LeafNode(text_node.text)
    if text_node.text_type == TEXT_TYPE_BOLD:
        return LeafNode(text_node.text, tag="b")
    if text_node.text_type == TEXT_TYPE_ITALIC:
        return LeafNode(text_node.text, tag="i")
    if text_node.text_type == TEXT_TYPE_CODE:
        return LeafNode(text_node.text, tag="code")
    if text_node.text_type == TEXT_TYPE_LINK:
        return LeafNode(text_node.text, tag="a", props={"href": text_node.url})
    if text_node.text_type == TEXT_TYPE_IMAGE:
        return VoidNode("img", props={"src": text_node.url, "alt": text_node.text})
    raise ValueError(f"unknown value \"{text_node.text_type}\"")

def multiplsitter(text, delimiter, text_type):
    new_nodes = []
    for i, s in enumerate(text.split(delimiter, 4)):
        new_nodes.append(TextNode(s, text_type if i == 1 else TEXT_TYPE_TEXT))
                          
    if len(new_nodes) == 4:
        return List(new_nodes[:3]).extend(multiplsitter(new_nodes[3], delimiter, text_type))

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TEXT_TYPE_TEXT:
            new_nodes.append(old_node)
            continue



main()
