# tarea01-PS

## Requerimiento

"Mypass": Escribir un programa que permita a los usuarios almacenar y gestionar contraseñas de forma segura en línea de comandos, con opciones para agregar, recuperar, actualizar y eliminar contraseñas. Se podrá entregar información adicional a cada contraseña para facilitar la busqueda al usuario, por ejemplo una palabra clave. El almacenamiento de la contraseña debe ser seguro. 
Las claves son almacenadas de manera encriptada con la libreria Fernet y una key generada al momento.
La clave Maestra es encriptada con un HASH MD5

Adicionalmente la solución tendrá una módulo "Generador de Contraseñas": Crear una herramienta que genere contraseñas seguras y las muestre en línea de comandos, permitiendo a los usuarios especificar la longitud y los caracteres permitidos. 
Se generan claves con un largo designado por el usuario y los elementos permitidos por este.

## Instrucciones para interacción con línea de comandos
A continuación se presentan ejemplos que demuestran cómo se interactúa usando la línea de comandos.

### POST Method
```bash
curl -X POST -H "Content-Type: application/json" -d "{"""keyword""": """secret""", """length""": 12, """lowercase""": true, """uppercase""": true, """digits""": true, """punctuation""": true}" http://localhost:5000/passwords
```
Método para agregar contraseña. Se debe ingresar todos los campos que aparecen para generar correctamente una contraseña.

### GET Method
```bash
curl http://localhost:5000/passwords/secret
```
Método para obtener contraseña. Se debe otorgar palabra clave ya existente para funcionar correctamente.

### PUT Method
```bash
curl -X PUT -H "Content-Type: application/json" -d "{"""keyword""": """secret""", """length""": 12, """lowercase""": true, """uppercase""": true, """digits""": true, """punctuation""": true}" http://localhost:5000/passwords/secret
```
Método para actualizar contraseña. Se debe ingresar todos los campos que aparecen para actualizar correctamente una contraseña.

### POST Method
```bash
curl -X DELETE http://localhost:5000/passwords/secret
```
Método para eliminar contraseña. Se debe otorgar palabra clave ya existente para funcionar correctamente.