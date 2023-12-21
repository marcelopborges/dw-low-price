from fastapi import FastAPI

app = FastAPI()
fake = Faker()

@app.get("/gerar_compra")
async def gerar_compra():
    return {
        "client": "Nome do cliente",
        "credicard": "Tipo do cartão",
        "ean": "Código de barra do produto",
        "price": "Preço do produto",
        "store": 11,
        "datetime": "Data da compra",
        "clientPosition": "Posição do cliente"
    }
