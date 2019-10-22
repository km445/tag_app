# JSON REST API Tag application

## Application specification

1. Estimated computational complexity - O(n)  (linear).
1. Available tags are stored in constants.py
1. Using application virtualenv, run some tests with `python -m unittest tests.get_tags_tests` in a terminal in project root.
1. If applicable, time spent on request processing is sent in "time_taken" response parameter. It does not include network delays.

## Application demo instructions

1. Clone the project `https://github.com/km445/tag_app.git`
1. Install application virtualenv(python 3 is required)/library which is specified in requirements.txt `pip install -r requirements.txt`. 
1. Using application virtualenv, run `python runserver.py` in a terminal in project root.
1. Send a POST request that looks something like this: `curl -H "Content-Type: application/json" -XPOST "localhost:5889/get_tags" -d '{"ad_text":"New Toyota  Corolla LE  2007"}'`
