
from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/helloworld")
def hello_world():
 
 return {"Welcome to this app... Sade C. Johnson created this simple starter app. Stay tuned for something a little bit more complex!"}