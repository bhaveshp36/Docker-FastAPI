from fastapi import FastAPI

app = FastAPI()

inventory = {
    1:{
        "name":"Milk",
        "price":70,
        "brand":"AMUL"
    },
    2:{
        "name":"Bread",
        "price":50,
        "brand":"Britania"
    }
    }

@app.get("/")
def home():
    return {"Data":"testing"}

@app.get("/about")
def about():
    return {"Data":"about"}

@app.get("/get-item/{item_id}")
def get_item(item_id:int):
    return inventory[item_id]