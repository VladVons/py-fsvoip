# Created: 22.09.2016
# Vladimir Vons, VladVons@gmail.com

import os
import optparse
from flask import Flask, request, current_app, send_from_directory, url_for
from flask_login import LoginManager
#
import Forms

App = Flask(__name__, template_folder='Templates', static_folder='Static')

login_manager = LoginManager()
login_manager.init_app(App)

@login_manager.user_loader
def load_user(aId):
    print('---1')
#    return User.query.get(int(aId))
    return 10


'''
@App.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if (endpoint == 'static'):
        filename = values.get('filename', None)
        if (filename):
            file_path = os.path.join(App.root_path, endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)
'''

@App.route('/Download/<path:aFileName>', methods=['GET', 'POST'])
def rDownload(aFileName):
    Dir = current_app.root_path + '/Download'
    print('----2', Dir, aFileName)
    #uploads = os.path.join(current_app.root_path, App.config['UPLOAD_FOLDER'])
    return send_from_directory(directory=Dir, filename=aFileName)


@App.route('/<aName>', methods=["POST", "GET"])
def rRootHandler(aName):
    NotFound = Forms.TFNotFound(request.form)
    Arr = {
    'index'   : Forms.TFIndex(request.form),
    'login'   : Forms.TFLogin(request.form),
    'search'  : Forms.TFSearch(request.form),
    'version' : Forms.TFVersion(request.form)
    }
    Form = Arr.get(aName, NotFound)
    return Form.Render()


@App.route('/')
def rRoot():
    #return rRootHandler('index')
    return rRootHandler('search')



class TMain():
    def GetCommandLine(self):
        Usage = 'usage: %prog [options]'
        Parser = optparse.OptionParser(usage = Usage)
        Parser.add_option('-p', '--port',     default = 8800, help = 'port number')
        Parser.add_option('-d', '--records',  default = './Download/call', help = 'mode')
        Result, Args = Parser.parse_args()
        return Result

    def Run(self):
        Cmd = self.GetCommandLine()
        print("Start main on port %s" % (Cmd.port))
        #App.config.from_object(Cmd)
        App.config['RECORDS'] = Cmd.records
        App.secret_key = "Vlad_" + str(os.urandom(12))
        App.run(host = '0.0.0.0', port = Cmd.port, debug = True)
