#Höfundur: Huginn Þór Jóhannsson
from bottle import route, run, template

@route('/hi/<name>')
def hi(name="Name"):
    return template('Hello {{name}},how are you?', name=name)

@route('/')
def index():
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
run(host="localhost",port=8080,debug=True)
