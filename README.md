# tarea01-PS

## Requerimiento

"Mypass": Escribir un programa que permita a los usuarios almacenar y gestionar contraseñas de forma segura en línea de comandos, con opciones para agregar, recuperar, actualizar y eliminar contraseñas. Se podrá entregar información adicional a cada contraseña para facilitar la busqueda al usuario, por ejemplo una palabra clave. El almacenamiento de la contraseña debe ser seguro. 
Las claves son almacenadas de manera encriptada con la libreria Fernet y una key generada al momento.
La clave Maestra es encriptada con un HASH MD5

Adicionalmente la solución tendrá una módulo "Generador de Contraseñas": Crear una herramienta que genere contraseñas seguras y las muestre en línea de comandos, permitiendo a los usuarios especificar la longitud y los caracteres permitidos. Consideramos seguro que contenga combinaciones aleatorias de los elementos permitidos por el usuario.
