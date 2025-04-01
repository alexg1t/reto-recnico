import csv
import sys
def resumir_csv(nombre_archivo='valores_generados.csv'):

    try:
        # Variables de resumen
        creditos = 0
        debitos = 0
        monto_mayor = 0
        id_mayor = 0
        conteo_creditos = 0
        conteo_debitos = 0

        # Leer el archivo CSV
        with open(nombre_archivo, 'r') as archivo:
            # Crear lector de CSV
            lector_csv = csv.DictReader(archivo)
            
            # Iterar por cada fila
            for fila in lector_csv:
                # Convertir monto a float
                monto = float(fila['monto'])
                
                # Contar y sumar por tipo
                if fila['tipo'] == 'credito':
                    creditos += monto
                    conteo_creditos += 1
                else:
                    debitos += monto
                    conteo_debitos += 1
                
                # Encontrar transacción de mayor monto
                if monto > monto_mayor:
                    monto_mayor = monto
                    id_mayor = fila['id']

        # Calcular balance final
        balance_final = creditos - debitos

        # Imprimir el reporte en consola
        print("Reporte de Transacciones")
        print("---------------------------------------------")
        print(f"Balance Final: {balance_final:.2f}")
        print(f"Transacción de Mayor Monto: ID {id_mayor} - {monto_mayor:.2f}")
        print(f"Conteo de Transacciones: Crédito: {conteo_creditos} Débito: {conteo_debitos}")
    
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {nombre_archivo}")
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")


def main():
    # Si hay argumento
    if len(sys.argv) > 1:
        nombre_archivo = sys.argv[1]
        resumir_csv(nombre_archivo)
    else:
        # Usar nombre de archivo por defecto
        resumir_csv()


if __name__ == "__main__":
    main()