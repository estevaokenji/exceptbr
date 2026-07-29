import os
from .translator import Translator

class Traceback:
    def __init__(self, exception: Exception):
        self.nome = type(exception).__name__
        self.texto = Translator(str(exception)).strip().capitalize()
        tb, arquivo = self.traceback(exception)
        self.linha = tb.tb_lineno
        self.pasta = os.path.dirname(arquivo)
        self.nome_arquivo = os.path.basename(arquivo)
        self.codigo = self.code(arquivo)
        
    def traceback(self, exception: Exception):
        tb = exception.__traceback__
        while tb.tb_next:
            tb = tb.tb_next
        return tb, tb.tb_frame.f_code.co_filename

    def code(self, arquivo: str):
        with open(arquivo, "r", encoding="utf-8") as f:
            linhas = f.readlines()
        inicio = self.linha - 4
        fim = self.linha + 1
        if fim > len(linhas):
            fim = len(linhas)
            inicio -= 1
        inicio = max(0,inicio)
        codigo = ""
        for i in range(inicio, fim):
            n = f"{(i+1):{len(str(fim))}d}"
            c = linhas[i].rstrip("\n")
            if i + 1 == self.linha:
                e = "[bright_red]❱[/]"
                c = f"[bold bright_red]{c}[/]"
            else:
                e = " "
                n = f"[grey35]{n}[/]"
                c = f"[grey46]{c}[/]"
            codigo += f"\n{e} {n} {c}"
        return codigo