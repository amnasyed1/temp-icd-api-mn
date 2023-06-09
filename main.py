from fastapi import FastAPI

import pandas as pd

import uvicorn


df = pd.read_csv('./data/rxdetail2018new.csv')


app = FastAPI()

@app.get('/')
def home():
    return {'this is an API service for MN code details'}

@app.get('/preview')
async def preview():
    top10rows = df.head(10)
    result = top10rows.to_json(orient="records")
    return result

@app.get('/launch_year/{value}')
async def icdcode(value):
    print('value: ', value)
    filtered = df[df['launch_year'] == value]
    if len(filtered) <= 0:
        return 'There is nothing here'
    else:
        return filtered.to_json(orient="records")

@app.get('/dosage_form/{value}/encounter_count/{value2}')
async def icdcode2(value, value2):
    print('value: ', value)
    filtered = df[df['dosage_form'] == value]
    filtered2 = filtered[filtered['encounter_count'] == value2]
    if len(filtered2) <= 0:
        return 'There is nothing here'
    else:
        return filtered2.to_json(orient="records")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
