# %%
# Imports #

import sys
import os
from os.path import expanduser
import argparse
import pandas as pd
import datetime

from config import (
    file_dir,
    parent_dir,
    grandparent_dir,
    great_grandparent_dir,
    data_dir,
    report_dir,
)

from utils.gmail_tools import (
    get_body_dataframe_from_search_string,
)

from utils.display_tools import print_logger, pprint_df, pprint_ls


# %%
# Variables #

today_date = datetime.datetime.now().strftime("%Y-%m-%d")


# %%
# Main #


if __name__ == "__main__":
    search_string = f"from:me to:me after:{today_date}"
    authentication_directory = os.path.join(
        expanduser("~"), "credentials", "personal", "gmail_auth"
    )

    if "ipykernel" in sys.argv[0]:
        print("Running in IPython kernel")
    else:
        parser = argparse.ArgumentParser(description="Export gmail search as csv")
        # search string
        parser.add_argument(
            "-s", "--search-string", type=str, help="String to search gmail for"
        )
        # outfile
        parser.add_argument("-o", "--outfile", type=str, help="File to save output to")
        # authentication_directory
        parser.add_argument(
            "-a",
            "--authentication-directory",
            type=str,
            help="Directory to store authentication files",
        )

        args = parser.parse_args()

        if args.search_string:
            search_string = args.search_string
        else:
            print(f"No search string specified. Using default: {search_string}")

        if args.outfile:
            outfile = args.outfile
        else:
            outfile = os.path.join(report_dir, "email_bodies.csv")
            print(f"No outfile specified. Using default: {outfile}")

        if args.authentication_directory:
            authentication_directory = args.authentication_directory
        else:
            print(
                f"No authentication directory specified. Using default: {authentication_directory}"
            )

    print_logger(f"Searching gmail for: {search_string}")

    df = get_body_dataframe_from_search_string(
        search_string,
        auth_dir=authentication_directory,
    )

    print_logger("Output (first 20 rows):")
    pprint_df(df.head(20))

    print_logger(f"Saving to: {outfile}")
    df.to_csv(outfile, index=False)

    print_logger("Done")

# %%
