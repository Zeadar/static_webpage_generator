import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node1, node2)
        
    def test_eq_false(self):
        node1 = TextNode("TestText", None, "")
        node2 = TextNode("TestText", None)
        self.assertNotEqual(node1, node2)



if __name__ == "__main__":
    unittest.main()

