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


class TConfBase():
    DEBUG = True
    SECRET_KEY = os.environ.get('eSECRET_KEY', 'APPKEY' + str(os.urandom(12)))
    SQLALCHEMY_DATABASE_URI = os.environ.get('eDATABASE_URL', 'sqlite:///' + os.path.join(BaseDir, 'App.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PORT      = os.environ.get('ePORT', CMD.port)
    RECORDS   = os.environ.get('eRECORDS', CMD.records)
    MAIN_PAGE = os.environ.get('eMAIN_PAGE')


class TConfRelease(TConfBase):
    DEBUG = False

class TConfDebug(TConfBase):
    pass
