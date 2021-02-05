# YOLO를 통한 가위바위보 판정 프로그램
- 프로젝트명: RSP (Rock Scissors Paper)
- 참여기간: 2020.12.28 ~ 2020.12.31 (4일)
- 참여인원: 3명 (김기영, 옥진해, 전고은)
- 역할:
- 프로젝트 세부내용
    - 가위, 바위, 보 이미지의 직접적인 Labeling을 통한 이미지 데이터 학습
    - 학습 결과을 이용한 Webcam으로 가위바위보 판정
        - 1인일 경우 : 가위, 바위, 보 3가지 중 어떤 것인지 출력
        - 2인 이상일 경우 : 가위, 바위, 보 3가지 중 어떤 것인지 출력, 승패 확인
- 사용언어 및 버전 : Python 3.9.1
- 사용툴: Vscode, Google Colab
- 라이브러리
    - Numpy 1.18.5
    - OpenCV 4.3.0
    - Yolo v3

## Files
### GameCustomYolo.ipynb
    Yolo을 이용하여 이미지 데이터 학습을 할 수 있는 과정이 있습니다.
    이번 학습은 Google Colab에서 이루어졌습니다.

### yolo_custom_RSP_video.py
    OpenCV(DNN), Yolo v3(Darknet), Webcam을 활용하여 학습된 가위바위보 모델을 검증하여 출력해주는 코드입니다.
    - 준비물 : Webcam

## Directory
### data
- 이미지 파일(.jpg) : 102장
- 이미지 라벨링 파일(.txt) : 102개

### model
- classes.names : 검출 해야할 물체의 종류
    - Rock
    - Paper
    - Scissors
- custom_data.data : classes, train, valid, names, backup의 경로 지정
- custom-train-yolo.cfg : 경우에 따른 max_batches와 steps, filers
    경우에 따라 아래의 내용을 수정할 필요가 있습니다.
    - max_batches = classes * 2000
    - steps = max_batches * 0.8, max_batches * 0.9
    - filters = (classes + coordinates + 1) * masks
        * coordinates : 4 (center x, center y, width, height)
        * mask : 3 ( color : r, g, b)
- test.txt : test 데이터 지정
- train.txt : train 데이터 지정

## Demo
[YOLO를 통한 가위바위보 학습 - 1인의 경우](https://youtu.be/Efdvvv-RvF0)  
[YOLO를 통한 가위바위보 학습 - 2인의 경우](https://youtu.be/x7iqZd_DmKQ)  
[YOLO를 통한 가위바위보 학습 - 3인 이상의 경우](https://youtu.be/87-4rrAkaCc)  