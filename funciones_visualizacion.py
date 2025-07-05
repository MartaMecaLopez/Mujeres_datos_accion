import pandas as pd 
import numpy as np
from sqlalchemy import create_engine
import pymysql
pd.set_option('display.max_columns', None)


def ver_unicos(df):
    print('  ')
    print('VISUALIZACIÓN DE ÚNICOS')
    print('  ')
    for col in df.select_dtypes(include='object'):
        print(col)
        print('-----------------------------')
        print(df[col].unique())    


def extract_data(file, nombre_df):
    print(f"Extrayendo datos desde {file}...")
    print('  ')
    nombre_df = pd.read_csv(file)
    print('INFORMACIÓN SOBRE COLUMNAS')
    print('  ')
    print(nombre_df.info())
    print('  ')
    print('--------------------------------------------------')
    print('  ')
    print('VISUALIZACIÓN DE NULOS')
    print('  ')
    print(nombre_df.isnull().sum())
    ver_unicos(nombre_df)

    return nombre_df.head()



def porcentaje_nulos(df):
    nulos = df.isnull().sum()/df.shape[0]*100
    nulos = nulos[nulos > 0]
    nulos.sort_values(ascending=False)
    nulos = nulos.to_frame(name='perc_nulos').reset_index()
    return nulos



def extract_data_df(df):
    print('INFORMACIÓN SOBRE COLUMNAS')
    print('  ')
    print(df.info())
    print('  ')
    print('--------------------------------------------------')
    print('  ')
    print('VISUALIZACIÓN DE NULOS')
    print('  ')
    print(df.isnull().sum())
    ver_unicos(df)

    return df.head()




