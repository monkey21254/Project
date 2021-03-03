import base64
import random
import requests
from bson import ObjectId, SON
from flask import Flask, render_template, request, session, redirect
from pymongo import MongoClient, GEOSPHERE  # MongoDB 와 연동가능
from datetime import datetime

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

global check_root
####################################
check_root = 0  # atlas(1), local(2) / 초기 상태 (0)
####################################

global file_list
file_list = []
filename = 'atlas_connect_info.txt'
with open(filename, encoding='utf-8') as f:
    while True:
        line = f.readline()
        if not line: break
        file_list.append(line)
        file_list = list(tuple(file_list))
        if line.find('atlas') == 0:
            atlas_login_info = line[6:]
root_login = atlas_login_info

filename2 = 'local_connect_info.txt'
with open(filename2, encoding='utf-8') as f:
    while True:
        line = f.readline()
        if not line: break
        file_list.append(line)
        file_list = list(tuple(file_list))
        if line.find('host') == 0:
            local_login_info = line[5:]
            local_value1, local_value2 = local_login_info.split(sep=':')


class MyMongoClient(object):
    def __init__(self, database='bookstore', collection='books'):
        if check_root == 0: # 초기 상태
            self.client = MongoClient()
            self.database = self.client['bookstore_login']
            self.collection = self.database['users']
        elif check_root == 1: # Atlas 로그인
            self.root_login = root_login
            self.client = MongoClient(self.root_login)
            self.database = self.client[database]
            self.collection = self.database[collection]
        elif check_root == 2: # 로컬 로그인
            self.client = MongoClient()
            self.database = self.client[database]
            self.collection = self.database[collection]

    def get_collection(self):
        return self.collection

    def set_collection(self, collection):
        self.collection = collection


@app.route('/atlas_connect_info')
def atlas_connect_info():
    return render_template('atlas_connect_info.html',
                           login_info=root_login,
                           value1=local_value1, value2=local_value2)


@app.route('/atlas_connect_info_update', methods=['POST'])
def atlas_connect_info_update():
    global check_root, file_list

    login_dict = {key:item for key, item in request.form.items()}
    for item in file_list:
        if 'atlas' in item:
            print(True)

    if login_dict['customRadio'] == 'radio1':
        edit_result = "Atlas 접속 완료"
        check_root = 1
        for item in file_list:
            if 'atlas' in item:
                with open('atlas_connect_info.txt', 'w') as f:
                    f.write('atlas=' + login_dict['atlas_data'] + '\n')
    elif login_dict['customRadio'] == 'radio2':
        edit_result = "로컬 접속 완료"
        check_root = 2
        for item in file_list:
            if 'atlas' in item:
                with open('local_connect_info.txt', 'w') as f:
                    f.write('host=' + login_dict['local_data1'] + ':' + login_dict['local_data2'] + '\n')
    else:
        edit_result = "접속 불가"

    return render_template('atlas_edit_result.html',
                           edit_result=edit_result)


@app.route('/')
def homepage():
    name = 'Homepage'

    if 'username' in session:
        message = "로그인 되었습니다."
    else:
        message = "로그인이 필요합니다."

    city = 'daegu'
    city_upper = city.upper()
    app_id = 'c10e58684c8fc21d6771342fe25e50fe'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={app_id}'
    res = requests.get(url)
    weather_data = res.json()

    description = weather_data["weather"][0]['description']
    description_upper = description.upper()
    icon = weather_data["weather"][0]['icon']
    temp = round(weather_data["main"]["temp"] - 273, 1)

    return render_template('index.html', name=name, message=message,
                           city=city_upper,
                           temp=temp, icon=icon,
                           description=description_upper)


@app.route('/login', methods=['GET', 'POST'])
def login():
    global check_root
    if request.method == 'GET':
        return render_template('login.html')
    else:
        print('--------- LOGIN POST ---------')
        username = request.form['username']
        password = request.form['password']
        print('User name:', username)
        myclient = MyMongoClient('bookstore', 'users')
        user = myclient.get_collection().find_one({'username': username, 'password': password})

        if user:
            session['username'] = user['username']
            print('Match user:', user)
        else:
            print("로그인 오류")
            return render_template('error.html', id="아이디 또는 비밀번호가 잘못되었습니다.")

        return redirect('/')


