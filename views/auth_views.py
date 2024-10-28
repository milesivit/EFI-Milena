from flask import Blueprint, request, jsonify, make_response
from datetime import timedelta
from flask_jwt_extended import (
    get_jwt,                 # Permite obtener el contenido del token JWT
    get_jwt_identity,        # Permite obtener la identidad del usuario actual del token
    jwt_required,            # Decorador que exige la autenticación con JWT para acceder a una ruta
    create_access_token,     # Crea un token de acceso JWT
)
from werkzeug.security import generate_password_hash, check_password_hash  # Utilidades para manejar hashes de contraseñas
from app import db                  # Importa la instancia de la base de datos de la app Flask
from models import User             # Importa el modelo de usuario
from schemas import UserSchema, UserMinimalSchema  # Importa los esquemas para serializar usuarios

# Crea un Blueprint llamado "auth", que permite definir rutas específicas para autenticación
auth_bp = Blueprint("auth", __name__)

# Define la ruta "/login" para iniciar sesión. Solo acepta el método POST
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.authorization  # Obtiene las credenciales enviadas en la solicitud
    username = data.username      # Extrae el nombre de usuario
    password = data.password      # Extrae la contraseña

    # Busca al usuario en la base de datos según el nombre de usuario
    usuario = User.query.filter_by(username=username).first()

    # Verifica si el usuario existe y si la contraseña coincide
    if usuario and check_password_hash(pwhash=usuario.password_hash, password=password):
        acces_token = create_access_token(
            identity=username,                          # Identidad del usuario en el token
            expires_delta=timedelta(minutes=20),        # Expira en 20 minutos
            additional_claims=dict(administrador=usuario.is_admin),  # Añade un reclamo adicional indicando si es admin
        )
        return jsonify({"Token": f"{acces_token}"})     # Devuelve el token de acceso
    return jsonify({"Mensaje": "El usuario y la contraseña no coinciden."})  # Mensaje de error si falla la autenticación

# Define la ruta "/users" para listar o crear usuarios. Acepta métodos GET y POST. Requiere autenticación JWT.
@auth_bp.route("/users", methods=["GET", "POST"])
@jwt_required()
def user():
    # Obtiene datos adicionales del JWT, como si el usuario es administrador
    additional_data = get_jwt()
    administrador = additional_data.get(
        "administrador", False
    )  # Asigna False por defecto si no está presente

    # Si el método es POST, intenta crear un nuevo usuario
    if request.method == "POST":
        if administrador:  # Verifica si el usuario autenticado es administrador
            data = request.get_json()       # Obtiene los datos JSON enviados en la solicitud
            username = data.get("nombre_usuario")  # Extrae el nombre de usuario
            password = data.get("password")  # Extrae la contraseña

            # Verifica si el usuario ya existe en la base de datos
            si_existe_usuario = User.query.filter_by(username=username).first()
            if si_existe_usuario:
                return jsonify({"Error": "El nombre de usuario ya existe."}), 400  # Retorna error si el usuario ya existe

            # Genera el hash de la contraseña
            password_hasheada = generate_password_hash(
                password=password,
                method="pbkdf2",
                salt_length=8,
            )
            print(password_hasheada)  # Imprime el hash de la contraseña para verificar

            try:
                # Crea un nuevo usuario y lo agrega a la base de datos
                nuevo_usuario = User(username=username, password_hash=password_hasheada)
                db.session.add(nuevo_usuario)
                db.session.commit()

                return jsonify({"Usuario Creado": username}), 201  # Retorno correcto si el usuario se crea con éxito
            except:
                return jsonify({"Error": "Ocurrió un error al crear usuario."})  # Devuelve un error si ocurre un problema

        # Si no es administrador, devuelve un mensaje de no autorizado con código 403
        return (
            jsonify({"Mensaje": "UD no está habilitado para crear un usuario."}),
            403,
        )

    # Si el método es GET, obtiene y devuelve una lista de usuarios
    usuarios = User.query.all()  # Consulta todos los usuarios
    if administrador:
        return jsonify(UserSchema().dump(obj=usuarios, many=True))  # Si es admin, muestra todos los datos de usuario
    else:
        return jsonify(UserMinimalSchema().dump(obj=usuarios, many=True))  # Si no es admin, muestra datos mínimos
