# Gestor de Transacciones Financieras

Este proyecto contiene un conjunto de herramientas para generar y analizar datos de transacciones en formato CSV.

## Descripción

El proyecto consta de dos scripts principales:
1. **Generador de CSV**: Crea archivos CSV con datos de transacciones aleatorias de tipo crédito y débito.
2. **Analizador de Transacciones**: Procesa los archivos CSV que se le pasen y muestra un resumen de las transacciones.

Los scripts están escritos en Python y utilizan solo módulos de la biblioteca estándar, sin dependencias externas.

## Características

### Generador de CSV
- Genera registros con IDs secuenciales
- Asigna tipos de transacción (crédito o débito) aleatoriamente
- Crea montos aleatorios entre 0 y 1000 con formato de dos decimales (.00)
- Configurable para generar diferente cantidad de registros

### Analizador de Transacciones
- Calcula el balance final (crédito - débito)
- Identifica la transacción de mayor monto
- Cuenta el número de transacciones por tipo
- Se puede ejecutar desde la línea de comandos


## Requisitos

- Python 3.6 o superior

## Instalación

1. Clona este repositorio:
```bash
git clone https://github.com/alexg1t/reto-tecnico.git

```

2. Otorga permisos de ejecución a los scripts:
```bash
chmod +x generador_csv.py
chmod +x resumen_csv.py
```

## Uso

### Generador de CSV

```bash
python gen.py
```

Si es necesario usarlo, este programa generará el número de registros indicados en un archivo llamado "valores_generados.csv".

```bash
C:\Users\aleg1t\reto-tecnico>python gen.py
Ingrese el numero de registros a generar : 15
Archivo generado con 15 registros.
```


### Procesador de Transacciones

```bash
# Especificando el nombre del archivo
python res.py mi_archivo.csv
```


## Ejemplo de Salida

El programa mostrará un resumen como el siguiente:

```
Reporte de Transacciones
---------------------------------------------
Balance Final: 325.00
Transacción de Mayor Monto: ID 3 - 200.00
Conteo de Transacciones: Crédito: 3 Débito: 2
```

## Estructura de Archivos

```
reto-tecnico/
├── gen.py                # Script para generar archivo CSV
├── res.py                # Script para analizar y mostrar resumen
├── valores_generados.csv # Archivo csv generado (ejemplo)
└── README.md             # Este archivo
```

## Formatos

### Formato del CSV Generado

El CSV generado tendrá la siguiente estructura:

```
id,tipo,monto
1,credito,100.00
2,debito,50.00
3,credito,200.00
```

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir:
1. Haz un fork del repositorio
2. Crea una rama para tu característica (`git checkout -b feature/nueva-caracteristica`)
3. Haz commit de tus cambios (`git commit -m 'Añade nueva característica'`)
4. Envía un push a la rama (`git push origin feature/nueva-caracteristica`)
5. Abre un Pull Request

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.