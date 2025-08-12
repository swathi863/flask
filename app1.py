from flask import *
app=Flask(__name__)
@app.route('/admin')
def admin():
    return "This is admin!"
@app.route('/student')
def student():
    return "This is student!"
@app.route('/staff')
def staff():
    return "This is staff!"
@app.route('/users/<name>')
def users(name):
    if name==admin:
        return redirect(url_for('admin'))
    if name==student:
        return redirect(url_for('student'))
    if name==staff:
        return redirect(url_for('staff'))
if __name__=="__main__":
    app.run(debug=True)