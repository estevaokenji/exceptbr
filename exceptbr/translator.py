from .datamanager import DataManager
from deep_translator import GoogleTranslator

class Translator(str):
    def __new__(cls, texto: str):
        manager = DataManager()
        if texto not in manager.data:
            manager.adicionar(GoogleTranslator("en", "pt").translate(texto))
        return manager.obter(texto)