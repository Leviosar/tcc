# RISC-V Binary Steganography

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# Installing

This project uses `poetry` as dependency manager and the recommended way to install is cloning it's source and installing all the dependencies through `poetry`.

```
# Clone repository 
git clone https://github.com/leviosar/tcc

# Navigate to the src directory
cd src

# Install all dependencies
poetry install

# Enter into the virtual env created by poetry
poetry run shell

# Call steganossaurus like a python module
python -m steganossaurus --help
```

# Encoding