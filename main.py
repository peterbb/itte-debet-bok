import json, os
from bottle import request, route, get, put, static_file, post, delete, run, redirect

ROOT = os.path.join(os.getcwd(), "static")

account_uid = 2
account_db = {
    0 : {'name': "Peter Brottveit Bock",
         'saldo': 0,
         'history': []},
    1 : {'name': "Julia Batkiewicz",
         'saldo': 100,
         'history': []}
}


@get('/static/<filename:path>')
def get_static(filename):
    return static_file(filename, root=ROOT)

@get('/')
def index():
    redirect("static/index.html")

@get('/users')
@get('/users/')
def list_users():
    return { id : account['name'] for 
             id, account in account_db.iteritems() }

@get('/users/<id:int>')
@get('/users/<id:int>/')
def user_info(id):
    if id in account_db:
        return account_db[id]
    else:
        print "Request for non-existing user %s" % id
        return None

@post('/users')
@post('/users/')
def new_user():
    print "Add new user"
    pass

menu_uid = 2
menu_db = {
    0: ("Bayer", 35),
    1: ("Cola", 20)
    }

@get('/menu')
@get('/menu/')
def get_menu():
    return menu_db

@get('/menu/<id:int>')
@get('/menu/<id:int>/')
def get_menu_item(id):
    return menu_db[id]

@post('/menu')
@post('/menu/')
def new_menu_item():
    global menu_uid
    description = request.forms.get('description')
    price       = int(request.forms.get('price')) # XXX 
    menu_db[menu_uid] = (description, price)
    menu_uid += 1

@put('/menu/<id:int>')
@put('/menu/<id:int>/')
def update_menu_item(id):
    description = request.forms.get('description')
    price       = int(request.forms.get('price')) # XXX 
    menu_db[id] = (description, price)


@delete('/menu/<id:int>')
@delete('/menu/<id:int>/')
def delete_menu_item(id):
    del menu_db[id]


run(host="localhost", port=8080)
