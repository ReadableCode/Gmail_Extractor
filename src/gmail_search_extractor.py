# %%
# Imports #

import os
from os.path import expanduser
import pandas as pd

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

search_string = "Maggie@romancetravelgroup.com"

df = get_body_dataframe_from_search_string(
    search_string,
    auth_dir=os.path.join(expanduser("~"), "credentials", "personal", "gmail_auth"),
)

pprint_df(df)

# save to csv
df.to_csv(os.path.join(report_dir, "email_bodies.csv"), index=False)

# %%
