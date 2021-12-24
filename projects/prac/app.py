
from flask import Flask, render_template, request
from flask.json import jsonify
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

#위에가 API의 한 단위이다. / 요청을 받으면 위에것이 시작이 된다.
#그래서 위의 url를 잘 활용을 해야하고, 중복되면 안된다.

@app.route('/mypage')
def mypage():
    return 'This is my pageeeee!'

@app.route('/test', methods=['POST'])
def test_post():
    title_receive= request.form['title_give']
    print(title_receive)
    return jsonify({'result':'success', 'msg':'이 요청은 POST입니다.'})



@app.route('/test', methods=['GET'])
def test_get():
    title_receive= request.args.get('title_give')
    print(title_receive)
    return jsonify({'result':'success', 'msg':'이 요청은 GET입니다.'})


if __name__ == '__main__':  
   app.run('0.0.0.0',port=4444,debug=True)
# port =5000이 보통 기본적인데, 이게 안되면, 일단 포트넘버를 바꿔서 해도 되긴 한다. 근데 아마 재부팅하면은 이전의 5000번이 죽고 
# 사용가능 할 것이다. 