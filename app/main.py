from fastapi import FastAPI, File, UploadFile
import mysql.connector



import pandas as pd

app = FastAPI()

@app.get("/dataframe")
async def get_dataframe():
    cnx = mysql.connector.connect(
    host="rm-l4vtsmuu203976dh4qo.mysql.me-central-1.rds.aliyuncs.com",
    user="admin_account",
    password="Admin@2023",
    database="mysql"
    )

    cursor = cnx.cursor()

    query = """SELECT 
            name,
            id,
            degree,
            field_of_study,
            university,
            graduation_year,
            courses
    FROM new_schema.ayman
    """

    cursor.execute(query)

    result = cursor.fetchall()

    cnx.close()
    df = pd.read_json("data.json")
    return df.to_json(orient='records')
