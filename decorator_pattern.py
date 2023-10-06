# Component (Base interface)
class TextEditor:
    def write(self, text):
        pass

# Concrete Component (Base class)


class SimpleTextEditor(TextEditor):
    def write(self, text):
        print(f"Writing: {text}")

# Decorator (Abstract class)


class TextDecorator(TextEditor):
    def __init__(self, wrapped):
        self._wrapped = wrapped

    def write(self, text):
        self._wrapped.write(text)

# Concrete Decorator


class BoldDecorator(TextDecorator):
    def write(self, text):
        print(f"<b>{text}</b>")

# Concrete Decorator


class ItalicDecorator(TextDecorator):
    def write(self, text):
        print(f"<i>{text}</i>")


# Client code
if __name__ == "__main__":
    simple_editor = SimpleTextEditor()
    bold_editor = BoldDecorator(simple_editor)
    italic_bold_editor = ItalicDecorator(bold_editor)

    simple_editor.write("Plain text")  # Output: Writing: Plain text
    bold_editor.write("Bold text")  # Output: <b>Bold text</b>
    # Output: <i><b>Italic and Bold text</b></i>
    italic_bold_editor.write("Italic and Bold text")
