import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        node = HTMLNode("p", "This is an HTML node test for props = None", None, None)
        node2 = HTMLNode("p", "This is an HTML node test for props = {}", None, {})
        node3 = HTMLNode("p", "This is an HTML node test for props = href and target", None, {"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), "")
        self.assertEqual(node2.props_to_html(), "")
        self.assertEqual(node3.props_to_html(), ' href="https://www.google.com"')

    def test_multiple_props(self):
        node = HTMLNode(
            "a",
            "link",
            None,
            {"href": "https://www.google.com", "target": "_blank"},
        )
        # Think carefully: what *exact* string (including spaces and order) should props_to_html return?
        expected = ' href="https://www.google.com" target="_blank"'  # fill in once you're sure
        self.assertEqual(node.props_to_html(), expected)

    def test_leaf_node(self):
        node = LeafNode("p", "This is a paragraph of text.")
        expected = "<p>This is a paragraph of text.</p>"
        self.assertEqual(node.to_html(), expected)

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        expected = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(node.to_html(), expected)


    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

if __name__ == "__main__":
    unittest.main()