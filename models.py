from pydantic import BaseModel

class FormatoResposta(BaseModel):
        nome_musica: str
        artista: str
        featuring: str | None