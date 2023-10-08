import pandas as pd
import re

# Verificar tipo de dtos de los dataframe
def verificar_datos(df):
    # Comprobamos que el dataframe sea valido
    if not isinstance(df, pd.DataFrame):
        raise ValueError("El parámetro df, debe ser un dataframe de pandas")
    
    # Obtenemos un resumen de tipos de datos y valores nulos 
    resume = {"columna": [], "tipo_dato": [], "datos_nulos": [],
              "porcentaje_nulos": [], "porcentaje_no_nulos": []}
    
    for colum in df.columns:
        no_nulos = (df[colum].count()/len(df)) * 100
        # Advertimos si la columna tiene valores nulos
        if df[colum].isnull().sum():
            print(f"Advertencia: la columna {colum}, tiene valores nulos")
            
        resume["columna"].append(colum)
        resume["tipo_dato"].append(df[colum].apply(lambda x: type(x)).unique())
        resume["datos_nulos"].append(df[colum].isnull().sum())
        resume["porcentaje_nulos"].append(round(100-no_nulos, 2))
        resume["porcentaje_no_nulos"].append(round(no_nulos, 2))
        
    salida = pd.DataFrame(resume)
    return salida

# Funcion para mostrar valores nulos por columna
def valores_nulos_columna(df, columna):
    # Obtenemos los valores nulos de la columna
    nulos = df[columna].isnull()
    
    # Creamos un dataframe con los valores nulos
    df_nulos = df[nulos]
    
    # Añadimos el indice 
    df_nulos["index"] = df_nulos.index
    
    return df_nulos

