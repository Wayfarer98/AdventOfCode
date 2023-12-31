# My advent of code solutions for years to come
-------

## How to get setup
The problem input is different for each problem solver, so you first need to extract you session token to get your specific problem input. Extract your session token by logging in to the [advent of code](https://adventofcode.com/), then go to the first problem text (https://adventofcode.com/2023/day/1/input). Open the developer tools in the network tab, refresh the page, then click on any request. Navigate to the request headers and find a *Cookie* field. Copy the long session id, but don't include the *session=* part.
In the root of the project, create a .env file. Write ```AOC_<year>_SESSION = <you ession token>```

## 2023

This year will be a python3 based solution. To run the solutions, preferably create a venv with `python -m venv aoc` in the 2023 root directory. Install the necessary dependencies with `pip install -r requirements.txt`.
To get the solutions to any day, navigate to the 2023 root directory and run:
```python -m Day<x>.day<x>```
For example, to get the solutions to day 1, run:
```python -m Day1.day1```
