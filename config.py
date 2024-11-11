from flask import Flask
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://attendanceDB_upwardate:815da069d6094be1f50757a78ad5301fe23a800e@zvbxl.h.filess.io:3305/attendanceDB_upwardate'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/')
def home():
    return "21.83.0627 Fanes Setiawan"

app.app_context().push()
