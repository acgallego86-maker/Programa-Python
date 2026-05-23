# Andres Felipe Gallego Correa
#Grupo: 213022_124
#Programa: Ingenieria Electronica
# Código fuente: Autoria Propia.

# 1. Matriz con 5 filas que contiene informacion de los clientes en cada sesion

Datos_sesion_clientes=[
    ["ID2026-01",240,10], #la duración esta dada en segundos que es la segunda columna  
    ["ID2026-02",50,2],
    ["ID2026-03",100,5],
    ["ID2026-04",300,15],
    ["ID2026-05",75,3]    
]

def nivel_compromiso(duracion, clics):
    """ La funcion me va ayudar a clasificar el compromiso de los clientes 
    segun la duracion y los clics que tengan.
    Parametros: duracion y clics
    """
    # logica de Negocio para clasificar el compromiso de cada sesion
    if duracion > 180 and clics > 8:
        return "Alto"
    elif duracion < 60 or clics < 3:
        return "Bajo"
    else:
        return "Medio"
    
# Salida: Generar un informe listando el ID del cliente y su clasificación final.
for sesion in Datos_sesion_clientes:
    ID_cliente = sesion[0]
    duracion = sesion[1]
    clics = sesion[2]
    
    compromiso = nivel_compromiso(duracion, clics)
    
    print(f"Cliente: {ID_cliente}, Compromiso: {compromiso}")
    
    