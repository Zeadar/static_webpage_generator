class TextNode:
    def __init__(self, text = "", text_type = "normal", url = None):
        self.text = text
        self.text_type = text_type
        self.url = url
    def __str__(self):
        return f"text {self.text}\ntext_type {self.text_type}\nurl {self.url}"
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

