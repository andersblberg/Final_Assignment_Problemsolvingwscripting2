# tests/test_file_types.py
import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'C:/Users/Blomberg/Desktop/scripting/Final_Assignment_Problemsolvingwscripting2/FileOrganizer')))

from file_types import text_files, image_files

def test_text_files_patterns():
    patterns = text_files.FILE_PATTERNS
    assert isinstance(patterns, list)
    assert any(r'.*\.txt$' == pattern for pattern in patterns)

def test_image_files_patterns():
    patterns = image_files.FILE_PATTERNS
    assert isinstance(patterns, list)
    assert any(r'.*\.jpg$' == pattern for pattern in patterns)
