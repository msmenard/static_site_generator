import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a sandwich", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_url(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT, url=None)
        self.assertEqual(node, node2)

    def test_types(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_different_urls_not_equal(self):
        node = TextNode("img", TextType.LINK, "https://a.com")
        node2 = TextNode("img", TextType.LINK, "https://b.com")
        self.assertNotEqual(node, node2)

    def test_not_equal_to_other_type(self):
        node = TextNode("text", TextType.TEXT)
        self.assertNotEqual(node, "text")

if __name__ == "__main__":
    unittest.main()