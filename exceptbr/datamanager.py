import json
from pathlib import Path

class DataManager:
    __ARQUIVO = Path(__file__).parent / "translations.json"

    def __init__(self):
        self._data = self.carregar()

    def carregar(self):
        with open(self.__ARQUIVO, encoding="utf-8") as f:
            return json.load(f)

    def salvar(self):
        with open(self.__ARQUIVO, "w", encoding="utf-8") as f:
            json.dump(self._data, f, ensure_ascii=False, indent=4)

    def adicionar(self, erro, traducao):
        self._data[erro] = traducao
        self.salvar()
        return traducao

    def obter(self, erro):
        return self._data.get(erro,"")