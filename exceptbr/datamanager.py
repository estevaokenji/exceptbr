import json
from pathlib import Path

class DataManager:
    ARQUIVO = Path(__file__).parent / "translations.json"

    def __init__(self):
        self.data = self.carregar()

    def carregar(self):
        with open(self.ARQUIVO, encoding="utf-8") as f:
            return json.load(f)

    def salvar(self):
        with open(self.ARQUIVO, "w", encoding="utf-8") as f:
            json.dump(self.data, f, ensure_ascii=False, indent=4)

    def adicionar(self, erro, traducao):
        self.data[erro] = traducao
        self.salvar()
        return traducao

    def obter(self, erro):
        return self.data.get(erro,"")