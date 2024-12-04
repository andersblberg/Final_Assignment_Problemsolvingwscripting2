import os
import shutil
import re
import logger

def sort_files(directory, file_types_dict):
    try:
        for root, dirs, files in os.walk(directory):
            # Exclude directories related to the script
            dirs[:] = [d for d in dirs if d not in ('file_types', '__pycache__', 'tests', 'venv', '.git')]
            
            # Exclude script files from being processed
            files = [f for f in files if f not in (
                'main.py', 'sorter.py', 'config.py', 'logger.py', 'file_sorter.log',
                '__init__.py', 'audio_files.py', 'image_files.py', 'text_files.py'
            )]
            
            # Process only files in the top-level directory
            if root != directory:
                continue

            for file in files:
                file_moved = False
                file_path = os.path.join(root, file)
                for category, patterns in file_types_dict.items():
                    for pattern in patterns:
                        if re.match(pattern, file, re.IGNORECASE):
                            dest_dir = os.path.join(directory, category)
                            if not os.path.exists(dest_dir):
                                os.makedirs(dest_dir)
                            shutil.move(file_path, os.path.join(dest_dir, file))
                            logger.log_info(f"Moved {file} to {dest_dir}")
                            file_moved = True
                            break
                    if file_moved:
                        break
                if not file_moved:
                    logger.log_info(f"No category found for {file}. Skipping.")
    except PermissionError as e:
        logger.log_error(f"Permission error: {e}")
    except Exception as e:
        logger.log_error(f"An error occurred: {e}")
