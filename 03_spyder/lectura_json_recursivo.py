# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 08:02:38 2018

@author: Andres
"""

import json
import pandas as pd
import os

directorio_a_leer = 'C://Users//Andres//Desktop//artworks'

ejemplo_json = directorio_a_leer + '//a//000//a00001-1035.json'

llaves_a_usarse = ['id','all_artists','title','medium','dateText',
                   'acquisitionYear','height','width','units']

def obtener_registros_de_archivos_json(path_archivo,llaves):
    with open(path_archivo) as texto_json:
        contenido_json = json.load(texto_json)
    lista_valores_leidos = []
    for llave in llaves:
        lista_valores_leidos.append(contenido_json[llave]) ## 38
    return tuple(lista_valores_leidos)

#registro_json = obtener_registros_de_archivos_json(ejemplo_json,llaves_a_usarse)
#registro_json_dt = pd.DataFrame([registro_json])

def leer_directorios_json_en_carpetas(directorio,llaves):
    trabajos_arte_encontrados = []
    for path_raiz,lista_directorios,archivos in os.walk(directorio):
        for archivo in archivos:
            if archivo.endswith('json'):
                directorio_archivo = os.path.join(path_raiz,archivo)
                registro_encontrado=obtener_registros_de_archivos_json(directorio_archivo,llaves)
                trabajos_arte_encontrados.append(registro_encontrado)
                break
    
    df = pd.DataFrame.from_records(trabajos_arte_encontrados,columns=llaves,index='id')
    return df

df = leer_directorios_json_en_carpetas(directorio_a_leer,llaves_a_usarse)
