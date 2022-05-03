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
    # print("Target path is ", target_path)
    with open(f"{os.getcwd()}/ourventure-backend/DataPreperation/DataCollections/name_collection_output.json", "r", encoding='utf8') as json_data:
        # print(json_data)
        return json.load(json_data)

def get_user_preference(json_output):
    print("Exporting data to user preference selection")
    #print(json_output.keys())
    basic_option = ["nation", "cultural"]
    print("Do you wish to search by nation or by cultural region?")
    
    do_enum(basic_option)
    search_value = int(input("Number: "))
    match search_value:
        case 1:
            print("Searching by national origin")
            selected_value = get_values(argument="origin", values=json_output)
        case 2:
            print("Searching by cultural origin")
            selected_value = get_values(argument="region", values=json_output)
    
    for i in json_output.keys():
        print(i)

def get_values(argument, values):
    print("Select values")
    for i in values:
        print("Oh boi!")
        print(i)
    #do_enum()

def do_enum(argument_list):
    for number, argument in enumerate(argument_list, start=1):
        print(number, " ", argument)


if "__main__" == __name__:
    print("Starting up name selection")
    print(os.getcwd())
    json_output = collect_json_info()
    # print(json_output)
    print(len(json_output), type(json_output))
    get_user_preference(json_output)
