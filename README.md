# File Organizer

## Introduction

The File Organizer is a Python program designed to automate the organization of files within a specified directory based on their file types. It scans the directory, identifies files using regular expressions, and moves them into categorized folders such as "Text Files," "Images," and "Audio Files." This tool simplifies file management, reduces clutter, and enhances productivity by making file retrieval more efficient.

## Features

- **File Handling**: Traverses directories and moves files into appropriate folders based on their types.
- **Modular Design**: Separates sorting logic, configuration, and logging into distinct modules for better maintainability.
- **Metaprogramming**: Dynamically adds new file type categories without modifying the core logic.
- **Error Handling**: Manages permissions issues and handles non-existent directories gracefully.
- **Regular Expressions**: Identifies file types using pattern matching.
- **Unit Testing**: Includes tests using `pytest` to verify the correctness of modules.

## Project Structure

```
project/
├── main.py
├── sorter.py
├── config.py
├── logger.py
├── file_types/
│   ├── __init__.py
│   ├── text_files.py
│   ├── image_files.py
│   └── audio_files.py
└── tests/
    ├── __init__.py
    ├── test_main.py
    ├── test_sorter.py
    └── test_file_types.py
```

- **main.py**: The entry point of the application.
- **sorter.py**: Contains the logic for sorting and moving files.
- **config.py**: Stores configuration settings like the target directory.
- **logger.py**: Manages logging of informational messages and errors.
- **file_types/**: A package containing modules that define file type categories and patterns.
- **tests/**: Contains unit tests for the modules.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/andersblberg/Final_Assignment_Problemsolvingwscripting2.git
   cd fileorganizer
   ```

2. **Set Up a Virtual Environment (Optional but Recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   *Note: If you don't want to use `requirements.txt`, you can manually install `pytest` if you plan to run tests:*

   ```bash
   pip install pytest
   ```

## Usage

1. **Configure the Target Directory**

   Open `config.py` and set the `TARGET_DIRECTORY` variable to the path of the directory you want to organize:

   ```python
   # config.py
   TARGET_DIRECTORY = '...'  # Replace with your actual directory path
   ```

   *Note for Windows Users*: Use forward slashes (`/`) or double backslashes (`\\`) in paths to avoid escape character issues.

2. **Run the Script**

   Execute the `main.py` script using Python:

   ```bash
   python main.py
   ```

3. **Check the Organized Files**

   The script will organize files in the target directory into subfolders based on their file types.

4. **Review Logs**

   A log file named `file_sorter.log` will be created in the project directory. It contains information about moved files and any errors encountered.

## Configuration

### Adding New File Type Categories

You can add new file type categories by creating a new Python file in the `file_types` directory. Each file should define:

- `CATEGORY_NAME`: The name of the category (used as the folder name).
- `FILE_PATTERNS`: A list of regular expression patterns to match file names.

**Example:**

```python
# file_types/audio_files.py

CATEGORY_NAME = 'Audio Files'
FILE_PATTERNS = [
    r'.*\.mp3$',
    r'.*\.wav$',
    r'.*\.aac$',
    r'.*\.flac$',
]
```

The script will automatically detect and incorporate new file type modules without any changes to the core code.

## Testing

### Running Unit Tests

The project includes unit tests using `pytest`. To run the tests, execute:

```bash
pytest
```

### Test Cases Covered

- **Test `load_file_types` Function**

  Ensures that file type modules are loaded correctly.

- **Test `sort_files` Function**

  Verifies that files are moved to the correct directories based on patterns.

- **Test File Type Patterns**

  Checks that `FILE_PATTERNS` are correctly defined in each file type module.

### Test Output

You should see output indicating that all tests have passed:

```bash
============================================== test session starts ================================================
platform win32 -- Python 3.x.x, pytest-x.x.x, pluggy-x.x.x
collected 4 items

tests/test_file_types.py ..                                                                                   [ 50%]
tests/test_main.py .                                                                                          [ 75%]
tests/test_sorter.py .                                                                                        [100%]

=============================================== 4 passed in 0.07s =================================================
```

## Project Details

### main.py

- **Functions**:
  - `load_file_types()`: Dynamically loads file type modules.
  - `main()`: The main function that orchestrates the process.
- **Error Handling**: Catches exceptions and logs errors.

### sorter.py

- **Function**:
  - `sort_files(directory, file_types_dict)`: Sorts files into categories.
- **Exclusions**: Skips specified directories and files to prevent processing the script's own files.

### config.py

- **Variables**:
  - `TARGET_DIRECTORY`: The path of the directory to organize.

### logger.py

- **Logging Configuration**: Sets up logging to `file_sorter.log`.
- **Functions**:
  - `log_info(message)`: Logs informational messages.
  - `log_error(message)`: Logs error messages.

### file_types/

- Contains modules defining categories and patterns.
- **Example Modules**:
  - `text_files.py`
  - `image_files.py`
  - `audio_files.py`

### tests/

- **test_main.py**: Tests `load_file_types` function.
- **test_sorter.py**: Tests `sort_files` function.
- **test_file_types.py**: Tests file type pattern definitions.

## Notes

- **Ensure the Script is Outside the Target Directory**: Keep the script's code separate from the directory it's organizing to prevent it from processing its own files.
- **Permissions**: Make sure you have read and write permissions for the target directory.
- **Operating System Compatibility**: The script is designed to work on Windows, macOS, and Linux systems.
- **Avoid Processing Hidden Files**: The script excludes directories like `__pycache__` and files starting with a dot (e.g., `.gitignore`).

## Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the Repository**

2. **Create a Feature Branch**

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Commit Your Changes**

   ```bash
   git commit -am 'Add a new feature'
   ```

4. **Push to the Branch**

   ```bash
   git push origin feature/your-feature-name
   ```

5. **Open a Pull Request**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **Python Documentation**: For extensive documentation on modules and best practices.
- **pytest Documentation**: For guidance on writing unit tests.
- **Community Forums**: For solutions and discussions on Python programming challenges.

## Contact

For any questions or issues, please open an issue on the GitHub repository or contact the maintainer at [s339872@oslomet.no](mailto:s339872@oslomet.no).

---

**Disclaimer**: This README provides a comprehensive guide to setting up, configuring, and using the File Organizer program. Please ensure you have backups of important files before running the script, as it will move files within your directory.
