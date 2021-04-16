from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)


# herencia html
@app.route('/')
def index():
    name = 'Gerson'
    return render_template('index.html', name=name)


@app.route('/client')
def client():
    list_name = ['Client1', 'Cliente2', 'Client3']
    return render_template('client.html', list=list_name)


@app.route('/page/')
@app.route('/page/<name>')
def name(name='user'):
    return 'Hello {}'.format(name)


@app.route('/about')
def about():
    return 'About Us Page !'


@app.route("/p/<string:slug>/")
def show_post(slug):
    return "Mostrando el post {}".format(slug)


@app.route("/admin/post/")
@app.route("/admin/post/<int:post_id>/")
def post_form(post_id=None):
    return "post_form {}".format(post_id)


# redireccionamiento


@app.route('/Admin')
def hello_admin():
    return 'Hello Admin'


@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s as Guest' % guest


# @app.route('/user/<name>')
# def hello_user(name):
#     if name == 'admin':
#         return redirect(url_for('hello_admin'))
#     else:
#         return redirect(url_for('hello_guest', guest=name))


# Renderizado

@app.route('/user/<name>')
def user(name= 'Gerson'):
    age = 16
    my_list = [1, 2, 3, 4]
    my_car = {
        "brand": "Mazda",
        "model": "RX-7 Spirit R",
        "year": 2002
    }
    return render_template('user.html', user_name=name, age=age, list=my_list, car=my_car)


# parametros
@app.route('/params')
def params():
    # si tiene algun parametro llamado params1 se obtiene el valor
    # numero de parametros puede ser indefinido
    # http://127.0.0.1:5000/params?params1=Gerson&params2=parametrodos
    param = request.args.get('params1', 'no contiene parametros')
    param_dos = request.args.get('params2', 'no contiene parametros')
    return 'El parametro es : {}, {}'.format(param, param_dos)


if __name__ == '__main__':
    app.run(debug=True)
