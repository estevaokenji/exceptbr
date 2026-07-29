import os, json

class DataManager:
    arquivo = os.path.join(os.path.dirname(__file__),"translations.json")

    def __init__(self):
        self.data = self.carregar()

    def carregar(self):
        with open(self.arquivo, encoding="utf-8") as f:
            return json.load(f)

    def salvar(self):
        with open(self.arquivo, "w", encoding="utf-8") as f:
            json.dump(self.data, f, ensure_ascii=False, indent=4)

    def adicionar(self, erro, traducao):
        self.data[erro] = traducao
        self.salvar()
        return traducao

    def obter(self, erro):
        return self.data.get(erro,"")