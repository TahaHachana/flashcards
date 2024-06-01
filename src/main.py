import os
import shutil

from html_template import index_template

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


def rec_list_folders_in_dir(dir):
    folders = []
    for folder in os.listdir(dir):
        folder_path = os.path.join(dir, folder)
        if os.path.isdir(folder_path):
            folders.append(folder_path)
            folders.extend(rec_list_folders_in_dir(folder_path))
    return folders


def move_up_one_dir(path):
    new_path = path.replace(CONTENT_DIR, ".")
    if new_path != ".":
        # print(f"deleting {new_path}")
        shutil.rmtree(new_path, ignore_errors=True)
    # if not os.path.exists(new_path):
    os.makedirs(new_path, exist_ok=True)
    print(f"Created directory: {new_path}")
    return new_path


folders_to_exclude = ["content", ".git", "src"]


def not_excluded_folder(folder):
    return folder not in folders_to_exclude


def write_index_html(new_path):
    folder_names = [
        name
        for name in os.listdir(new_path)
        if os.path.isdir(os.path.join(new_path, name))
    ]
    folder_names = list(filter(not_excluded_folder, folder_names))
    links = [{"href": f"./{folder}/", "text": folder} for folder in folder_names]
    context = {
        "title": "My Title",
        "links": links,
    }
    html_output = index_template.render(context)
    index_file_path = os.path.join(new_path, "index.html")
    with open(index_file_path, "w") as index_file:
        index_file.write(html_output)
        print(f"Created index.html in: {new_path}")


def contains_md_files(folder):
    for file in os.listdir(folder):
        if file.endswith(".md"):
            return True
    return False


def main():
    folders = rec_list_folders_in_dir(CONTENT_DIR)
    print(f"folders: {folders}")
    if os.path.exists("./index.html"):
        os.remove("./index.html")
    write_index_html(".")
    new_paths = []
    for folder in folders:
        new_paths.append(move_up_one_dir(folder))
    for new_path in new_paths:
        write_index_html(new_path)


if __name__ == "__main__":
    main()

# Todo: Carousel child HTML template
# Todo: Markdown to HTML conversion
# Todo: Generate carousel page from markdown files
