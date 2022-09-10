#!/usr/bin/env python
__author__ = "Jim Cassidy"
__copyright__ = "Copyright 2020, SpiderPig Project"
__credits__ = ["Jim Cassidy"]
__license__ = "???"
__version__ = "0.1.0"
__maintainer__ = "Jim Cassidy, "
__email__ = "jim@ion8.net"
__status__ = "Dev"

import typer
from os import path
import os
from google.cloud import storage
# from google.api_core import exceptions
from dotenv import load_dotenv
# from cli_commands import init
# from cli_commands import integration
# from cli_commands import generate
# from cli_commands import upload

load_dotenv("./config/.env")

BUCKET_NAME = os.getenv("BUCKET_NAME")
GOOGLE_APPLICATION_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
CLIENT_NAME = os.getenv("CLIENT_NAME")
map_directory = "integrations"
config_directory ="config"

import typer


def main(name: str):
    print(f"Hello {name}")


if __name__ == "__main__":
    typer.run(main)