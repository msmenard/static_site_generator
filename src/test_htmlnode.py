import unittest

from htmlnode import HTMLNode


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


if __name__ == "__main__":
    unittest.main()