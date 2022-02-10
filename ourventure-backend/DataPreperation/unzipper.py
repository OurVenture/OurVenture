import os
import zipfile

if __name__ == "__main__":
    print("Unzipping all files in DataCollections directory")
    zip_path = "ourventure-backend/DataPreperation/DataCollections"
    if os.path.exists(zip_path):
        print("Path exists!")
        for file in os.listdir(zip_path):
            if file.endswith(".zip"):
                print(file)
                with zipfile.ZipFile(f"{zip_path}/{file}", "r") as zip:
                    zip.extractall(zip_path)
    else:
        print("Project directory structure does not conform to the main branch ... please contact a team member for more information")
        print("Prefferd directory structure: ourventure/ourventure-backend/DataPreperation/DataCollections")
