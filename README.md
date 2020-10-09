# Proyecto
COMPILERS PROJECT PAR ++

# Tabla de contenidos

- [Proyecto](#proyecto)
- [Table of contents](#tabla-de-contenidos)
- [Avance 1](#avance1)
- [Tecnologías](#tecnologías)

# Avance 1
[(Back to top)](#tabla-de-contenidos)

Avance 1 - Léxico Sintaxis

En este primer avance después de haber logrado definir los diagramas de las gramáticas a utilizar en el lenguaje PAR ++ se utilizó PLY como Analizador Léxico y Sintactico, se definieron todos los tokens mas comunes a utilizar en un lenguaje de programación usandolos mas tarde en la definición de la sintaxis de las gramáticas determinadas en los diagramas.

El lenguaje manejado tiene algunas similitudes con algunos lenguajes que actualmente se usan por lo que el léxico será familiar, a continuación listamos los tipos de grámaticas con los que cuenta:
 - Programa
 - Variables
 - Tipos de variables
 - Definición de IDs
 - Dimensiones de matrices y arreglos
 - Funciones tipo void y return
 - Estructura de parámetros
 - Asignaciones
 - Lectura
 - Escritura
 - Condicionales
 - Ciclos
 - Constantes
 - Expresiones
 - Comparadores

Para correr el programa se tiene que contar en el directorio del mismo un archivo llamado Input.txt con el código a probar, si es aceptable nos indicará que el código es "Apropiado", si existe algo que no se cuente estructurado de la manera en la que se definieron las gramáticas nos indicara "No Apropiado"

# Tecnologías
[(Back to top)](#tabla-de-contenidos)

PLY-3.11
Python 3.8.1
