from flask import Flask,render_template,request,redirect
import os,pickle
from PIL import Image
import numpy as np
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

@app.route('/mnist',methods=['GET','POST'])
def mnist():
    if request.method=='GET':
        return render_template('mnistform.html')
    else:
        f=request.files['filename']
        path=os.path.dirname(__file__)+'/static/upload/'+f.filename
        f.save(path)

        img=Image.open(path).convert('L')# 흑백으로 변형
        img = np.resize(img,(1,784))
        img=255-(img)
        path='/static/upload/'+f.filename
        modelpath='model.pkl'
        model=''
        f=open(modelpath,'rb')
        model=pickle.load(f)
        pred=model.predict(img)
        print(pred)
        f.close()
        return render_template('mnistresult.html',data=[pred[0],path])


if __name__=='__main__':
    app.run(debug=True,port=80)
