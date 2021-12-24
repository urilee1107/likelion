from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient          
client = MongoClient('localhost', 27017)  
db = client.uriMall                      

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
        '이름':cusName_receive,
        '수량':numOrder_receive,
        '주소':cusAdd_receive,
        '전화번호': cusPhone_receive
    }

    db.uriMall.insert_one(order)

    return jsonify({'result':'success', 'msg': '이 요청은 POST!'})


## DB에 있는 데이터를 불러오는 것
@app.route('/orders', methods=['GET'])
def read_orders():
    orders = list(db.uriMall.find({},{'_id':0}))
    return jsonify({'result':'success', 'msg': '이 요청은 GET!', 'orders':orders})




if __name__ == '__main__':
    app.run('0.0.0.0', port=4444, debug=True)