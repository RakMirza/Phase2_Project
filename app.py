from flask import Flask, render_template

app = Flask(__name__)           # a Flask object

@app.route('/')                 # called when visiting web URL 127.0.0.1:5000/hello
def index():
    print('*** DEBUG:  inside hello_world() ***')
    return '<PRE>Hello, World!</PRE>'            # expected to return a string (usu. the HTML to display)

@app.route('/about')                 # called when visiting web URL 127.0.0.1:5000/hello
def about():
    print(" Inside about ")
    return '<PRE>Hello, World!</PRE>'            # expected to return a string (usu. the HTML to display)
   

if __name__ == '__main__':
    app.run(debug=True, port=5000)    # app starts serving in debug mode on port 5000