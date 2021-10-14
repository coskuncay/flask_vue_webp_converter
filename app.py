from flask import Flask,request, Response, jsonify
from flask_sqlalchemy import SQLAlchemy
import datetime
from config import postgresqlConfig
import csv
import hashlib
from flask_cors import CORS
from PIL import Image
import io


app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = postgresqlConfig
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

class App(db.Model):
    __tablename__ = 'apps'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR)
    icon = db.Column(db.VARCHAR)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def __init__(self, id, name, icon, created_at, updated_at):
        if "".__eq__(updated_at):
            updated_at = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        self.id = id
        self.name = name
        self.icon = icon
        self.created_at = created_at
        self.updated_at = updated_at

    @staticmethod
    def add_app(_id, _name, _icon, _created_at , _updated_at):
        new_app = App(id=_id, name=_name, icon=_icon, created_at=_created_at, updated_at=_updated_at)
        db.session.add(new_app)
        db.session.commit()

    @staticmethod
    def json(self):
        return {'id': self.id, 'name': self.name,
                'icon': self.icon, 'created_at': self.created_at , 'updated_at': self.updated_at}



class Screenshot(db.Model):
    __tablename__ = 'screenshots'
    id = db.Column(db.Integer, primary_key=True)
    app_id = db.Column(db.Integer, db.ForeignKey('apps.id'))
    app = db.relationship("App", backref=db.backref("apps", uselist=False))
    file_name = db.Column(db.VARCHAR)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def __init__(self, id, app_id, file_name, created_at, updated_at):
        if "".__eq__(updated_at):
            updated_at = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        self.id = id
        self.app_id = app_id
        self.file_name = file_name
        self.created_at = created_at
        self.updated_at = updated_at

    @staticmethod
    def json(self):
        return {'id': self.id, 'app_id': self.app_id,
                'app': App.json(self.app), 'file_name': self.file_name, 'created_at': self.created_at, 'updated_at': self.updated_at}


    @staticmethod
    def add_screenshot(_id, _app_id, _file_name, _created_at, _updated_at):
        new_ss = Screenshot(id=_id, app_id=_app_id, file_name=_file_name, created_at=_created_at, updated_at=_updated_at)
        db.session.add(new_ss)
        db.session.commit()

    @staticmethod
    def get_all_ss():
        return [Screenshot.json(ss) for ss in Screenshot.query.all()]

    @staticmethod
    def get_ss_id(_id):
        return [Screenshot.json(Screenshot.query.filter_by(id=_id).first())]

def sethash(s):
    return str(int(hashlib.sha256(s.encode('utf-8')).hexdigest(), 16) % 10**8)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, db.Identity(start=1, increment=1, cycle=True), primary_key=True)
    username = db.Column(db.VARCHAR)
    password = db.Column(db.VARCHAR)

    @staticmethod
    def json(self):
        if self is None:
            return None
        return {'name': self.username,
                'password': self.password}

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @staticmethod
    def add_user(_username, _password):
        user = User.json(User.query.filter_by(username=_username).first())
        if user is not None:
            return {
                'success': False,
                'msg': "Username is taken"
            }

        new_user = User(username=_username, password=_password)
        db.session.add(new_user)
        db.session.commit()
        return {
            'success': True,
            'msg': "Successfully Registered"
        }

    @staticmethod
    def login(username, password):
        user = User.json(User.query.filter_by(username=username).first())
        if user is None:
            return {
                    'success': False,
                    'msg': "User not found"
                }
        else:
            hashedPwd = sethash(password)
            if hashedPwd == user["password"]:
                return {
                    'success': True,
                    'msg': "Successful"
                }
            return {
                    'success': False,
                    'msg': "Wrong Password"
                }

def create_database():
    db.create_all()


create_database()

User.add_user("appz", sethash("`123456&*"))
User.add_user("1", sethash("1"))

def read_app_file(filename):
    with open("{}".format(filename)) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        isAppFile = True
        for row in csv_reader:
            if line_count == 0:
                if 'app_id' in row:
                    isAppFile = False
                line_count += 1
            else:
                if isAppFile:
                    App.add_app(row[0], row[1], row[2], row[3], row[4])
                else:
                    Screenshot.add_screenshot(row[0], row[1], row[2], row[3], row[4])
                line_count += 1


read_app_file("static/sample_apps.csv")

read_app_file("static/sample_screeshots.csv")


@app.route('/login', methods=['POST'])
def login():
    if request.method == "POST":
        data = request.get_json(force=True)
        verified = User.login(data["username"], data["password"])
        return jsonify(verified)


@app.route('/register', methods=['POST'])
def register():
    if request.method == "POST":
        data = request.get_json(force=True)
        verified = User.add_user(data["username"], sethash(data["password"]))
        return jsonify(verified)


@app.route('/convert', methods=['POST'])
def convert():
    if request.method == "POST":
        image_data = request.get_data()
        image = Image.frombytes('RGBA', (128,128), image_data, 'raw')
        image.show()
        return jsonify(True)



@app.route('/api/apps', methods=['GET'])
def get_all_apps():
    return {
        'data': [App.json(app) for app in App.query.all()],
    }

@app.route('/api/apps/<id>', methods=['GET'])
def get_app_by_id(id):
    return {
        'data': App.json(App.query.filter_by(id=id).first())
    }


@app.route('/api/screenshots', methods=['GET'])
def screenshots():
    if request.method == "GET":
        return {
            'data': Screenshot.get_all_ss(),
        }



if __name__ == '__main__':
    app.run()
