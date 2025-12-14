import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_multiple_children(self):
        children = [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ]
        parent_node = ParentNode("p", children)
        self.assertEqual(parent_node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_children_with_props(self):
        child_node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        parent_node = ParentNode("p", [child_node])
        self.assertEqual(parent_node.to_html(), '<p><a href="https://www.google.com">Click me!</a></p>')
    
    def test_to_html_with_children_missing(self):
        parent_node = ParentNode("div", [])
        with self.assertRaises(ValueError) as ctx:
            parent_node.to_html()
        self.assertEqual(str(ctx.exception), "Children are missing.")

    def test_to_html_with_tag_missing(self):
        parent_node = ParentNode(None, [LeafNode("b", "x")])
        with self.assertRaises(ValueError) as ctx:
            parent_node.to_html()
        self.assertEqual(str(ctx.exception), "Tag is missing.")

if __name__ == "__main__":
    unittest.main()