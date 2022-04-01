from flask import Flask,render_template,request,redirect
import os
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/main')
def main():
    return render_template('method.html')

@app.route('/user/<username>') # 변수값을 받는법
def show_user(username):
    return username+"!!!"

@app.route('/user/<username>/<int:age>') # 변수깂빋는데 형식지정해서
def show_user_age(username,age):
    return username+"!!!"+str(age+100)

# request object
# Form(post, 딕셔너리형태일때 사용), args(get방식,?뒤에있는값), files, method(post냐 get이냐 체크할때)

# method[] 안에 받을형식 적으면 됨
@app.route("/method",methods=['GET','POST'])
def method_test():
    if request.method=="POST":
        #data=
        return render_template('show_result.html',data=request.form)
    else:
        #data=request.args
        return render_template('show_result.html',data=request.args)

@app.route('/upload',methods=['GET','POST'])
def upload():
    if request.method=="GET":
        return render_template("fileup.html")
    else:
        f=request.files['file']
        path=os.path.dirname(__file__)+'/upload/'+f.filename
        f.save(path)
        print(path)
        return redirect('/')
if __name__=='__main__':
    app.run(debug=True,port=80)
