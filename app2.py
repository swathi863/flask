from flask import *
'''
app = Flask(__name__)

@app.route("/hello/<int:nam>")
def home(nam):
    return "These number  %d" %nam

if __name__ == "__main__":
    app.run(debug=True)
'''

'''
app=Flask(__name__)
@app.route('/login',methods=['GET'])
def login():
    uname=request.args.get('uname')
    passwrd=request.args.get('pass')
    if uname=='swathi' and passwrd=="1234567890":
        return "Welcome %s"%uname
    else:
        return "invalid %s"%uname
if __name__=="__main__":
    app.run(debug=True)
'''
app=Flask(__name__)
@app.route('/login',methods=['POST'])
def login():
    uname=request.form['uname']
    passwrd=request.form['pass']
    if uname=='swathi' and passwrd=="1234567890":
        return "Welcome %s"%uname
    else:
        return "invalid %s"%uname
if __name__=="__main__":
    app.run(debug=True)