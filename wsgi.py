#!.venv/bin/python3
"""
Copyright (c) 2023 - present amc.com
"""
import os
from dotenv import load_dotenv, find_dotenv
from amc import create_app

load_dotenv(find_dotenv())

app = create_app()


if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=os.getenv('PORT', '5000')
    )
