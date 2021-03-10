## Contents
### Repository 
#### Level2
+ Package_backup
	+ Level2 & Level3 일부 내용에 관한 package화 된 자료를 backup 해놓은 폴더
+ _***"210302(Level 2).ipynb"***_ : 교재를 보고 따라하면서 작성했던 2고지의 Jupyter Notebook 포맷 파일
+ log.png
	+ Level 2 과정 중 backprop 단계에서 generation 및 메모리 할당에 관한 부분을 확인했던 로그 이미지 파일

#### Level3
+ Level 3 (~Step 31).ipynb
	+ 3고지 Step 31까지 실제로 진행했던 Jupyter Notebook 파일 (31단계까지는 core_simple.py를 사용하여 기본적인 연산자 오버로딩에 대해서 다룸)
+ Level 3 (Step 32~).ipynb
	+ 3고지 Step 32부터 실제로 진행했던 Jupyter Notebook 파일 (32단계부터는 core_complex.py를 사용하여 core_simple의 기능에 추가적으로 고차 미분, 삼각함수를 추가하게 됨
+ .png & .dot
	+ 딥러닝책에서 요구하는 Graphviz 모듈을 활용하여 Node & Edge 를 시각화하는 작업을 수행하는데 그에 대한 결과물

#### Level4
+ Level 4.ipynb
	+ 4고지에서 요구하는 tensor의 역전파 수행, reshape, transpose, sum, 브로드캐스팅, 등을 패키지에 추가하게 되는데 그에 대한 변화과정을 작성한 Jupyter Notebook 파일

#### myPackage
+ __init__.py
	- 패키지임을 알리는 파일이자 core_simple.py & core_complex.py를 다른 경로의 파일에서 myPackage를 임포트함으로써 사용할 수 있도록 config 되어있는 파일
+ core_simple.py
	- 3고지의 Step 31까지 사용되었던 .py 파일
+ core_complex.py
	- 3고지의 Step 32부터 계속 사용하게되는 .py 파일 (계속 업데이트 과정이 이루어지고 있음), 연산자에 대한부분은 거의 변동이 없고 Variable or Function class의 변동이 있는 편.
+ functions.py
	- 삼각함수, reshape, transpose, broadcast 등 여러가지 기능이 추가되는 부분
+ utils.py
	- Graphviz나 이 패키지와 직접적인 관련은 없으나 기능의 추가를 위해서 불러들어야 하는 알고리즘 또는 함수에 대한 부분이 저장되어 있는 공간

#### 2. step
+ .ipynb로는 테스트가 어려운 부분에 대해서 .py 파일을 테스트용으로 사용하고 있는 디렉토리

### PDF (밑바닥부터 시작하는 딥러닝 3 (총 5개의 고지로 구성)
> #### ~2고지
+ 바로가기    
[밑바닥부터 시작하는 딥러닝 3 (~제 2고지).pdf](https://github.com/monkey21254/Project/blob/main/Deep%20Learning/%EB%B0%91%EB%B0%94%EB%8B%A5%EB%B6%80%ED%84%B0%20%EC%8B%9C%EC%9E%91%ED%95%98%EB%8A%94%20%EB%94%A5%EB%9F%AC%EB%8B%9D%203%20(~%EC%A0%9C%202%EA%B3%A0%EC%A7%80).pdf)    
+ 다운로드    
[밑바닥부터 시작하는 딥러닝 3 (~제 2고지).pdf](https://github.com/monkey21254/Project/files/6080416/3.2.pdf)    

> ~3고지
+ 바로가기
[밑바닥부터 시작하는 딥러닝 3 (~제 3고지).pdf](https://github.com/monkey21254/Project/blob/main/Deep%20Learning/%EB%B0%91%EB%B0%94%EB%8B%A5%EB%B6%80%ED%84%B0%20%EC%8B%9C%EC%9E%91%ED%95%98%EB%8A%94%20%EB%94%A5%EB%9F%AC%EB%8B%9D%203%20(~%EC%A0%9C%203%EA%B3%A0%EC%A7%80).pdf)
+ 다운로드
[밑바닥부터 시작하는 딥러닝 3 (~제 3고지).pdf](https://github.com/monkey21254/Project/files/6114049/3.3.pdf)
