import unittest

from split_node_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitNodeDelimeter(unittest.TestCase):
    def test_code_text(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)

    def test_bold_text(self):
        node = TextNode("This is text with a **bolded phrase** in the middle", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bolded phrase", TextType.BOLD),
            TextNode(" in the middle", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)

    def test_italic_text(self):
        node = TextNode("This is text with an _italic phrase_ in the middle", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        expected = [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("italic phrase", TextType.ITALIC),
            TextNode(" in the middle", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)


if __name__ == "__main__":
    unittest.main()