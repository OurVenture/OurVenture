import json
import os
import re


def collect_json_info():
    target_file = "name_collection_output.json"
    # path_name = "c:\Users\jedel\PycharmProjects\OurVenture\ourventure-backend\DataPreperation\DataCollections\name_collection_output.json"
    # print(f"Current directory start is {os.getcwd()}")
    # print(f"Current directory content is {os.listdir(os.getcwd())}")
    files_paths = [os.path.abspath(x) for x in os.listdir(os.getcwd())]
    # print("Getting abspaths", files_paths)
    # print(target_file)
    target_path = [x for x in files_paths if re.search(target_file, x)]
    print("Target path is ", target_path)
    with open(f"{os.getcwd()}/ourventure-backend/DataPreperation/DataCollections/name_collection_output.json", "r", encoding='utf8') as json_data:
        print(json_data)
        return json.load(json_data)

def get_user_preference():
    print("Exporting data to user preference selection")



if "__main__" == __name__:
    print("Starting up name selection")
    print(os.getcwd())
    json_output = collect_json_info()
    # print(json_output)