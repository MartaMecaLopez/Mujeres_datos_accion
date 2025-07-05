import pandas as pd
import numpy as np


def puntos_por_barra(df):
    nuevas_columnas = {}
    for col in df.columns:
        nuevas_columnas[col] = col.lower().replace(".", "_")

    df.rename(columns = nuevas_columnas, inplace = True)
    df.columns



def minusculas(df):
    nuevas_columnas = {}
    for col in df.columns:
        nuevas_columnas[col] = col.lower()

    df.rename(columns = nuevas_columnas, inplace = True)
    df.columns    

def cambio_tipo(df, col, tipo):
    df[col] = df[col].astype(tipo)
    print(df.info()) 


def tipo_fecha(df, col):
    df[col] = pd.to_datetime(df[col])
    print(df.info())     

    

def limpieza_tallas(df, col):
    df[col] = df[col].str.lower()
    df[col] = df[col].str.replace('size', "")
    df[col] = df[col].str.replace('pcs', "")
    df[col] = df[col].str.replace('pc', "")
    df[col] = df[col].str.replace('cm', "")
    df[col] = df[col].replace(r'^\s*\d+\s*$', np.nan, regex=True) #si hay un número solo lo convertimos en un nulo
    df[col] = df[col].str.replace(r"\(.*?\)", "", regex=True) #borra todo lo que haya dentro de un paréntesis (incluidos)
    df[col] = df[col].str.replace(r'^.*?-', '', regex=True) #borra todo lo que haya delante de un guión, incluido el mismo
    df[col] = df[col].str.replace('.', "")
    df[col] = df[col].str.replace(' ', "")
    df[col] = df[col].replace(r'^.{7,}$', np.nan, regex=True) #marca como nulos todos los campos con 7 o más cefras (numeros o letras)


def cambiar_numerico(df, col):
    cambiar_numerico = [col]
    for columna in cambiar_numerico:
        df[columna] = pd.to_numeric(df[columna], errors='coerce')
    df.info()  


def cambiar_a_entero(df, col):
    df[col] = pd.to_numeric(df[col], errors='coerce')  # Convierte a numérico (float si hay decimales o NaN)
    df[col] = df[col].astype('Int64')  #convierte a entero permitiendo NaNs (Int64 de pandas, no int normal)
    df.info()

   

def cambiar_objeto(df, col):
    df[col] = df[col].astype(str)
    df.info()


# Cambiar nulo por nueva categoría
def objeto_categoria (df, col):
    df[col] = df[col].fillna('Unknown')
# Cambiar nulo por moda
def objeto_moda(df, col):
    moda= df[col].mode()[0] 
    df[col] = df[col].fillna(moda)
    return moda
# Cambiar nulo por mediana
def mediana_num(df, col):
    mediana= df[col].median()
    df[col] = df[col].fillna(mediana)   
    nulos= df.isnull().sum().sort_values(ascending= False)
    return nulos



def si_no(df, col):
    df[col] = df[col].replace({'1': 'si', '0': 'no'})
    return df



def limpieza_solo_numeros(df, col):
    df[col] = df[col].str.lower()
    df[col] = df[col].str.replace(r"\(.*?\)", "", regex=True)  # borra todo lo que haya dentro de paréntesis (incluidos)
    df[col] = df[col].str.replace(r'[a-zA-Z]', '', regex=True)   # borra todas las letras
    df[col] = df[col].str.replace(r'^.*?\.', '', regex=True) #borra todo lo que haya delante de un punto
    df[col] = df[col].str.replace(r'\\', '', regex=True) #borra las barras invertidas "\"
    df[col] = df[col].str.replace('/', '', regex=True) #borra las barras invertidas "/"
    df[col] = df[col].str.replace('.', "")
    df[col] = df[col].str.replace(' ', "")

    return df




def meses(df, col):
    diccionario_mapa = {1: "enero", 2: "febrero", 3: "marzo",  4: "abril",  5: "mayo",  6: "junio",  7: "julio",  8: "agosto",  9: "septiembre",  10: "octubre",  11: "noviembre",  12: "diciembre",} 
    for item in col:
        df[item] = df[item].map(diccionario_mapa)
 