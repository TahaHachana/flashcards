import os
import shutil

from html_template import html_output

CONTENT_DIR = "./content"

# import sys
# import markdown

# markdown_text = """
# # Heading
# - List item 1
# - List item 2
# """

# html = markdown.markdown(markdown_text)
# print(html)


# print(sys.executable)

def list_folders_in_dir(dir):
    for folder in os.listdir(dir):
        folder_path = os.path.join(dir, folder)
        if os.path.isdir(folder_path):
            print(folder_path)
            list_folders_in_dir(folder_path)

def create_index_file(path):
    new_path = path.replace(CONTENT_DIR, ".")
    if new_path != ".":
        shutil.rmtree(new_path) #, ignore_errors=True)
    # if not os.path.exists(new_path):
    os.makedirs(new_path)
    print(f"Created directory: {new_path}")
    index_file_path = os.path.join(new_path, 'index.html')
    with open(index_file_path, 'w') as index_file:
        index_file.write("<html><body><h1>Index</h1></body></html>")
        print(f"Created index.html in: {new_path}")

def main():
    folders = list_folders_in_dir(CONTENT_DIR)
    create_index_file(CONTENT_DIR)
    for folder in folders:
        create_index_file(folder)

if __name__ == "__main__":
    main()