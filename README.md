# Proyecto
COMPILERS PROJECT PAR ++

# Tabla de contenidos

- [Proyecto](#proyecto)
- [Table of contents](#tabla-de-contenidos)
- [Avance 1](#avance1)
- [Avance 2](#avance2)
- [Avance 3](#avance3)
- [Avance 4](#avance4)
- [Avance 5](#avance4)
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
| Operando Izquierdo  | Operando Derecho  |  Operador   |  Resultado  |
| ------------------- | ----------------- | ----------- | ----------- |
|        int          |       int         |      +      |      int    |
|        float        |       int         |      -      |      float  |
|        char         |       float       |      >      |      err    |
|        int          |       int         |      ==     |      bool   |
 
      
La tabla completa de estos escenarios de nuestra semántica, también conocida como Cubo Semántico,  se puede visualizar completa en el documento Semánitca.pdf. 
Lo que tratamos de expresar con esta estructura es las combinaciones que se podrán realizar con el lenguage Par++ asi como las combinaciones que detonarian un error, es decir si sumamos una variable de tipo int con otra variable de tipo int el resultado será de tipo int, asi mismo con los demas operandos y los tipos de variables.

El resultado err (error) nos indica que la combinación de esas variables no es posible.  

# Avance 3
[(Back to top)](#tabla-de-contenidos)

En este avance se hizo un refactor del cubo semántico para un mejor rendimiento al momento de acceder a este, la tabla de funciones y variables fue implementada usando diccionarios en los cuales se definio que nuestras funciones guardarían los siguientes valores:

- Nombre
- Tipo de retorno
- Parametros
- Variables (scope)

Ademas se implementaron algunos de los puntos neuralgicos a ocupar en nuestra gramáticas los cuales harán uso de los cuadruplos a generar, el cubo semantico, tabla de funciones y variables. 

# Avance 4
[(Back to top)](#tabla-de-contenidos)

 Se reestructuró la forma en que las variables y funcioones son guardadas, se estarán manejando diccionarios para facil acceso al buscar.
 Debido a que se estarán implementando arreglos y matrices se agregaron validaciones para identificar si las variables definidas son simples, arreglos o matrices, teniendo en cuenta que al revisar la gramática el programa validará la cantidad de elementos que contiene para hacer esta validación.
 
 Se definieron los espacios de memoria para los entornos
 
- Global
- Local
- Constantes

Asi como también el poder guardar estás variables a traves de un diccionario.

# Avance 5
En este avance se realizó el código intermedio para realizar las siguientes acciones:
- Validaciones semánticas llamando a la clase SemanticCube.py
- Guardar variables globales en la tabla global llamando a la clase FunctionTable.py
- Guardar variables locales dentro de las tablas de variables llamando a la clase FunctionTable.py
- Guardar parámetros de las funciones dentro de la estructura interna param types y paramsNumber

Se generaron cuadruplos para las siguientes expresiones:
- Expresiones aritméticas
- Estatutos condicionales
- Estatutos secuenciales
- Funciones

Se realizó el mapa de memoria para la maquina virtual usando diccionarios para cada entorno del programa, cada diccionario tiene llaves con los tipos de variables es decir (int, float, bool, char) para en el momento de guardar las variables se guarder en el espacio correcto.
Para la clase memory.py se crearon funciones para asignar espacio de memoria de acuerdo al entorno y tipo de dato, función para obtener valores guardados dentro de estás estructuras y función para resetear contadores cuando se termine de ejecutar una función.


# Tecnologías
[(Back to top)](#tabla-de-contenidos)

- PLY-3.11
- Python 3.8.1
