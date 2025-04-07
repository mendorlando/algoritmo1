from flask import Flask

# Inicializar la aplicación
app = Flask(__name__)

# Aquí puedes agregar configuraciones adicionales si es necesario
app.config['SECRET_KEY'] = 'mi_clave_secreta'

# Importar las rutas después de crear la aplicación
from app import routes

