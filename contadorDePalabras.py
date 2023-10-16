NOMBRE_ARCHIVO = "chat.txt"
EOF = ""
PALABRAS = ["Te amo","te amo", "t amo", "teamo", "ily", "i l y", "love u", "lov u", "luv u", "Luv u", "Te adoro", "te adoro", "te quiero", "Te quiero"]

def procesar_linea(linea, diccionario_contador):
    for palabra in PALABRAS:
        if palabra in linea:
            diccionario_contador[palabra] += 1
    return diccionario_contador

def inicializarDiccionario(diccionario):
    for palabra in PALABRAS:
        diccionario[palabra] = 0
    return diccionario

def print_diccionario(diccionario):
    cantidadTotal = 0
    for elemento in diccionario:
        cantidadTotal += diccionario[elemento]
        print(f"{elemento} - {diccionario[elemento]} veces.")
    print(f"Cantidad de veces total que nos dijimos que nos amamos: {cantidadTotal}")

def main():
    cantidadLineasContadas = 1
    contador = dict()
    contador = inicializarDiccionario(contador)
    archivo = open(NOMBRE_ARCHIVO, "r", errors='ignore')
    linea = archivo.readline()
    while(linea != EOF):
        cantidadLineasContadas += 1
        contador = procesar_linea(linea, contador)
        linea = archivo.readline()
    print_diccionario(contador)
    print(f"cantidad de lineas: {cantidadLineasContadas}")
    archivo.close()
    
main()