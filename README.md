### Hexlet tests and linter status:
[![Actions Status](https://github.com/sgmdlt/python-project-lvl3/workflows/hexlet-check/badge.svg)](https://github.com/sgmdlt/python-project-lvl3/actions)
[![Python CI](https://github.com/sgmdlt/python-project-lvl3/actions/workflows/python-ci.yml/badge.svg)](https://github.com/sgmdlt/python-project-lvl3/actions/workflows/python-ci.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/d9a8d018be5322f613df/maintainability)](https://codeclimate.com/github/sgmdlt/python-project-lvl3/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/d9a8d018be5322f613df/test_coverage)](https://codeclimate.com/github/sgmdlt/python-project-lvl3/test_coverage)

# page-loader
### **page-loader** is a simple cli-utility to download web pages
---
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install **page-loader**.

```bash
pip install --user git+https://github.com/sgmdlt/python-project-lvl3.git
```

## Usage

### As library function

```python
from page_loader import download

file_path = download('https://ru.hexlet.io/courses', '/var/tmp')
print(file_path)  # => '/var/tmp/ru-hexlet-io-courses.html'
```

### As CLI util

```bash
$ page-loader --help
usage: page-loader [options] <url>

Download web-pages and saves localy

positional arguments:
  url                   url to download

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        output dir (default: [current directory])
  -l {DEBUG,WARNING}, --log-level {DEBUG,WARNING}
                        sets log level (default: WARNING)


$ page-loader --output /var/tmp https://ru.hexlet.io/courses
/var/tmp/ru-hexlet-io-courses.html
```

## Usage example

[![asciicast](https://asciinema.org/a/OQojp3sUpmiDATbTwMCJKnqaC.svg)](https://asciinema.org/a/OQojp3sUpmiDATbTwMCJKnqaC)
