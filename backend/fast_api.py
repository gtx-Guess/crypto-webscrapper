from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from web_scraper import get_cyrpto_data

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/get_crypto")
def query_crypto_data(response: Response):
    resp = get_cyrpto_data()
    if resp:
        return resp
    else:
        response.status_code = 500
        return "Didnt get the crypto data"

# python3 -m uvicorn fast_api:app --reload