import mysql.connector
from mysql.connector import Error

def create_connection():
    """ Create a database connection to the MySQL database """
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='7>>HhNN6/fZ',
            database='clima_sostenible'
        )
        if connection.is_connected():
            print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def register_user(nombre, correo, contrasenia):
    """ Register a new user in the database """
    connection = create_connection()
    cursor = connection.cursor()
    try:
        query = "INSERT INTO  sistemaautenticacion (nombre, correo, contrasenia) VALUES (%s, %s, %s)"
        cursor.execute(query, (nombre, correo, contrasenia))
        connection.commit()
        print("User registered successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def check_login(correo, contrasenia):
    """ Check user login credentials """
    connection = create_connection()
    cursor = connection.cursor()
    user = None
    try:
        query = "SELECT * FROM  sistemaautenticacion WHERE correo = %s AND contrasenia = %s"
        cursor.execute(query, (correo, contrasenia))
        user = cursor.fetchone()
        print(f"User found: {user}")
    except Error as e:
        print(f"The error '{e}' occurred")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
    return user



class ForoDebate:
    def __init__(self, titulo, descripcion, punto_de_vista, otras_observaciones=''):
        self.titulo = titulo
        self.descripcion = descripcion
        self.punto_de_vista = punto_de_vista
        self.otras_observaciones = otras_observaciones

    @staticmethod
    def save(titulo, descripcion, punto_de_vista, otras_observaciones=''):
        connection = create_connection()
        cursor = connection.cursor()
        try:
            query = "INSERT INTO foro_debates (titulo, descripcion, punto_de_vista, otras_observaciones) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (titulo, descripcion, punto_de_vista, otras_observaciones))
            connection.commit()
            print("Debate saved successfully")
        except Error as e:
            print(f"The error '{e}' occurred")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

class ForoPregunta:
    def __init__(self, titulo, pregunta):
        self.titulo = titulo
        self.pregunta = pregunta

    @staticmethod
    def save(titulo, pregunta):
        connection = create_connection()
        cursor = connection.cursor()
        try:
            query = "INSERT INTO foro_preguntas (titulo, pregunta) VALUES (%s, %s)"
            cursor.execute(query, (titulo, pregunta))
            connection.commit()
            print("Question saved successfully")
        except Error as e:
            print(f"The error '{e}' occurred")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

class ForoHilo:
    def __init__(self, titulo, tema):
        self.titulo = titulo
        self.tema = tema

    @staticmethod
    def save(titulo, tema):
        connection = create_connection()
        cursor = connection.cursor()
        try:
            query = "INSERT INTO foro_hilos (titulo, tema) VALUES (%s, %s)"
            cursor.execute(query, (titulo, tema))
            connection.commit()
            print("Thread saved successfully")
        except Error as e:
            print(f"The error '{e}' occurred")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()


# Funcion para guardar las campanias en la base de datos
def save_campaign(nombre_campania, descripcion_campania, fecha_inicio, fecha_fin, presupuesto=None):
    connection = create_connection()
    cursor = connection.cursor()

    try:
        if presupuesto == '':
            presupuesto = None  # Convert empty string to None

        if presupuesto is not None:
            query = "INSERT INTO campaign (nombre_campania, descripcion_campania, fecha_inicio, fecha_fin, presupuesto) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (nombre_campania, descripcion_campania, fecha_inicio, fecha_fin, presupuesto))
        else:
            query = "INSERT INTO campaign (nombre_campania, descripcion_campania, fecha_inicio, fecha_fin) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (nombre_campania, descripcion_campania, fecha_inicio, fecha_fin))

        connection.commit()
        print("Campaign saved successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


# Funcion para guardar las denuncias en la base dedatos
def save_denuncia(titulo, descripcion, evidencia_filename, ubicacion, denunciados, otros_detalles=None):
    connection = create_connection()
    cursor = connection.cursor()

    try:
        query = "INSERT INTO denuncias (titulo, descripcion, evidencia_filename, ubicacion, denunciados, otros_detalles) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (titulo, descripcion, evidencia_filename, ubicacion, denunciados, otros_detalles))
        connection.commit()
        print("Denuncia saved successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


def get_all_debates():

    connection = create_connection()
    cursor = connection.cursor(dictionary=True)
    debates = []
    try:
        query = "SELECT * FROM foro_debates ORDER BY fecha_creacion DESC"
        cursor.execute(query)
        debates = cursor.fetchall()
    except Error as e:
        print(f"The error '{e}' occurred")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
    return debates

def get_all_questions():

    connection = create_connection()
    cursor = connection.cursor(dictionary=True)
    questions = []
    try:
        query = "SELECT * FROM foro_preguntas ORDER BY fecha_creacion DESC"
        cursor.execute(query)
        questions = cursor.fetchall()
    except Error as e:
        print(f"The error '{e}' occurred")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
    return questions

def get_all_threads():

    connection = create_connection()
    cursor = connection.cursor(dictionary=True)
    threads = []
    try:
        query = "SELECT * FROM foro_hilos ORDER BY fecha_creacion DESC"
        cursor.execute(query)
        threads = cursor.fetchall()
    except Error as e:
        print(f"The error '{e}' occurred")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
    return threads
