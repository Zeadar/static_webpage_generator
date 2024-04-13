import unittest

from htmlnode import HtmlNode
from htmlnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_props_to_html_ideal_case(self):
        node = HtmlNode(props= {
                   "attr1": "prop1",
                   "attr2": "prop2",
                })
        self.assertEqual(node.props_to_html(), " attr1=\"prop1\" attr2=\"prop2\"")

    def test_props_to_html_props_none(self):
        node = HtmlNode(props=None)
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_empty_dict(self):
        node = HtmlNode(props={})
        self.assertEqual(node.props_to_html(), "")

class TestLeafNode(unittest.TestCase):
    def test_to_html_ideal_case(self):
        node = LeafNode(tag="a", value="Click me!", props={"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")

    def test_to_html_no_tag(self):
        node = LeafNode(value = "sample value", tag = None)
        self.assertEqual(node.to_html(), "sample value")
    
    def test_to_html_no_prop(self):
        node = LeafNode(tag = "p", value = "This is a paragraph of text.", props = None)
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

if __name__ == "__main__":
    unittest.main()

