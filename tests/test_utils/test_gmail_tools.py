# %%
# Imports #

import os
from os.path import expanduser

import config_test_utils  # noqa F401
from src.utils.display_tools import print_logger
from src.utils.gmail_tools import get_gmail_service

# %%
# Tests #


def test_get_gmail_service():
    gmail_service = get_gmail_service(
        os.path.join(expanduser("~"), "credentials", "personal", "gmail_auth")
    )
    assert gmail_service is not None
    print_logger(f"gmail_service: {gmail_service}")


# %%
# Main #

if __name__ == "__main__":
    test_get_gmail_service()


# %%
