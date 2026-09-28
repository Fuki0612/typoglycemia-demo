from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Typoglycemia Demo API")


class ShuffleRequest(BaseModel):
    text: str
    strength: float = 1.0


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/shuffle")
def shuffle(request: ShuffleRequest):
    # TODO: 単語内部の文字シャッフルロジックを実装する
    raise NotImplementedError
