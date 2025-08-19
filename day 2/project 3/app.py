from flask import Flask,redirect,url_for, request

app=Flask(__name__)

@app.route('/success/<name>/<age>')
def success(name,age):
    return f'your name is {name} and your age is {age}'
   

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method=='POST':
        name = request.form['nm']
        age = request.form['age']
        return redirect(url_for('success',name=name,age=age))
    
    else:
        name = request.args.form['nm']
        age = request.args.form['age']
        return redirect(url_for('success',name=name,age=age))
    

if __name__=='__main__':
    app.run(debug=True)