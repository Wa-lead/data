from fastapi import FastAPI, File, UploadFile
import mysql.connector


columns = ['name', 'id', 'degree', 'field_of_study', 'university', 'graduation_year', 'courses',
           'health_history', 'intersts', 'car', 'house', 'job', 'city', 'country', 'date_of_birth']


app = FastAPI()


@app.get("/data")
async def return_data(id):
        cnx = mysql.connector.connect(
                host="rm-l4vtsmuu203976dh4qo.mysql.me-central-1.rds.aliyuncs.com",
                user="admin_account",
                password="Admin@2023",
                database="mysql"
        )

        cursor = cnx.cursor()
        print()
        query = f"SELECT * FROM new_schema.data2 WHERE id = \"{id}\""
        cursor.execute(query)
        result = cursor.fetchall()
        cnx.close()
        return dict(zip(columns, result[0]))