@app.route('/logout')
def logout():
    session.pop('username', None) #
    return redirect('/')


# 표시 용도
@app.route('/book_add', methods=['GET'])
def add_book():
    return render_template('book_add.html')


# 데이터를 받아서 MongoDB에 넣을 것
@app.route('/book_add_process', methods=['POST'])
def add_book_process():
    myClient = MyMongoClient()

    title = request.form['title']
    file = request.files['file']
    encoded_data = base64.b64encode(file.read())
    author = request.form['author']
    price = request.form['price']
    isbn = request.form['isbn']

    bookJson = {'title': title, 'encoded_data': encoded_data,
                'author': author, 'price': price,
                'created_date': datetime.now()}
    # 데이터가 없을 경우 NULL값을 반환
    # result = collection.insert_one(bookJson)
    result = myClient.get_collection().insert_one(bookJson)
    print(result.inserted_id)

    if result.inserted_id:
        book_add_result = '정상 등록'
    else:
        book_add_result = '등록 실패'

    return render_template('book_add_result.html',
                           book_add_result=book_add_result)


@app.route('/book_id_search', methods=['GET'])
def book_id_search():
    return render_template('book_id_search.html')


@app.route('/book_id_search_process', methods=['POST'])
def book_id_search_process():
    # 로컬 접속
    # client = MongoClient("mongodb://localhost:27017/")

    client = MyMongoClient()
    database = client["song-db"]
    collection = database['books']
    _id = request.form['id']

    query = {'_id': ObjectId(_id)} # 60063b57dbd7318b45a4b092
    doc = collection.find_one(query)
    title = doc['title'] # 테스트입니다. <- 출력
    encoded_data = doc['encoded_data'].decode('utf-8')

    img_src_data = f"data:image/png;base64,{encoded_data}"
    # print(encoded_data)

    author = doc['author']
    price = doc['price']

    return render_template('book_id_search_result.html',
                           title=title, author=author,
                           price=price, img_src_data=img_src_data)


@app.route('/book_search', methods=['GET'])
def book_search():
    return render_template('book_search.html')


@app.route('/book_search_process', methods=['POST'])
def book_search_process():
    item = request.form['item_to_search']
    data = request.form['data_to_search']

    client = MyMongoClient()
    cursor = client.get_collection().find()
    cur_count = 0
    query = None

    for cur in cursor:
        if item == 'id' and ObjectId(data) == cur['_id']:
            query = {'_id': ObjectId(data)}
        elif item == 'title' and data == cur['title']:
            query = {'title': data}
        elif item == 'author' and data == cur['author']:
            query = {'author': data}
        elif item == 'price' and data == cur['price']:
            query = {'price': data}
        else:
            continue

    if query is None:
        return render_template('error.html')
    cursor = client.get_collection().find(query)
    cursor_list = []
    for cur in cursor:
        cursor_list.append(cur)
        cur_count += 1

    return render_template('book_search_result.html', cursor_list=cursor_list)


@app.route('/pharmacy_search', methods=['GET'])
def pharmacy_search():
    if check_root != 2:
        return render_template('error.html', id="로컬이 아닌 잘못된 접근입니다.")

    client = MyMongoClient("kim_db", "pharmacy")
    client2 = MyMongoClient("kim_db", "modify_pharmacy")
    modify_pharmacy = client2.get_collection()
    cursor = client.get_collection().find()
    for cur in cursor:
        if cur.get('경도') == None:
            continue
        phar_loc = {'type': 'Point'}
        phar_loc['coordinates'] = [float(cur.get('경도')), float(cur.get('위도'))]
        bookJson = {'pharmacyName': cur.get('약국명'), 'location': phar_loc}
        modify_pharmacy.insert_one(bookJson)
    modify_pharmacy.create_index([('location', GEOSPHERE)])
    query = {'location': {'$near': SON([('$geometry', SON([ ('type', 'Point'), ('coordinates', [128.62707, 35.88107]) ])),
                                   ('$maxDistance', 1000)])}}
    pharmacy = modify_pharmacy.find(query)

    return render_template('hkit_pharmacy.html', pharmacy=pharmacy)


