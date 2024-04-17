from functools import reduce

class HtmlNode:
    def __init__(self, value = None, tag = None, props = None, children = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def __repr__(self):
        return f"HtmlNode({self.value}, {self.tag}, {self.props}, {self.children})"
    def to_html(self):
        raise NotImplementedError("Booga booga")
    def props_to_html(self):
        if type(self.props) is not dict or len(self.props) == 0:
            return ""
        props_iter = [f"{key}=\"{self.props[key]}\"" for key in self.props]
        return reduce(lambda a, c: f"{a} {c}", props_iter, "")

class LeafNode(HtmlNode):
    def __init__(self, value, tag = None, props = None):
        super().__init__(value, tag, props)
    def to_html(self):
        if self.value == None:
            raise ValueError("value cannot be None")
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class VoidNode(HtmlNode):
    def __init__(self, tag, props = None):
        super().__init__(tag=tag, props=props)
    def to_html(self):
        if self.tag == None:
            raise ValueError("tag cannot be None")
        return f"<{self.tag}{self.props_to_html()}>"


def reducer(a, c):
    return a + c.to_html()

class ParentNode(HtmlNode):
    def __init__(self, children, tag = None, props = None):
        super().__init__(tag = tag, children = children, props = props)
    def to_html(self):
        if self.tag == None:
            raise ValueError("No tag")
        if self.children == None or len(self.children) == 0:
            raise ValueError("No children")
        return f"<{self.tag}{self.props_to_html()}>{reduce(reducer, self.children, '')}</{self.tag}>"

