import os

from starlette.datastructures import CommaSeparatedStrings

API_V1_STR = "/api"

PROJECT_NAME = os.getenv("PROJECT_NAME", "FastApi Sample")
ALLOWED_HOSTS = CommaSeparatedStrings(os.getenv("ALLOWED_HOSTS", ""))
