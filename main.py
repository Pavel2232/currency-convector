from fastapi import FastAPI

from utils import convert_currency_fixerapi_free

app = FastAPI(
    title='currency convector'
)

@app.get("/api/rates/")
async def rates(origin: str, to: str, value: int | float):
    currency = convert_currency_fixerapi_free(origin.upper(), to.upper(), value)
    return {"Convert currency": f'{currency}-{to}'}

