#!.venv/bin/python3
"""
Copyright (c) 2023 - present amc.com
"""
from dotenv import load_dotenv, find_dotenv
from amc import create_app

load_dotenv(find_dotenv())

app = create_app()

if __name__ == "__main__":
    app.run()
