from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime

from config import postgresqlConfig
import csv

app = Flask(__name__)

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
    def add_screenshot(_id, _app_id, _file_name, _created_at, _updated_at):
        new_ss = Screenshot(id=_id, app_id=_app_id, file_name=_file_name, created_at=_created_at, updated_at=_updated_at)
        db.session.add(new_ss)
        db.session.commit()


def create_database():
    db.create_all()


create_database()


def read_app_file(filename):
    with open("{}".format(filename)) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        isAppFile = True
        for row in csv_reader:
            if line_count == 0:
                print(row)
                if 'app_id' in row:
                    isAppFile = False
                line_count += 1
            else:
                if isAppFile:
                    App.add_app(row[0], row[1], row[2], row[3], row[4])
                else:
                    Screenshot.add_screenshot(row[0],row[1], row[2], row[3], row[4])
                line_count += 1


read_app_file("static/sample_apps.csv")

read_app_file("static/sample_screeshots.csv")


if __name__ == '__main__':
    app.run()
