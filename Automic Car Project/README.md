# Raspberry pi 4 & Android Studio를 활용한 수동, 반자동 자동차 제작
- 프로젝트명: Automic
- 참여기간: 2020.10.28 ~ 2020.11.25
- 참여인원: 3명 (김기영, 김채진, 서강원, 옥진해, 전고은)
- Workflow: 아이디어 구상, 자동차 Kit 구매 및 제작, 어플리케이션 개발, 이미지 프로세싱 및 소켓 통신(UDP, Wi-Fi), PPT 제작
- 프로젝트 세부내용
    - Kit를 조립하고 Raspberry Pi와 결합하여 자동차 제작
    - 자동차를 교차로에서 원하는 지점으로 지정하여 자동 운행이 가능하도록 하는 기능 탑재
	- 조이스틱을 만들어 수동으로 운행가능하도록 기능 추가
    - Wi-Fi 및 소켓 통신(UDP)을 통해 어플리케이션 화면 내부에 Raspberry 자동차에 연결된 Webcam 화면과 연동
	- 이미지 프로세싱을 통해 교차점 측정 및 좌우를 인식하는 어플리케이션 개발
    - 제작된 틀을 토대로 PPT 제작
- 사용 기기 : Raspberry Pi 4
	- OS : Raspbian, Python IDE
- 사용언어 및 버전 : Python 3.8.5
- 사용툴: VS Code, Android Studio(Java)
- 라이브러리
	- RPi.GPIO
    - Numpy 1.18.5
    - OpenCV 4.3.0

## Files
### AutomicCar  
    Android Studio (Java Base) files 

### Raspberry pi 3, 4
	- Raspberry Pi 내부에 사용된 Python 파일 포함 Directory
#### CARControl.py, CARControl_UDP.py, CARControl_UDP_ver2.py
	- 자동차 키트 운행에 필요한 모듈
    - CARControl, CARControl_UDP : 최초 제작 파일 및 1차 수정 파일
	- CARControl_DUP_ver2 : 최종 파일

#### CARServer.py, CARServer_UDP.py, CARServer_UDP_ver2.py
	- Raspberry Pi 및 Android 어플리케이션 간 Wi-Fi 통신 수행 py file
	- CARServer, CARServer_UDP : 최초 제작 파일 및 1차 수정 파일
	- CARServer_UDP_ver2 : 최종 파일이자 작업을 수행하는 메인 파일

#### follow_line.py
	- Line Tracking을 수행하는 모듈
	- 교차로 카운팅 및 좌우 판별하여 자동 운행

### PPT(PDF)
	+[Automic Car 최종.pdf 바로가기](https://github.com/monkey21254/Project/blob/main/Automic%20Car%20Project/Automic.Car.pdf)    
	+[Automic Car 최종.pdf [Download]](https://github.com/monkey21254/Project/files/6018952/Automic.Car.pdf)
