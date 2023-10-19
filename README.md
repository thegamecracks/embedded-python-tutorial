# embedded-python-tutorial

This is a demonstration of manually creating a portable Python application
on Windows without tools like [PyInstaller].

## Prerequisites

- Python installed on your system
- An embedded Python package of the same version on [python.org](https://www.python.org/downloads/)

## Setup

1. Unpack the embedded package's contents into the project root
2. Install the source code and dependencies with `py -m pip install --prefix . ./source_code`
3. Run `py fix_scripts.py` to help the console scripts find python.exe and its dependencies
4. Start the application with `Scripts\my_app.exe`

Once done, the project directory can be copied elsewhere (including another drive) for usage.

## Limitations

`fix_scripts.py` replaces absolute paths to your system installation with relative paths,
requiring the user to execute the script from the terminal with the project root as the
current working directory.

[PyInstaller]: https://pyinstaller.org/en/stable/
