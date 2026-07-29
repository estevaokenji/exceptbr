import sys
from rich.panel import Panel
from rich import print
from .traceback import Traceback

def excepthook(tipo, valor, tb):
    try:
        err = Traceback(valor)
        print(Panel(f"[reset]{err.pasta}\\{err.nome_arquivo}:{err.linha}\n{err.codigo}[/]", title=f"{err.nome}: [reset]{err.texto}[/]", style="bold bright_red", width=100))
    except Exception:
        import traceback
        traceback.print_exception(tipo, valor, tb)

def install():
    sys.excepthook = excepthook