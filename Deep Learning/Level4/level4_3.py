if '__file__' in globals():
    import os, sys
    print('__file__ in globals at level4_3.py')
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


import myPackage.functions as F
import myPackage.layers as L
from myPackage import Layer


model = Layer()
model.l1 = L.Linear(5) # 출력 크기 지정
model.l2 = L.Linear(3)

# 추론
def predict(model, x):
    y = model.l1(x)
    y = F.sigmoid(y)
    y = model.l2(y)
    return y

# 모든 매개변수에 접근
for p in model.params():
    print(p)

print(model.__dict__)

# 모든 매개변수의 기울기 재설정
model.cleargrads()

