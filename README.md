# tarea01-PS

## Nombres

- Gastón Quevedo
- Jorge Roldán

## Descripción

Es un gestor de contraseñas implementado con metodos CRUD y manejado a traves de la CMD de Windows

## Instalación

Requiere la instalación de las librerias cryptography, Flask.

## Cómo usar

Requiere CMD. A continuación se muestran los comandos de uso para el gestor de contraseñas. Se usan como ejemplo las siguientes variables: user, password, secret las cuales son username, masterpassword y keyword respectivamente.

### POST Method
```bash
curl -X POST -H "Content-Type: application/json" -d "{"""username""": """user""", """password""": """password"""}"  http://localhost:5000/users
```
Método para agregar usuarios. Se deben ingresar ambos campos para generar un usuario

### GET Method
```bash
curl http://localhost:5000//users/user?password=password
```
Método para iniciar sesion.

### GET Method
```bash
curl http://localhost:5000/users/user/logout
```
Método para cerrar sesion.

### POST Method
```bash
curl -X POST -H "Content-Type: application/json" -d "{"""keyword""": """secret""", """length""": 12, """lowercase""": true, """uppercase""": true, """digits""": true, """punctuation""": true}" http://localhost:5000/users/user/passwords?random=true
```
Método para agregar contraseña. Se debe ingresar todos los campos que aparecen para generar correctamente una contraseña.

### POST Method
```bash
curl -X POST -H "Content-Type: application/json" -d "{"""keyword""": """secret""", """password""":"""password"""}" http://localhost:5000/users/user/passwords?random=false
```
Método para agregar contraseña. Se debe ingresar todos los campos que aparecen para agregar correctamente una contraseña.

### GET Method
```bash
curl http://localhost:5000/users/user/passwords/secret
```
Método para obtener contraseña. Se debe otorgar palabra clave ya existente para funcionar correctamente.

### PUT Method
```bash
curl -X PUT -H "Content-Type: application/json" -d "{"""keyword""": """secret""", """length""": 12, """lowercase""": true, """uppercase""": true, """digits""": true, """punctuation""": true}" http://localhost:5000/users/user/passwords/secret?random=true
```
Método para actualizar contraseña. Se debe ingresar todos los campos que aparecen para actualizar correctamente una contraseña a una aleatoria.

### PUT Method
```bash
curl -X PUT -H "Content-Type: application/json" -d "{"""keyword""": """secret""", """password""": """password"""}" http://localhost:5000/users/user/passwords/secret?random=false
```
Método para actualizar contraseña. Se debe ingresar todos los campos que aparecen para actualizar correctamente una contraseña.

### POST Method
```bash
curl -X DELETE http://localhost:5000/users/user/passwords/secret
```
Método para eliminar contraseña. Se debe otorgar palabra clave ya existente para funcionar correctamente.

##Cómo contribuir

Pendiente

##Licencia

MIT License

Copyright (c) 2024 Gastón Quevedo - Jorge Roldán

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
