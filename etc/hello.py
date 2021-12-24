
import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.likelion    

# 타겟 URL을 읽어서 HTML를 받아오고,
#headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
#data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
#soup = BeautifulSoup(data.text, 'html.parser')

#print(soup)
#old_content > table > tbody > tr:nth-child(2) > td.title > div > a #그린북의 주소

#movies = soup.select('#old_content > table > tbody > tr')
#print(movies)

# for movie in movies:
#     a_tag= movie.select_one('td.title > div> a')
#     if a_tag is not None:
#         rank = movie.select_one('td:nth-child(1) > img')['alt']
#         title = a_tag.text
#         star = movie.select_one('td.point').text
#         doc = {
#             'rank' : rank,
#             'title' : title,
#             'star' : star
#         }
#         db.movies.insert_one(doc)


# targetmovie= db.movies.find_one({'title':'매트릭스'})
# targetstar = targetmovie['star']

# movies = db.movies.find({'star':targetstar})

# for movie in movies:
#     print(movie['title'])

# db.movies.update_many({'star':targetstar}, {'$set':{'star':0}})

print(db.movies.find_one({'title':'매트릭스'})['star'])
        #print(rank, title , star)


# # 선택자를 사용하는 방법 (copy selector)
# soup.select('태그명')
# soup.select('.클래스명')
# soup.select('#아이디명')

# soup.select('상위태그명 > 하위태그명 > 하위태그명')
# soup.select('상위태그명.클래스명 > 하위태그명.클래스명')

# # 태그와 속성값으로 찾는 방법
# soup.select('태그명[속성="값"]')

# # 한 개만 가져오고 싶은 경우
# soup.select_one('위와 동일')

#old_content > table > tbody > tr:nth-child(2) > td.point
#old_content > table > tbody > tr:nth-child(2) > td:nth-child(1) > img

