import os
import json


def get_file_tree(dir_path: str, items_to_ignore: list[str]) -> list[dict]:
    file_tree = []
    for item in os.listdir(dir_path):
        if item in items_to_ignore:
            continue

        full_path = os.path.join(dir_path, item)
        if os.path.isdir(full_path):
            file_tree.append({
                "name": item,
                "type": "folder",
                "children": get_file_tree(full_path, items_to_ignore)
            })
        else:
            file_tree.append({
                "name": item,
                "type": "file"
            })
    return file_tree


if __name__ == "__main__":
    items_to_ignore = ['node_modules', '.git']
    file_tree = get_file_tree(
        dir_path=os.path.dirname(os.getcwd()),
        items_to_ignore=items_to_ignore
    )
    json.dump(file_tree, open("file_tree.json", "w"), indent=2)
