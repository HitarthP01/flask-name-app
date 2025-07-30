# from flask import Flask, request, render_template_string

# app = Flask(__name__)

# form_template = '''
# <form method = "POST" action ="/greet">
#     <label for="name"> Enter your name: </label>
#     <input type ="text" name ="name" id ="name">
#     <input submit ="submit" value = "Submit">
# </form>
# '''

# greet_template ='''
# <h1>Hello, {{ name }}!</h1>
# <a href = "/"> Go back </a>
# '''

# @app.route('/',methods = ['GET'])
# def home():
#     return render_template_string(form_template)

# @app.route('/greet', methods = ['POST'])
# def greet():
#     name = request.form['name']
#     return render_template_string(greet_template,name = name)

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, request, render_template_string

app = Flask(__name__)

form_template = '''
<form method="POST" action="/greet">
    <label for="name">Enter your name:</label>
    <input type="text" name="name" id="name">
    <input type="submit" value="Submit">
</form>
'''

greet_template = '''
<h1>Hello, {{ name }}!</h1>
<a href="/">Go back</a>
'''

@app.route('/', methods=['GET'])
def home():
    return render_template_string(form_template)

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form['name']
    return render_template_string(greet_template, name=name)

if __name__ == '__main__':
    app.run(debug=True)