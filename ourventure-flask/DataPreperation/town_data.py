import pandas as pd
import os
import re
import traceback
from zipfile import ZipFile


def unzip_cities():
    # Checks if text/csv file exists in data collections (ignored by git)
    if not os.path.exists("ourventure-flask/DataPreperation/DataCollections/cities5000.txt"):
        # Checks that the ZIP file exists (not ignored by git)
        if os.path.exists("ourventure-flask/DataPreperation/cities5000.zip"):
            # print("Extracting zip file")
            try: 
                with ZipFile("ourventure-flask/DataPreperation/cities5000.zip", "r") as zp:
                    zp.extractall(path="ourventure-flask/DataPreperation/DataCollections")
                    print("Extracted files!")
            except Exception as e:
                print(f"An error occured with extracting the cities data {e} {traceback.format_exc()}")
        else:
            # This section could be Automated, but it does not need to be since this process mostly follows the architectural principle of WORM's (WRITE ONCE, READ MANY)
            print("The zip file needs to be downloaded, use the following link : ")
    print()

def process_cities():
    cities_csv = pd.read_csv("ourventure-flask/DataPreperation/DataCollections/cities5000.txt", delimiter="\t")
    print(cities_csv)

if __name__ == "__main__":
    unzip_cities()
    process_cities()