from flask import *
'''
app = Flask(__name__)

@app.route("/hello/<name>")
def home(name):
    return "These is:"+name

if __name__ == "__main__":
    app.run(debug=True)
'''
'''
app=Flask(__name__)
#@app.route('/')
@app.route('/user/<name>')   #delimiter
def message(name):
    #return render_template('base.html')
    return render_template('base.html',name=name)
if __name__=="__main__":
    app.run(debug=True)
'''

'''
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('base.html')

if __name__ == "__main__":
    app.run(debug=True)
'''