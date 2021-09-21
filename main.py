from lector_excel import excel_to_list
from tkinter import filedialog
from generador_animacion import generar_animacion

from matplotlib.pyplot import plot, show, xlabel, ylabel

def obtener_ruta_excel():
    ruta = filedialog.askopenfilename()
    return ruta
if __name__ == "__main__":
    lista = excel_to_list(obtener_ruta_excel())
    generar_animacion(lista[0], lista[1], lista[2], lista[3])
