import csv
import random

def gen_csv(num_reg):

    # Tipos de transaccion disponible
    tipos = ['credito', 'debito']
    
    # Abrir el archivo
    with open('valores_generados.csv', 'w', newline='', encoding='utf-8') as archivo_csv:
        escritor = csv.writer(archivo_csv)
        # Escribir encabezados o coulumnas
        escritor.writerow(['id', 'tipo', 'monto'])
        # Generar registros
        for id_unico in range(1, num_reg + 1):
            # Seleccionar tipo de manera aleatoria 
            tipo = random.choice(tipos)
            
            # Generar un entero aleatorio entre 0 y 1000
            monto = random.randint(0, 1000)
            
            # Escribir el registro con formato de 2 decimales
            escritor.writerow([id_unico, tipo, f'{monto}.00'])
    
    print(f"Archivo generado con {num_reg} registros.")

# Preguntar por numero de registros a generar
num=int(input('Ingrese el numero de registros a generar : '))
# Ejecutar la función para generar 15 registros
gen_csv(num)

