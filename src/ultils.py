import os
import sys

def resource_path(relative_path):
    """ Obtiene la ruta absoluta al recurso, funciona tanto en desarrollo como en el ejecutable """
    try:
        # PyInstaller crea una carpeta temporal y almacena la ruta en _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)