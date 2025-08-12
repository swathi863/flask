from flask import *
app = Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
    res=""
    try:
        if request.method=='POST':
            Number1=float(request.form.get('Number1',0))
            Number2=float(request.form.get('Number2',0))
            operation=request.form.get("operation")
            if operation=="Add":
                res=Number1+Number2
            elif operation=="Sub":
                res=Number1-Number2
            elif operation=="Mul":
                res=Number1*Number2
            elif operation=="Div":
                res=Number1/Number2 if Number2!=0 else "Cannot divide by 0"
            elif operation=="FloorDiv":
                res=int(Number1//Number2) if Number2!=0 else "Cannot divide by 0"
            elif operation=="Mod":
                res=Number1%Number2 
            elif operation=="Pow":
                res=Number1**Number2 
        return render_template('calculator.html',res=res)
    except ValueError:
        res="Invalid Input:Please enter numbers only"

if __name__ == "__main__":
    app.run(debug=True)
