import os
from types import TracebackType
from rich.panel import Panel
from .translator import Translator

class Traceback:
    def __init__(self, exception: Exception):
        self._nome = type(exception).__name__
        self._texto = Translator(str(exception)).strip().capitalize()
        tb = self.traceback(exception)
        arquivo = tb.tb_frame.f_code.co_filename
        self._linha = tb.tb_lineno
        self._pasta = os.path.dirname(arquivo)
        self._nome_arquivo = os.path.basename(arquivo)
        self._codigo = self.code(arquivo)
        
    def traceback(self, exception: Exception) -> TracebackType:
        tb = exception.__traceback__
        while tb.tb_next:
            tb = tb.tb_next
        return tb

    def code(self, arquivo: str) -> str:
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

    def panel(self) -> Panel:
        return Panel(f"[reset]{self._pasta}\\{self._nome_arquivo}:{self._linha}\n{self._codigo}[/]", title=f"{self._nome}: [reset]{self._texto}[/]", style="bold bright_red", width=100)