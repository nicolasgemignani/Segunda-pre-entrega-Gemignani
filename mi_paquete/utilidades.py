import json

def guardarArchivo(BD, archivo):
    """
    Guarda la información de los clientes en un archivo .json.
    
    :param: BD (dict) Diccionario que contiene los clientes.
    :param: archivo (str) Nombre del archivo en el que se guardará la información.
    """
    try:
        with open(archivo, 'w') as file:
            # Convertir el diccionario BD a formato JSON y guardarlo en el archivo
            json.dump(BD, file, indent=4)
        print(f'Información guardada en {archivo}.')
    except IOError as e:
        print(f'Error al guardar la información en {archivo}: {e}')