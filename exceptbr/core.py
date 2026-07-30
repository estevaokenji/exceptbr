import sys
from rich import print
from .traceback import Traceback

def excepthook(tipo, valor, tb):
    try:
        print(Traceback(valor).panel())
    except Exception:
        import traceback
        traceback.print_exception(tipo, valor, tb)

def install():
    sys.excepthook = excepthook