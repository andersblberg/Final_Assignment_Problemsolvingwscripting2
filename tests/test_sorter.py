# tests/test_sorter.py
import os
import sys
import shutil
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'C:/Users/Blomberg/Desktop/scripting/Final_Assignment_Problemsolvingwscripting2/FileOrganizer')))

from sorter import sort_files

@pytest.fixture
def setup_test_environment(tmp_path):
    # Create dummy files
    test_files = ['document.txt', 'image.jpg', 'music.mp3', 'notes.pdf']
    for file_name in test_files:
        (tmp_path / file_name).touch()
    return tmp_path

def test_sort_files(setup_test_environment):
    directory = str(setup_test_environment)
    file_types_dict = {
        'Text Files': [r'.*\.txt$', r'.*\.pdf$'],
        'Images': [r'.*\.jpg$'],
        'Audio Files': [r'.*\.mp3$']
    }
    sort_files(directory, file_types_dict)

    # Check if directories were created and files moved
    assert os.path.exists(os.path.join(directory, 'Text Files'))
    assert os.path.exists(os.path.join(directory, 'Images'))
    assert os.path.exists(os.path.join(directory, 'Audio Files'))

    # Check if files are in the correct directories
    assert os.path.exists(os.path.join(directory, 'Text Files', 'document.txt'))
    assert os.path.exists(os.path.join(directory, 'Text Files', 'notes.pdf'))
    assert os.path.exists(os.path.join(directory, 'Images', 'image.jpg'))
    assert os.path.exists(os.path.join(directory, 'Audio Files', 'music.mp3'))
