import markdown
#import re


class Flashcard:
    def __init__(self, question, answer): #, code):
        self.question = question
        self.answer = answer
#        self.code = code


def flashcard_from_md(md):
    sections = md.split("---")
    sections = [part.strip() for part in sections]
    if len(sections) != 2:
        raise ValueError(
            "The markdown text does not contain exactly two sections separated by '---'"
        )
    return Flashcard(sections[0], sections[1]) #, sections[2])


# def split_markdown_text(markdown_text):

#     code_block = re.search(r"```.*?```", markdown_text, re.DOTALL)
#     if code_block:
#         code_block = code_block.group()
#         markdown_text = markdown_text.replace(code_block, "")
#     return markdown_text, code_block


def markdown_to_html(markdown_text):
    html = markdown.markdown(markdown_text, extensions=["fenced_code"])
    return html
