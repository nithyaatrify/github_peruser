import os
import json

def is_code_file(filename):
    code_extensions = ['.py', '.java', '.cpp', '.html', '.css', '.js', '.txt','.ipynb','.md']
    return any(filename.endswith(ext) for ext in code_extensions)

def parse_project_folder(folder_path, output_json_path):
    code_contents = {}

    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)

            if not is_code_file(file_name):
                continue

            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                content = file.read()
                code_contents[file_name] = content

    with open(output_json_path, 'w') as json_file:
        json.dump(code_contents, json_file, indent=4)

if __name__ == "__main__":
    project_folder = "file_path"  
    output_json_file = "code_contents.json" 

    parse_project_folder(project_folder, output_json_file)
    print(f"Code contents saved to {output_json_file}")
