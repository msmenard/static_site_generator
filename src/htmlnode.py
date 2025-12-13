class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if not self.props:
            return ""
        all_attributes = ""
        for key, value in self.props.items():
            all_attributes += f' {key}="{value}"'
        return all_attributes
        
    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)
    
    def to_html(self):
        added_props = self.props_to_html()
        if not self.value:
            raise ValueError
        if not self.tag:
            return self.value        
        return f"<{self.tag}{added_props}>{self.value}</{self.tag}>"
        