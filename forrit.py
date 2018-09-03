#Höfundur: Huginn Þór Jóhannsson
from bottle import route, run, template
from sys import argv
def index('/'):
    return """
    <h2>Verkefni 1.</h2>
    <a href="/about">Um okkur</a>
    <a href="/bio">Ferilskrár</a>
    <a href="/pics">Myndir</a>
    """

@route('/about')
def about():
    return "<h1>Testing About</h1>"

@route('/bio')
def bio():
    return "Testing Bio"

@route('/pics')
def testing():
    return "Testing Pics"
run(host="0.0.0.0",port=argv[1],debug=True)
