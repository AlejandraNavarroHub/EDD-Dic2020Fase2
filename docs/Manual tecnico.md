# Manual Técnico

## Índice

- [Introducción](#introducción)
- [Objetivos](#objetivos)
- [Alcances del proyecto](#alcances-del-proyecto)
- [Requerimentos funcionales](#requerimentos-funcionales)
- [Atributos del sistema](#atributos-del-sistema)
- [Administrador de almacenamiento](#administrador-de-almacenamiento)
- [Administrador del modo de almacenamiento](#administrador-del-modo-de-almacenamiento)
- [Administrador de índices](#administrador-de-índices)
- [Administrador de codificación](#administrador-de-codificación)
- [Generador de checksum](#generador-de-checksum)
- [Administrador de compresión de datos](#administrador-de-compresión-de-datos)
- [Administrador de seguridad](#administrador-de-seguridad)
- [Generador de diagramas de dependencias](#generador-de-diagramas-de-dependencias)
- [Repotrador gráfico](#reportador-grafico)
- [Diagrama de clases](#diagrama-de-clases)
- [Diagrama de Gantt](#diagrama-de-gantt)

## Introducción
TytusStorage busca ser una libreria capaz de proveer las funciones necesarias para ser usada como un DBMS, dicha libreria sera utilizada por los estudiantes del curso de Organizacion y Lenguajes de Compiladores 2 (Estudiantes con los cuales se esta trabajando en conjunto), para construir un lenguaje basado en SQL, que consumira las funciones de esta libreria.

La libreria pretende contar con todas las funciones de un DBMS como MySQL o PostgreSQL, entre ellas funciones de criptografia, encoding y hasta compresion de datos. 

Este manual pretende dar una explicacion del desarrollo de la libreria, para que cualquier desarrollador con conocimientos en estructuras y bases de datos pueda retomar el proyecto y fortalecer las debilidades que puedan ser evidenciadas en este.

## Objetivos

### General

obj

### Específicos

- obj
- obj
- obj

## Alcances del proyecto

Este proyecto es la segunda fase de un proyecto de nombre HashMode, el cual se puede revisar su documentacion [aqui.](https://github.com/tytusdb/tytus/blob/main/storage/team15/docs/Manual%20tecnico.md) Como se puede observar en la primera fase de este proyecto se desarrollo la estuctura para el almacenamiento interno de un DBMS, buscando crear las funciones necesarias para poder crear un administrador de bases de datos funcional y eficaz, en dicha fase la estructura utilizada fue una tabla hash, por las ventajas ahi descritas. Sin embargo, ese proyecto solo fue una de las partes que constituiran esta segunda fase, el proyecto fue construido en conjunto a otros compañeros del curso Estructuras de Datos, el objetivo de otros grupos era la construccion del mismo administrador pero con estructuras de datos distintas, arbol b, arbol b+, AVL, json, diccionarios e isam.

Esta segunda fase consiste en la unificacion de todos los modos de almacenamiento en una sola libreria universal, la cual tendra las mismas funciones que cada una de las librerias individuales y ciertos agregados extra, esta libreria hace posible la eleccion del modo de almacenamineto a utilizar en la creacion de las bases de datos, asi como tambien permite cambiar de modo una tabla en especifico, ademas de esta posibilidad, la libreria permite tambien la eleccion del encoding a utilizar, teniendo entre sus opciones ascii, iso-8859-1 y utf-8.

Adicionalmente, la libreria provee de una forma de compresion de datos, con la cual segun el modo elegido es posible la reduccion del espacio que una tabla o base de datos ocupa en nuestra computadora, siendo esto de gran beneficio para el almacenamiento de las bases de datos, dandonos un almacenaminto mas ligero y efectivo.

En caso del envio de datos, se provee de una funcion de cheksum, la cual permite verificar la integridad de los datos enviados, asi mismo, la libreria cuenta con funciones de seguridad especificamente de criptografia y una forma de monitorear la integridad de los datos por medio de blockchain, este metodo se conoce como Tablas Seguras, lo cual consiste en un modo en el cual cada nuevo insert constituye un bloque de BLockChain, y un update de uno de los nuevos datos representa la perdida de la integridad de los datos, lo cual indica que la tabla fue modificada. 

## Requerimentos funcionales

- req
- req
- req

## Atributos del sistema

- at
- at
- at

## Administrador de almacenamiento

cuerpo

## Administrador del modo de almacenamiento

cuerpo

## Administrador de índices

cuerpo

## Administrador de codificación

cuerpo

## Generador de checksum

cuerpo

## Administrador de compresión de datos

cuerpo

## Administrador de seguridad

cuerpo

## Generador de diagramas de dependencias

cuerpo

## Reportador gráfico

cuerpo

## Diagrama de clases

![diagrama-clases](img/diagrama-clases.png "Diagrama de clases")

## Diagrama de Gantt

![diagrama-gantt](img/diagrama-gantt.jpg "Diagrama de Gantt")
