import sys
from rich.panel import Panel
from rich import print
from .traceback import Traceback

def excepthook(tipo, valor, tb):
    err = Traceback(valor)
    print(Panel(f"[reset]{err.pasta}\\{err.nome_arquivo}:{err.linha}\n{err.codigo}[/]", title=f"{err.nome}: [reset]{err.texto}[/]", style="bold bright_red", width=100))

def install():
    sys.excepthook = excepthook