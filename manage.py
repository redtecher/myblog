from flask_script import Manager,Server,Shell
from flask_migrate import Migrate,MigrateCommand
from config import DevConfig
from webapp.models import User,Post,Tag
from webapp import db
from webapp import create_app
app = create_app(DevConfig)
migrate = Migrate(app,db)
manager = Manager(app)



@manager.shell
def make_shell_context():
    return dict(app=app,db=db,User=User,Post = Post,Tag=Tag)
manager.add_command("shell",Shell(make_context=make_shell_context))
manager.add_command("runserver",Server())
manager.add_command('db',MigrateCommand)




if __name__=='__main__':
    manager.run()