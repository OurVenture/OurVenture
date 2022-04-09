from fastapi import FastAPI
from Generation import Person


#The __init__ function acts as an interface for the API 
#All non interface files should be imported and presented via __init__
#Flask does not need to create pages, only API end points to interact with the VUE frontend
app = FastAPI()

@app.get("/region")
def initialise_region():
    print("Creating region")
    #To create a region, x many classes should be declared
    #A region needs an economy, a few organisations / guilds, an assortment of NPC's, 
    # Quests and Town details like stores, culture and ruler classes
    return "Got Region"


@app.get("/person")
def get_person():
    print("")
    return "Got Person"


@app.get("/")
def hello_world():
    return "Hello, World!"


if __name__ == "__main__":
    app.run()