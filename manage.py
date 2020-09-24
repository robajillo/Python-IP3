from app import create_app,db

from flask_script import Manager,Server
from  flask_migrate import Migrate, MigrateCommand
from app.models import User,Pitch,Comment

# Creating app instance
# app = create_app('development')
app = create_app('test')
app = create_app('production')

manager = Manager(app)
migrate = Migrate(app,db)
manager.add_command('server',Server)
manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User = User,Pitch=Pitch,Comment=Comment)

manager.add_command('server', Server)
@manager.command
def test():
    import unittest
    test = unittest.TestLoader().discover('test')
    unittest.TextTestRunner(verbosity=2).run(test)



if __name__ == '__main__':
    manager.run()