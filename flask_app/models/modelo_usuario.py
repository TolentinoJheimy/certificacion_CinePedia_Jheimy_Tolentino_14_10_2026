import re

from pymysql.err import IntegrityError

from flask_app.config.conexion_mysql import conectar_mysql


class Usuario:
    @staticmethod
    # Busca al usuario por su id; si no existe, devuelve None.
    def buscar_por_id(usuario_id):
        if usuario_id is None:
            return None

        filas = conectar_mysql().consultar(
            'SELECT * FROM usuarios WHERE id = %s',
            (usuario_id,),
        )
        return filas[0] if filas else None

    @staticmethod
    # Busca el correo para identificar al usuario.
    def buscar_por_correo(correo):
        filas = conectar_mysql().consultar(
            'SELECT * FROM usuarios WHERE correo = %s',
            (correo,),
        )
        return filas[0] if filas else None

    @staticmethod
    # Guarda al usuario y avisa si el correo ya esta registrado.
    def crear(datos):
        try:
            return conectar_mysql().consultar(
                'INSERT INTO usuarios(nombre,apellido,correo,contrasena_hash) VALUES(%s,%s,%s,%s)',
                (
                    datos['nombre'],
                    datos['apellido'],
                    datos['correo'],
                    datos['contrasena_hash'],
                ),
            )
        except IntegrityError as error:
            if error.args[0] == 1062:
                raise ValueError('El e-mail ya está registrado.') from error
            raise

    @staticmethod
    # Guarda el nuevo hash de la contraseña del usuario.
    def actualizar_contrasena(usuario_id, contrasena_hash):
        return conectar_mysql().consultar(
            'UPDATE usuarios SET contrasena_hash=%s WHERE id=%s',
            (contrasena_hash, usuario_id),
        )

    @staticmethod
    # Revisa los datos del registro y reune los errores encontrados.
    def validar_registro(datos, contrasena, confirmacion):
        errores = []

        if len(datos['nombre']) < 2:
            errores.append('El nombre debe tener al menos 2 caracteres.')
        if len(datos['apellido']) < 2:
            errores.append('El apellido debe tener al menos 2 caracteres.')
        if not re.fullmatch(r'[^\s@]+@[^\s@]+\.[^\s@]+', datos['correo']):
            errores.append('Ingresa un e-mail válido.')
        if not contrasena.strip():
            errores.append('La contraseña no puede estar vacía.')
        if len(contrasena.encode('utf-8')) > 72:
            errores.append('La contraseña debe ocupar como máximo 72 bytes.')
        if contrasena != confirmacion:
            errores.append('La contraseña y su confirmación deben ser iguales.')
        if len(datos['nombre']) > 255 or len(datos['apellido']) > 255:
            errores.append(
                'El nombre y apellido deben tener como máximo 255 caracteres.'
            )
        if len(datos['correo']) > 254:
            errores.append('El e-mail debe tener como máximo 254 caracteres.')
        if Usuario.buscar_por_correo(datos['correo']):
            errores.append('El e-mail ya está registrado.')

        return errores
