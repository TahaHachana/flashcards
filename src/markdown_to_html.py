import markdown
import re


def split_markdown_text(markdown_text):

    code_block = re.search(r"```.*?```", markdown_text, re.DOTALL)
    if code_block:
        code_block = code_block.group()
        markdown_text = markdown_text.replace(code_block, "")
    return markdown_text, code_block


def markdown_to_html(markdown_text):
    html = markdown.markdown(markdown_text, extensions=["fenced_code"])
    return html
