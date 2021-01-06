# Manual de Usuario

TytusStorage es una librería escrita en Python 3 que provee un gestor de almacenamiento para un administrador de bases de datos (DBMS).
TytusStorage almacena datos localmente utilizando hasta 7 modos de almacenamiento:

- Árbol AVL
- Árbol B
- Árbol B+
- Tabla Hash (de dispersión)
- ISAM
- Diccionarios
- JSON

TytusStorage está dotado de funciones de enlazamiento de datos, seguridad, graficación, entre otras, para otorgar una gran flexibilidad y comodidad de uso.

## Índice

- [Glosario](#glosario)
- [FAQ](#faq)
- [Uso de la librería](#uso-de-la-librería)
- [Uso del almacenamiento](#uso-del-almacenamiento)
- [Uso del administrador del modo de almacenamiento](#uso-del-administrador-del-modo-de-almacenamiento)
- [Uso del administrador de índices](#uso-del-administrador-de-índices)
- [Uso del administrador de codificación](#uso-del-administrador-de-codificación)
- [Uso del generador de checksum](#uso-del-generador-de-checksum)
- [Uso del administrador de compresión de datos](#uso-del-administrador-de-compresión-de-datos)
- [Uso del administrador de seguridad](#uso-del-administrador-de-seguridad)
- [Uso del generador de diagramas de dependencias](#uso-del-generador-de-diagramas-de-dependencias)
- [Uso del reportador gráfico](#uso-del-reportador-gráfico)


## Glosario

| TERMINO   | DESCRIPCCION   |
| ----- | ----- |
| Archivo CSV | Los archivos CSV son un tipo de documento en formato abierto sencillo para representar datos en forma de tabla, en las que las columnas se separan por comas y las filas por saltos de línea. |
| Base de datos | Una base de datos es un conjunto de datos pertenecientes a un mismo contexto y almacenados sistemáticamente para su posterior uso. Es capaz de almacenar gran cantidad de datos, relacionados y estructurados, que pueden ser consultados rápidamente de acuerdo con las características selectivas que se deseen. |
| Eficiencia | Proporcionar un desempeño apropiado, en relación con la cantidad de recurso utilizado, bajo condiciones establecidas en determinado momento del tiempo. |
| Interfaz | La interfaz es el medio donde el usuario puede comunicarse con una maquina, equipo o dispositivo, y comprender los puntos de contacto entre el usuario y el equipo.  |
| Llave Foranea | Una llave foránea o llave ajena es una limitación referencial entre dos tablas e identifica una columna o grupo de columnas en una tabla que se refiere a una columna o grupo de columnas en otra tabla. |
| Llave Primaria | Una llave primaria es un campo o una combinacion de campos que identifica de forma unica a cada fila de una tabla |
| Parametro | Un parámetro, generalmente, es cualquier característica que pueda ayudar a definir o clasificar un sistema particular. |
| Python | Python es un lenguaje de programación interpretado cuya filosofía hace hincapié en la legibilidad de su código. Se trata de un lenguaje de programación multiparadigma, ya que soporta orientación a objetos, programación imperativa y, en menor medida, programación funcional. |
| Registro | Un registro representa un objeto único de datos implícitamente estructurados en una tabla. |
| Tabla Hash | Una tabla hash es una estructura asosiada a llaves o claves con valores. La operación principal que soporta de manera eficiente es la búsqueda: permite el acceso a los elementos almacenados a partir de una clave generada. |
| Tupla | Una tupla es una lista ordenada finata de elementos (componentes).|

## FAQ

1. ¿PREGUNTA?

> **Respuesta:** RESPUESTA.


## Uso de la librería

Para ejecutar la librería es necesario tener instalado Python 3 para [Windows](https://www.python.org/downloads/windows/) o para [Linux](https://www.python.org/downloads/source/).

TytusStorage se puede incorporar en un proyecto con la siguiente línea de código:

```sh
from storage import TytusStorage
```

Se puede acceder al repertorio de funciones posteriormente descritas de la siguiente manera:

```sh
TytusStorage.createDatabase("new_database", "hash", "ascii")
TytusStorage.showDatabases()
TytusStorage.checksumDatabase("new_database", "MD5")
...
```

Conviene consultar el DOCSTRING de la función de interes, así como imprimir su resultado:

![DOCSTRING](img/docstring.png "DOCSTRING de una función")

```sh
creation = createDatabase("database", "hash", "utf8")
encoding = alterDatabaseEncoding("database", "utf8")
print(creation, ',', encoding)
```

> 0 , 3

TytusStorage almacena todo dentro de la carpeta *data* del proyecto, de manera recurrente y eficaz.


## Uso del almacenamiento

Las siguientes funciones se enfocan en 

### funci(param, param) 
explicacion

| Valor de retorno | Definición |
| ------ | ------ |
| 0 | Operación exitosa |
| 1 | Error en la operación |
| 2 | Base de datos inexistente |
| 3 | Tabla inexistente |


## Uso del administrador del modo de almacenamiento

Las siguientes funciones se enfocan en 

### funci(param, param) 
explicacion

| Valor de retorno | Definición |
| ------ | ------ |
| 0 | Operación exitosa |
| 1 | Error en la operación |
| 2 | Base de datos inexistente |
| 3 | Tabla inexistente |


## Uso del administrador de índices

Las siguientes funciones se enfocan en 

### funci(param, param) 
explicacion

| Valor de retorno | Definición |
| ------ | ------ |
| 0 | Operación exitosa |
| 1 | Error en la operación |
| 2 | Base de datos inexistente |
| 3 | Tabla inexistente |


## Uso del administrador de codificación

Las siguientes funciones se enfocan en 

### funci(param, param) 
explicacion

| Valor de retorno | Definición |
| ------ | ------ |
| 0 | Operación exitosa |
| 1 | Error en la operación |
| 2 | Base de datos inexistente |
| 3 | Tabla inexistente |


## Uso del generador de checksum

Las siguientes funciones se enfocan en 

### funci(param, param) 
explicacion

| Valor de retorno | Definición |
| ------ | ------ |
| 0 | Operación exitosa |
| 1 | Error en la operación |
| 2 | Base de datos inexistente |
| 3 | Tabla inexistente |


## Uso del administrador de compresión de datos

Las siguientes funciones se enfocan en 

### funci(param, param) 
explicacion

| Valor de retorno | Definición |
| ------ | ------ |
| 0 | Operación exitosa |
| 1 | Error en la operación |
| 2 | Base de datos inexistente |
| 3 | Tabla inexistente |


## Uso del administrador de seguridad

Las siguientes funciones se enfocan en 

### funci(param, param) 
explicacion

| Valor de retorno | Definición |
| ------ | ------ |
| 0 | Operación exitosa |
| 1 | Error en la operación |
| 2 | Base de datos inexistente |
| 3 | Tabla inexistente |


## Uso del generador de diagramas de dependencias

Las siguientes funciones se enfocan en 

### funci(param, param) 
explicacion

| Valor de retorno | Definición |
| ------ | ------ |
| 0 | Operación exitosa |
| 1 | Error en la operación |
| 2 | Base de datos inexistente |
| 3 | Tabla inexistente |


## Uso del reportador gráfico

Las siguientes funciones se enfocan en 

### funci(param, param) 
explicacion

| Valor de retorno | Definición |
| ------ | ------ |
| 0 | Operación exitosa |
| 1 | Error en la operación |
| 2 | Base de datos inexistente |
| 3 | Tabla inexistente |
