# Created: 21.12.2018
# Vladimir Vons, VladVons@gmail.com


from flask import request, current_app, send_from_directory, redirect, url_for
from flask_login import logout_user, login_required
from App import app
#
import Forms


@app.route('/Download/<path:aFileName>', methods=['GET', 'POST'])
def rDownload(aFileName):
    Dir = current_app.root_path.replace('App', '') + '/Download'
    #uploads = os.path.join(current_app.root_path, App.config['UPLOAD_FOLDER'])
    return send_from_directory(directory=Dir, filename=aFileName)


@app.route('/login', methods=["POST", "GET"])
def login():
    #to prevent recursion @login_required dont use rRootHandler()
    Form = Forms.TFLogin(request.form)
    return Form.Render()


@app.route('/logout')
def rLogout():
    logout_user()
    return redirect('index')


@app.route('/<aName>', methods=["POST", "GET"])
#@login_required
def rRootHandler(aName):
    Arr = {
    'index'   : Forms.TFIndex(request.form),
    'user'    : Forms.TFUser(request.form),
    'search'  : Forms.TFSearch(request.form),
    'compare' : Forms.TFCompare(request.form),
    'version' : Forms.TFVersion(request.form)
    }

    NotFound = Forms.TFNotFound(request.form)
    Form = Arr.get(aName, NotFound)
    return Form.Render()


@app.route('/')
@app.route('/index')
def rRoot():
    Page = current_app.config.get('MAIN_PAGE')
    if (Page):
        return redirect(Page)
    else:
        Form = Forms.TFIndex(request.form)
        return Form.Render()
