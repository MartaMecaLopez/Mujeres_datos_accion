# Importación de librerías

# Tratamiento de datos
import pandas as pd 
from sqlalchemy import create_engine  # sqlalchemy es una librería que permite conectarse y trabajar con bases de datos de manera más abstracta y flexible. 'create_engine' permite crear una conexión a bases de datos SQL de diferentes tipos, como MySQL, PostgreSQL, SQLite, etc.
import pymysql
import numpy as np

# Visualización
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option('display.max_columns', None) # para poder visualizar todas las columnas de los DataFrames

# Evaluar linealidad de las relaciones entre las variables
import scipy.stats as stats
from scipy.stats import shapiro, poisson, chisquare, expon, kstest

# Gestión de los warnings
import warnings
warnings.filterwarnings("ignore")

#importación de librerías que propias
import funciones_limpieza as limpieza
import funciones_visualizacion as visualizacion


df_movies = pd.read_csv('movies.csv')
df_oscars = pd.read_csv('oscar.csv')

#VISUALIZACIÓN

visualizacion.extract_data('movies.csv', df_movies)
visualizacion.ver_unicos(df_movies)


# Gestión de nulos

df_movies.isnull().sum()
df_movies['revenue'].value_counts()
df_oscars.isnull().sum()

def conteo_valores(df, nombre='DataFrame'):
    print(f'\n📊 Contando valores únicos en "{nombre}"\n')
    for col in df.columns:
        print(f'🟡 Columna: {col}')
        num_unicos = df[col].nunique(dropna=False)
        print(f"   → {num_unicos} valores únicos\n")
        print("   Valores y sus frecuencias:")
        print(df[col].value_counts(dropna=False))
        print("-" * 40)

conteo_valores(df_movies, nombre='DataFrame_Películas')


# Limpieza del dataset

df_movies.drop_duplicates(subset='imdbid', keep='first', inplace=True)

columnas_eliminadas = ['Unnamed: 0', 'dubious', 'tmdbId', 'popularity', 'production_companies', 'cast', 'crew', 'budget', 'cast_gender', 'crew_gender', 'revenue']

for colum in columnas_eliminadas:
    df_movies.drop(colum, axis = 1, inplace = True)

limpieza.minusculas(df_movies)

columnas_redondeo = ['cast_female_representation', 'crew_female_representation']

for col_red in columnas_redondeo:
    df_movies[col_red] = df_movies[col_red].round()

limpieza.cambiar_a_entero(df_movies, 'vote_count')

visualizacion.extract_data_df(df_movies)

# Separamos los elementos de la lista para crear un nuevo dataframe exclusivamente con esta información

df_movies['genres'] = df_movies['genres'].str.strip("[]").str.replace("'", "").str.split(", ")
df_movies['production_countries'] = df_movies['production_countries'].str.strip("[]").str.replace("'", "").str.split(", ")

# Creamos los dataframes adicionales

df_genres = df_movies.explode('genres')
df_countries = df_movies.explode('production_countries')

print(df_genres.columns)
print(df_countries.columns)

# A continuación, elimino las columnas que no son relevantes para estos nuevos dataframes

columnas_eliminadas_genres = ['year', 'bt_score', 'production_countries', 'release_date', 'vote_average', 'vote_count', 'cast_female_representation', 'crew_female_representation']
columnas_eliminadas_countries = ['year', 'bt_score', 'genres', 'release_date', 'vote_average', 'vote_count', 'cast_female_representation', 'crew_female_representation']

for colum in columnas_eliminadas_genres:
    df_genres.drop(colum, axis = 1, inplace = True)

for colum in columnas_eliminadas_countries:
    df_countries.drop(colum, axis = 1, inplace = True)

df_movies.to_csv('movies_clean.csv', index=False)
df_genres.to_csv('genres_clean.csv', index=False) 
df_countries.to_csv('countries_clean.csv', index=False) 
df_oscars.to_csv('oscars_clean.csv', index=False) 


