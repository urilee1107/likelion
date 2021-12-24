from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.likelion                      # 'likelion'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분
@app.route('/reviews', methods=['POST'])
def write_review():
    title_receive = request.form['title_give']
    author_receive = request.form['author_give']
    review_receive = request.form['review_give']

    review= {
        'title':title_receive,
        'author':author_receive,
        'review':review_receive
    }

    db.review.insert_one(review)

    return jsonify({'result':'success', 'msg': '이 요청은 POST!'})

## DB에 있는 데이터를 불러오는 것
@app.route('/reviews', methods=['GET'])
def read_reviews():
    reviews = list(db.review.find({},{'_id':0}))
    return jsonify({'result':'success', 'msg': '이 요청은 GET!', 'reviews':reviews})


if __name__ == '__main__':
    app.run('0.0.0.0', port=4444, debug=True)