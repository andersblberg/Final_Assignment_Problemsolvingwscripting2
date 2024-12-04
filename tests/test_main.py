import os
import sys
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'C:/Users/Blomberg/Desktop/scripting/Final_Assignment_Problemsolvingwscripting2/FileOrganizer')))

from main import load_file_types

def test_load_file_types():
    file_types = load_file_types()
    assert isinstance(file_types, dict)
    assert 'Text Files' in file_types
    assert 'Images' in file_types
    assert isinstance(file_types['Text Files'], list)
    assert len(file_types['Text Files']) > 0
