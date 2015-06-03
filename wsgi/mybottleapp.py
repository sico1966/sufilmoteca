from bottle import route, default_app

@route('/name/<name>')
def nameindex(name='Stranger'):
    return '<strong>Hola, %s!</strong>' % name
 
@route('/')
def index():
    return '<strong>Hello World!</strong>'

@route('/lista') # creamos una linea por cada informacion que saquemos del json
def lista():
	dicc={'pry_release_date.gte':'2014-09-15','primary_release_date.lte':'2014-10-22','api_key':'949149f8a7d1fe0fa6ac3eb641d11aae'}
	url_base="http://api.themoviedb.org/3/"
	r = requests.get(url_base+'discover/movie',params=dicc)
	j=r.json()
	lista=[]
	for peli in j["results"]: # recorre las peliculas
		lista.append(peli["title"]) # añade los titulos a lista que estaba vacia

	return template("fichero.tpl", listado=lista) #retorna la lista

# This must be added in order to do correct path lookups for the views
import os
from bottle import TEMPLATE_PATH
TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi/views/')) 

application=default_app()


