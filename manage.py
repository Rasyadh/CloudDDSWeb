import os

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from project import app
from project.core import db, encrypt
from project.models import User

migrate = Migrate(app,db)
manager = Manager(app)

manager.add_command('db',MigrateCommand)

@manager.command
def createdb():
	db.create_all()

@manager.command
def create_admin():
	admin = User(name = 'Admin', email='admin@telkom.co.id',password=encrypt.generate_password_hash("admintelkom"), status=1, nomorhp="081234567", role=1)
	db.session.add(admin)
	db.session.commit()

@manager.command
def create_user():
	user = User(name = 'User Biasa', email='user@telkom.co.id',password=encrypt.generate_password_hash("usertelkom"),status=1,nomorhp="0812691299")
	db.session.add(user)
	db.session.commit()



if __name__ == '__main__':
	manager.run()
