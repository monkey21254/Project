
#### Homepage Main (이미지 블로그 링크 (https://monkey2125.tistory.com/264)
![homepage](https://user-images.githubusercontent.com/74335601/109770069-6c328980-7c3e-11eb-8b65-100e64bbc27e.png)

# MongoDB를 활용한 Database 구축 및 홈페이지 서버 관리
- 참여기간: 2021.01.14 ~ 2021.01.25 (12일)
- 참여인원: 1명 (김기영)
- Workflow: HTML + CSS를 활용하여 Local 홈페이지 서버 구축 → MongoDB Atlas를 활용하여 Cloud 서버 운영 및 데이터 CRUD
- 사용언어 및 버전 : Python 3.9.1
- 사용툴: Pycharm professional, MongoDB Atlas, MongoDB Compass, Studio 3T
- 기능
	+ 출생년도에 따른 띠 확인
	+ 컴퓨터와의 가상 미니 화투게임
	+ 도서 등록, 검색, 수정, 삭제 기능 추가
	+ 도서 전체 조회 기능 (Local 서버 및 Cloud 서버 간 이동에 따라 DB 내용 변동)
	+ 한국IT교육원의 위, 경도를 토대로 1km 내에 있는 약국 정보 및 위치 확인
	+ 로그인, 로그아웃 기능 추가
	+ Local 이나 Atlas 계정을 통해 다룰 DB 선택 가능
	+ 홈페이지 메인 화면에 실시간 시계 및 대구 날씨 표시
- 라이브러리
    - Flask 1.1.2
    - Jinja2 2.11.2
    - bson 0.5.10
	- dnspython 2.1.0
	- numpy 1.19.5
	- pip 20.3.3
	- pymongo 3.11.2
	- requests 2.25.1
	- setuptools 51.3.3
	- urllib3 1.26.2

## Directory
### homepage_image
    Homepage 결과 이미지 자료 일부가 보관된 directory

### static
    Local server 구축 초반 단계에 사용된 이미지 (화투패, 12간지)
	홈페이지 서버 내에서 error가 있는 경우 사용되는 이미지 (error.jpg)
	데이터베이스 이미지 등록 확인용 이미지들 (leaves, rose, tree - jpg)

### templates
	서버 구축에 사용된 html 문서 (총 21개)

### venv
	Pycharm 가상환경 설정 디렉토리

## files
### app.py
	main 함수 파일 (21개의 html 문서간 연결이 되어 있는 서버 구축의 중심이 되는 파일)

### atlas_connect_info.txt
	MongoDB Atlas 접속 시 필요한 내용이 담긴 text 파일
	
### backup.txt
	로컬 및 Cloud 접속에 대한 정보 백업 파일
	
### local_connect_info.txt
	Local을 통해 홈페이지 접속 시 필요한 ip 주소(현 localhost) 및 포트번호


## Image
#### DB(book) overall list
![book](https://user-images.githubusercontent.com/74335601/109770111-7ce2ff80-7c3e-11eb-9db1-1fddbd07c2d2.png)
#### DB create
![add_book](https://user-images.githubusercontent.com/74335601/109770137-84a2a400-7c3e-11eb-981b-d96b7ceed8ac.png)
#### Pharmacy info
![pharmacy](https://user-images.githubusercontent.com/74335601/109767963-9f274e00-7c3b-11eb-82d3-0aa5bcf8a00e.png)
