import os
from pathlib import Path

import numpy as np
import requests
from dotenv import load_dotenv


class DataHelper:
    def __init__(self, year: int, day: int, session: str | None = None):
        self.year = year
        self.day = day
        if session is not None:
            self.session = session
        else:
            dotenv_path = Path(".env")
            load_dotenv(dotenv_path=dotenv_path)
            self.session = os.getenv("AOC_2024_SESSION")

    def get_data(self) -> list[str]:
        header = {"Cookie": "session=" + self.session}
        r = requests.get(
            f"https://adventofcode.com/{self.year}/day/{self.day}/input", headers=header
        )
        return r.text.split("\n")
