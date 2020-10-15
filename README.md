# Proyecto
COMPILERS PROJECT PAR ++

# Tabla de contenidos

- [Proyecto](#proyecto)
- [Table of contents](#tabla-de-contenidos)
- [Avance 1](#avance1)
- [Avance 2](#avance2)
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
# Avance 2
[(Back to top)](#tabla-de-contenidos)

Avance 2 - Semántica

Para este segundo avance se definió el comportamiento de la semántica en los tipos de variables que manejaremos de acuerdo a los operadores definidos en nuestro léxico, ejemplo:
 Operando Izquierdo       Operando Derecho         Operador         Resultado
       int                      int                   +                int
       float                    int                   -                float
       char                     float                 >                err
       int                      int                   ==               bool
      
La tabla completa de estos escenarios de nuestra semántica, también conocida como Cubo Semántico,  se puede visualizar completa en el documento Semánitca.pdf. 
Lo que tratamos de expresar con esta estructura es las combinaciones que se podrán realizar con el lenguage Par++ asi como las combinaciones que detonarian un error, es decir si sumamos una variable de tipo int con otra variable de tipo int el resultado será de tipo int, asi mismo con los demas operandos y los tipos de variables.

El resultado err (error) nos indica que la combinación de esas variables no es posible.  

# Tecnologías
[(Back to top)](#tabla-de-contenidos)

- PLY-3.11
- Python 3.8.1
