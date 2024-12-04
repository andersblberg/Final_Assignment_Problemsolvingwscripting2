import os
import sys
import sorter
import logger
import config
import importlib

def load_file_types():
    file_types_dict = {}
    file_types_dir = os.path.join(os.path.dirname(__file__), 'file_types')
    for filename in os.listdir(file_types_dir):
        if filename.endswith('.py') and filename != '__init__.py':
            module_name = f"file_types.{filename[:-3]}"
            module = importlib.import_module(module_name)
            if hasattr(module, 'FILE_PATTERNS'):
                file_types_dict[module.CATEGORY_NAME] = module.FILE_PATTERNS
    return file_types_dict

def main():
    try:
        target_directory = config.TARGET_DIRECTORY
        if not os.path.exists(target_directory):
            raise FileNotFoundError(f"Directory {target_directory} does not exist.")

        file_types_dict = load_file_types()
        sorter.sort_files(target_directory, file_types_dict)

    except Exception as e:
        logger.log_error(str(e))
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
