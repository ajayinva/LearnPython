class Element:
    def __init__(self, text=None, sub_element=None):
        self.text = text
        self.sub_element = sub_element

    def __str__(self):
        value = "<{}>\n".format(self.__class__.__name__)
        if self.text:
            value += "{}\n".format(self.text)
        if self.sub_element:
            value += str(self.sub_element)
        value += "</{}>\n".format(self.__class__.__name__)
        return value


class Paragraph(Element):
    def __init__(self, text=None, sub_element=None):
        super().__init__(text, sub_element)


class Body(Element):
    def __init__(self, text=None, sub_element=None):
        super().__init__(text, sub_element)


class Html(Element):
    def __init__(self, text=None, sub_element=None):
        super().__init__(text, sub_element)


p = Paragraph(text="This is a paragraph text")
body = Body("This is the Body Text", p)
html = Html(sub_element=body)

print(html)


