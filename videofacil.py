import os
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.post("/analyze")
def analyze():
    return {
        "status": "sucesso",
        "diagnostico": "Sistema verificado com sucesso em ambiente cloud.",
        "peca_nome": "Módulo FastAPI em Produção",
        "link_afiliado": "https://exemplo.com/sucesso-cloud"
    }

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)