@app.route('/jiji', methods=['GET', 'POST'])
def jiji():
    if request.method == 'POST':
        year = request.form['year']
        year = int(year)
        jiji_list = ['자', '축', '인', '묘', '진', '사', '오', '미', '신', '유', '술', '해']
        jiji_index = (year - 4) % 12
        myjiji = jiji_list[jiji_index]

        return render_template('jiji.html', myjiji=myjiji)
    else:
        return render_template('jiji.html', myjiji=None)


@app.route('/game', methods=['GET'])
def game():
    card = ['1-1', '1-2', '2-1', '2-2', '3-1', '3-2', '4-1', '4-2','5-1', '5-2', '6-1',
            '6-2','7-1', '7-2', '8-1', '8-2', '9-1', '9-2', '10-1', '10-2']

    random.shuffle(card)
    print(card)
    card_index = [item.find('-') for item in card]
    card_list = [int(item[:index]) for item, index in zip(card, card_index)]
    shuffled_card = card[:2]
    shuffled_card2 = card[2:4]
    print(shuffled_card, shuffled_card2)
    card_number = sum(card_list[:2]) % 10
    card_number2 = sum(card_list[2:4]) % 10
    print(card_number, card_number2)
    if card_number > card_number2:
        game_result = "I'm win"
    elif card_number < card_number2:
        game_result = "I'm lose"
    else:
        game_result = "Draw"

    return render_template('game.html', shuffled_card=shuffled_card,
                           shuffled_card2=shuffled_card2, game_result=game_result)


@app.route('/book_list', methods=['GET'])
def book_list():
    # client = MongoClient()
    # database = client['song-db']
    # collection = database['books']

    myClient = MyMongoClient()
    collection = myClient.get_collection()
    test = collection.find()
    print(test)
    count = collection.find().count()
    print('count:', count)

    # Cursor: 가져온 레코드의 집합
    cursor = collection.find() # return-type: class 'Cursor'
    book = []
    for cur in cursor:
        if cur.get('encoded_data'):
            decoded_data = cur['encoded_data'].decode('utf-8')
            image_src_data = f"data:image/png;base64,{decoded_data}"
            cur['encoded_data'] = image_src_data
            book.append(cur)
        else:
            cur['encoded_data'] = None
            book.append(cur)

    cursor = collection.find()
    return render_template('book_list.html',
                           cursor=cursor,
                           book=book,
                           count=count)


@app.route('/book_details/<_id>')
def book_details(_id=None):
    client = MyMongoClient()
    cursor = client.get_collection().find({'_id': ObjectId(f'{_id}')})
    for temp in cursor:
        title_data = temp.get('title')
        image_data = temp.get('encoded_data')
        if image_data is None:
            image_data = "None"
    return render_template('book_details.html', id=title_data, image_data=image_data)


@app.route('/book_edit/<_id>')
def edit_book(_id=None):
    return render_template('book_edit.html', id=_id)


@app.route('/book_edit_process', methods=['POST'])
def edit_book_process():
    client = MyMongoClient()

    to_edit_id = request.form['edit_id']
    cursor = client.get_collection().find({'_id': ObjectId(f'{to_edit_id}')})
    for temp in cursor:
        to_update_data = temp # class 'dict'

    title = request.form['title']
    file = request.files['file']
    encoded_data = base64.b64encode(file.read())
    author = request.form['author']
    price = request.form['price']

    bookJson = {'_id': ObjectId(f'{to_edit_id}'), 'title': title,
                'encoded_data': encoded_data, 'author': author,
                'price': price, 'created_date': datetime.now()} # class 'dict'

    result = client.get_collection().update(to_update_data, bookJson,
                                            upsert=True)
    print("result:", result)

    if result:
        book_edit_result = '수정 완료'
    else:
        book_edit_result = '수정 실패'

    return render_template('book_edit_result.html',
                           book_edit_result=book_edit_result)


@app.route('/book_remove/<_id>')
def remove_book(_id=None):
    client = MyMongoClient()
    test = client.get_collection().remove({'_id': ObjectId(f'{_id}')})

    if test:
        book_remove_result = '삭제 완료'
    else:
        book_remove_result = '삭제 실패'

    return render_template('book_remove.html', book_remove_result=book_remove_result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9900) # 211.54.173.40:9900
