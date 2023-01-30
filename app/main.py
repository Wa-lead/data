from fastapi import FastAPI, File, UploadFile
import pandas as pd

app = FastAPI()

@app.get("/dataframe")
async def get_dataframe():
    df = pd.read_json("data.json")
    return df.to_json(orient='records')

