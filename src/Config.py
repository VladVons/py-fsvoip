import os
import optparse


def GetCommandLine():
    Usage = 'usage: %prog [options]'
    Parser = optparse.OptionParser(usage = Usage)
    Parser.add_option('-p', '--port',     default = 8800, help = 'port number')
    Parser.add_option('-d', '--records',  default = './Download/call', help = 'mode')
    Result, Args = Parser.parse_args()
    return Result

BaseDir = os.path.abspath(os.path.dirname(__file__))
CMD = GetCommandLine()

class TConfig():
    SECRET_KEY = os.environ.get('SECRET_KEY', 'SECRET_KEY_NONE')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///' + os.path.join(BaseDir, 'App.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PORT = os.environ.get('PORT', CMD.port)
    RECORDS = os.environ.get('RECORDS', CMD.records)
