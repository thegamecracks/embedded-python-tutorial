# embedded-python-tutorial

This is a tutorial on how to manually create a portable Python application
on Windows without bundling tools like [PyInstaller].

## Prerequisites

- Python installed on your system
- A "Windows embeddable package" of the same version from [python.org](https://www.python.org/downloads/)

## Summary

The idea is to install the project's dependencies into the same directory where the embedded
Python executable is contained, then run the project's source code through a native executable.
To handle both the dependencies and the generation of the executable, the actual source code
is organized as a [package](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
using [setuptools](https://setuptools.pypa.io/en/latest/userguide/index.html) to formally declare
dependencies and a console script that can be used to start the application.

## Setup

1. Unpack the embeddable archive's contents into the project root
2. Install the source code and dependencies with `py -m pip install --prefix . ./source_code`
3. Run `py fix_scripts.py` to help the console scripts find python.exe and its dependencies
4. Start the application with `Scripts\my_app.exe`

Once done, the project directory can be copied elsewhere (including another drive) for usage.

## Limitations

`fix_scripts.py` replaces absolute paths to your system installation with relative paths,
requiring the user to execute the script from the terminal with the project root as the
current working directory.

## Recommendations

Coincidentally this project uses the same techniques as [PyDeploy](https://github.com/syegulalp/pydeploy/),
a purpose-built tool that takes advantage of embedded Python distributions.

[PyInstaller]: https://pyinstaller.org/en/stable/
