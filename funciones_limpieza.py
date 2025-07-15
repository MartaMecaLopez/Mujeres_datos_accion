import pandas as pd
import numpy as np




def minusculas(df):
    nuevas_columnas = {}
    for col in df.columns:
        nuevas_columnas[col] = col.lower()

    df.rename(columns = nuevas_columnas, inplace = True)
    df.columns    

def cambiar_a_entero(df, col):
    df[col] = pd.to_numeric(df[col], errors='coerce')  # Convierte a numérico (float si hay decimales o NaN)
    df[col] = df[col].astype('Int64')  #convierte a entero permitiendo NaNs (Int64 de pandas, no int normal)
    df.info()
 