import os
from dotenv import load_dotenv
from pathlib import Path
import requests
import numpy as np


class DataHelper:
    def __init__(self, year: int, day: int, session: str | None = None):
        self.year = year
        self.day = day
        if session is not None:
            self.session = session
        else:
            dotenv_path = Path('.env')
            load_dotenv(dotenv_path=dotenv_path)
            self.session = os.getenv('AOC_2023_SESSION')

    def get_data(self) -> np.ndarray:
        header = {'Cookie': 'session=' + self.session}
        r = requests.get(
            f'https://adventofcode.com/{self.year}/day/{self.day}/input',
            headers=header
        )
        return np.array(r.text.split('\n'))
