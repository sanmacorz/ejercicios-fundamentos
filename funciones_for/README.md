# Funciones

## Variables locales y globales

### Variables locales

- Variables que se definen dentro de una función.
- Son válidas únicamente dentro de la función.
- Las variables correspondientes a la función solamente son accesibles por la función, es decir, se pueden usar solamente por ella. Al usarlas fuera de la función marcará error.
- Una variable del algoritmo principal que se pasa a una función donde se modifica y es variable local, cambia su valor en la función pero NO en el algoritmo principal.

### Variables globales

- Son aquellas que no importa donde se usen o modifiquen siempre conservan los valore asignados, ya sea en el algoritmo principal o en las funciones.
- Para hacer que una variable sea global hay que definirla como tal por medio de la instrucción 'global nombre_variable'

## Llamado por valor y llamado por referencia

### Paso por valor

- Cuando se pasa una variable a una función creando una nueva localidad de memoria, donde se copian los valores de los parámetros de la función.
- La memoria ocupada aumenta de tamaño.
- Aunque en Python no se aumenta la memoria, el paso de la variable es equivalente a paso por valor.

### Paso por referencia

- La variable se puede modificar en la función y el cambio siempre se realiza usando la referencia a la localidad de memoria donde se almacena la variable. Ej. variables tipo lista.

## Funciones lambda

- Declaración de una funciónn en un solo renglón Ej:
  'f = lambda parametros:operacion'
