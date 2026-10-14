# CinePedia

CinePedia es una aplicación web para compartir películas y comentar sobre ellas. Permite registrarse, iniciar sesión, explorar el catálogo y ver los detalles de cada película. Cada usuario puede agregar, editar y eliminar sus propias películas, además de comentar las de otros usuarios.

## Tecnologías utilizadas

- **Python y Flask:** para la lógica del proyecto y las rutas de la aplicación.
- **MySQL y PyMySQL:** para guardar y consultar usuarios, películas y comentarios.
- **HTML, CSS y JavaScript:** para las páginas, los estilos y la interacción en el navegador.
- **Flask-Bcrypt:** para proteger las contraseñas mediante hashes.
- **python-dotenv:** para cargar la configuración desde un archivo `.env`.


## Estructura de carpetas

```text
.
├── .env
├── .env.example
├── .gitignore
├── Pipfile
├── Pipfile.lock
├── requirements.txt
├── run.py
├── flask_app/
│   ├── __init__.py
│   ├── config/
│   │   └── conexion_mysql.py
│   ├── controllers/
│   │   ├── controlador_peliculas.py
│   │   └── controlador_usuarios.py
│   ├── models/
│   │   ├── modelo_comentario.py
│   │   ├── modelo_pelicula.py
│   │   └── modelo_usuario.py
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   └── js/
│   │       └── script.js
│   └── templates/
│       ├── base.html
│       ├── editar_pelicula.html
│       ├── error.html
│       ├── inicio.html
│       ├── macros.html
│       ├── nueva_pelicula.html
│       ├── principal.html
│       └── ver_pelicula.html
└── resources/
    ├── README.md
    ├── CinePedia.png
    └── DB/
        ├── cinepedia.sql
        ├── migracion_3fn.sql
        ├── cinePedia.mwb
        └── ERD.png
```

## Autor

JheimyTolentino
