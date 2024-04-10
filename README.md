
# Wiki

Enciclopedia donde se pueden buscar palabras, añadir nuevas y editarlas u obtener palabras al azar.


## Funciones

- Convertidor
- Entrada
- Búsqueda
- Nueva_página
- Editar
- Guardar
- Random


## Apéndice

### Convertidor

En views.py creé una función llamada convertidor, esta convierte de markdown a html, toma como parametro el nombre del archivo, si el archivo existe lo convierte sino retorna None

### Entrada

Creé una función llamada entrada que recibe el parámetro de request y archivo, la cual llama a la función convertidor, si archivo no existe entonces renderiza error.html, si existe renderiza entry.html enviando el titulo y el contenido del archivo

### Búsqueda

Esta función obtiene la información del input en la barra de búsqueda con nombre "bus", convierte el archivo markdown con el nombre obtenido del input, en el caso de que no existe entonces lista todos los archivos que existen, se creó una lista vacía llamada recomendaciones y verifica si lo que hay en "bus" está dentro del nombre de los archivos existentes, en el caso que sí, entonces añade a la lista de recomendaciones el nombre del archivo y renderiza busqueda.html donde pasa la lista recomendaciones al template.

### Nueva página

En el metodo get simplemente renderiza new.html, en el metodo post obtiene los valores de los inputs "titulo" y "contenido" que se encuentran en new.html, verifica primero si el nombre ya existe, si ya existe renderizar error.html, si no, utiliza la función save_entry y guarda el archivo en la carpeta entries, convierte el archivo a html y renderiza entry.html, pasando el titulo del archivo y el contenido ya convertido 

### Editar

Toma el valor del input "titulo_entrada", obtiene la información del archivo con ese nombre y renderiza editar.html con el titulo y contenido

### Guardar

Toma los valores de los inputs "titulo" y "contenido", guarda en entries el archivo, convierte el archivo a html y renderiza la página entry.html pasando el titulo y el contenido html

### Random

Obtiene la lista de todos los archivos existentes, utiliza la funcion randome.choice() de python, convierte el archivo aleatorio, renderiza entry.html pasando el titulo y el contenido.

## Authors

- [@josephAhmedVargas](https://github.com/josephAhmedVargas)

