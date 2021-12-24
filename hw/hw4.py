from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.uriMall                      # 'likelion'라는 이름의 db를 만듭니다.

@app.route('/')
def home():
    return render_template('hw4_onePageMall.html')

## API 역할을 하는 부분
@app.route('/orders', methods=['POST'])
def write_orders():
    cusName_receive = request.form['customer_name_g']
    numOrder_receive = request.form['num_order_g']
    cusAdd_receive = request.form['customer_add_g']
    cusPhone_receive = request.form['customer_phone_g']

    order= {
        'name':cusName_receive,
        'numberOforders':numOrder_receive,
        'address':cusAdd_receive,
        'phoneNumber': cusPhone_receive
    }

    db.uriMall.insert_one(order)

    return jsonify({'result':'success', 'msg': '이 요청은 POST!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=4444, debug=True)