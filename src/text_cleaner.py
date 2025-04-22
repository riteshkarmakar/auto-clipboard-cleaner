import re
from typing import Literal


class TextCleaner:
    def __init__(self, text: str) -> None:
        self.original_text = text
        self.cleaned_text = text

    def trim(self) -> str:
        self.cleaned_text = self.cleaned_text.strip()
        return self.cleaned_text
        
    def remove_blank_lines(self) -> str:
        self.cleaned_text = re.sub(r'\n\s*\n', '\n', self.cleaned_text)
        return self.cleaned_text
        
    def replace_linebreak_with_space(self) -> str:
        self.cleaned_text = ' '.join(self.cleaned_text.splitlines())
        return self.cleaned_text
        
    def multiple_spaces_to_single(self) -> str:
        self.cleaned_text = re.sub(r'\s{2,}', ' ', self.cleaned_text)
        return self.cleaned_text

    def to_uppercase(self) -> str:
        self.cleaned_text = self.cleaned_text.upper()
        return self.cleaned_text
        
    def to_lowercase(self) -> str:
        self.cleaned_text = self.cleaned_text.lower()
        return self.cleaned_text
        
    def to_capitalize_case(self) -> str:
        self.cleaned_text = self.cleaned_text.title()
        return self.cleaned_text
        
    def to_sentence_case(self) -> str:
        self.cleaned_text = '. '.join(
            sentence.capitalize() for sentence in self.cleaned_text.split('. ')
        )
        return self.cleaned_text
    
    def numbered_list_to_plain(self) -> str:
        self.cleaned_text = '\n'.join(
            re.sub(r'^\d+\.[ \t]', '', line) for line in self.cleaned_text.splitlines()
        )
        return self.cleaned_text

    def wrap_text(self, wrap_with: Literal["Parentheses", "Curly Brackets", "Square Brackets", "Single Quotes", "Double Quotes"]) -> str:
        wrap_chars = {
            "Parentheses": ("(", ")"),
            "Curly Brackets": ("{", "}"),
            "Square Brackets": ("[", "]"),
            "Single Quotes": ("'", "'"),
            "Double Quotes": ('"', '"')
        }
        if wrap_with in wrap_chars:
            start_wrap, end_wrap = wrap_chars[wrap_with]
            self.cleaned_text = start_wrap + self.cleaned_text + end_wrap
        return self.cleaned_text
    
    def find_and_replace(self, find_text: str, replace_with: str) -> str:
        self.cleaned_text = self.cleaned_text.replace(find_text, replace_with)
        return self.cleaned_text

    def get_cleaned_text(self) -> str:
        return self.cleaned_text
