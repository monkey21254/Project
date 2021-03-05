# sys.path를 점검한 후 __file__ 에 해당되는 현재 파일의 디렉토리를 기준으로
# 하위 목록의 경로를 sys.path에 추가하는 작업을 수행한다.
if '__file__' in globals():
    import os, sys
    print('__file__ in globals') # __file__ : d:\python\step\level2.py
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import numpy as np
from myPackage import Variable
from myPackage.utils import get_dot_graph

x0 = Variable(np.array(1.))
x1 = Variable(np.array(1.))
y = x0 + x1

# 변수 이름 지정 - DOT 언어를 사용할 때 노드에 레이블(이름)을 달아주기 위해 수행
x0.name = 'x0'
x1.name = 'x1'
y.name = 'y'

txt = get_dot_graph(y, verbose=False)
print(txt)

# dot 파일로 저장
with open('sample.dot', 'w') as o:
    o.write(txt)
