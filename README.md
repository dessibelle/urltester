# URL tester

Tests accessibility of a list of URLs provided in a file as input to the `urltest.py` script.

## Prerequisites

Requires Python 3 and virtualenv.

## Installation

1. `mkdir venv`
1. `virtualenv --python python3 venv`
1. `source venv/bin/activate`
1. `pip install -r requirements.txt`

## Usage

```
python urltest.py urls.txt > urls.csv
```
