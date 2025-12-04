import unittest
from htmlnode import HtmlNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HtmlNode(props={"href": "https://www.google.com", "target": "_blank"})
        expected = ' href="https://www.google.com" target="_blank"'
        actual = node.props_to_html()
        self.assertEqual(expected, actual)

    def test_values(self):
        node = HtmlNode()
        expected = ""
        actual = node.props_to_html()
        self.assertEqual(expected, actual)
    
    def test_storage(self):
        node = HtmlNode(tag="div", value="I am a div")
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "I am a div")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)
        
if __name__ == "__main__":
    unittest.main()