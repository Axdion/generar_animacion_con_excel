import pandas

def excel_to_list(ruta:str):
    xls = pandas.ExcelFile(ruta)
    hoja = xls.sheet_names[0]

    df = xls.parse(hoja)
    lista = df.values.tolist()

    return (lista[0][0], lista[0][1], [x[0] for x in lista[1:len(lista)]], [x[1] for x in lista[1:len(lista)]])
