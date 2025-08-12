
def parse_special_characters(text: str):
    special_chars = {
        r'\n': '\n',  # Newline
        r'\t': '\t',  # Tab
        r'\r': '\r',  # Carriage return
        r'\\': '\\',  # Literal backslash
        r'\a': '\a',  # Bell
        r'\b': '\b',  # Backspace
        r'\f': '\f',  # Form feed
        r'\v': '\v',  # Vertical tab
    }
    
    for string_repr, char in special_chars.items():
        text = text.replace(string_repr, char)
    
    return text
