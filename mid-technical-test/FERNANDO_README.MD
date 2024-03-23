# IMPORTANTE
No logré correr el docker de tests por lo que no pude desarrollar las pruebas unitarias

Todos los endpoints funcionan de manera correcta.
Hice una arquitectura no muy compleja que funciona así:
router -> service -> dao(database logic)

El router llama los servicios y en los servicios se encuentra la logica de la API, los servicios llaman funciones del dao que practicamente solo son querys, así me permite reutilizar los querys y modulos de los servicios en muchas partes del código.

De esta manera me aseguré de que el proyecto esté correctamente modularizado y sigue los principios SOLID, asegurandome que estén bien hechos los imports, herencia y cada función tiene una unica responsabilidad permitiendome reutilizar funciones en muchos lugares del código.

## Extras que pude desarrollar

- Colección de POSTMAN exportada en JSON.
- Autenticación usando token JWT, no alcancé a desarrollar permisos o grupos para hacer validaciones extras, pero lo he hecho antes y me fue suficiente tiempo para implementar el login que funciona así:
    Create user -> login (returns user token) -> get actual user(returns user info)
    TODOS LOS ENDPOINTS REQUIEREN ESTAR LOGUEADO PARA USARLOS EXCEPTO LOS DE LOS USERS
- Mejora de endpoint List:
    Implementé paginación, se manda la pagina y el tamaño de la pagina y esto regresa los resultados paginados