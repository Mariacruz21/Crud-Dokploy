from app import app
from dotenv import load_dotenv
import os

load_dotenv()

# Mysql Settings (se quedan, no afectan)
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')
app.config['MYSQL_PORT'] = int(os.getenv('MYSQL_PORT', 3306))
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# 🚨 IMPORTANTE: NO conectar MySQL aún
# mysql = MySQL(app)
