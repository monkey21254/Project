# myPackage/utils.py
if '__file__' in globals():
    import os, sys
    print('__file__ in globals at utils.py')
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import os
import subprocess
import numpy as np
from myPackage import cuda
from myPackage import Variable


# =============================================================================
# Visualize for computational graph
# =============================================================================
def _dot_var(v, verbose=False):
    """
    _dot_var : Local 형식으로 사용될 함수

    - 차후 get_dot_graph 함수 전용으로 사용 예정
    
    Parameter
    ---------
    v: Variable 객체를 의미
    dot_var : 노드(변수) id, label, color, style 의 총 4가지 양식에 따라서 노드를 그리기 위한 제작틀
    name : 인자 v의 name이 지정되어 있는 경우에는 그 이름을 그대로 활용하고 아닌 경우에는 None으로 대체
    verbose : Flag 역할을 하는 파라미터로 True일 경우 Varaible로 들어오는 x 파라미터에 대해 추가 정보를 제공

    Function
    --------
    id : 파이썬 기본 내장 함수(객체의 ID를 반환)
    """
    dot_var = '{} [label="{}", color=orange, style=filled]\n'

    name = '' if v.name is None else v.name
    if verbose and v.data is not None:
        if v.name is not None:
            name += ': '
        name += str(v.shape) + ' ' + str(v.dtype)
    return dot_var.format(id(v), name)

def _dot_func(f):
    """
    _dot_func: 함수와 입력 변수간의 관계 및 함수와 출력 변수간의 관계를 표현하는 함수
    
    Parameter
    ---------
    dot_func : 노드(함수) id, label, color, style 의 총 4가지 양식에 따라서 노드를 그리기 위한 제작틀
    txt : 최종적으로 DOT digraph에 들어가는 문자열
    dot_edge : txt에 들어가는 edge를 표현하는 제작틀
    """
    dot_func = '{} [label="{}", color=lightblue, style=filled, shape=box]\n'
    txt = dot_func.format(id(f), f.__class__.__name__)

    dot_edge = '{} -> {}\n'
    for x in f.inputs:
        txt += dot_edge.format(id(x), id(f))
    for y in f.outputs:
        txt += dot_edge.format(id(f), id(y()))
    return txt

def get_dot_graph(output, verbose=True):
    """
    get_dot_graph : 역전파 수행(backward)에서 사용했던 방식을 가져와서 노드형태로 구현하는 함수

    Parameter
    ---------
    output : 최종 결과물(y)를 의미
    txt : 최종적으로 출력될 결과물로써 노드(Variable 객체, 함수 객체) 정보를 포함하고 있음
    funcs : 함수 객체가 들어갈 리스트로 차후 연결된 모든 관계를 표현하기 위해 사용될 예정
    seen_set : 함수 객체의 중복 append를 방지하기 위해 set을 사용
    """
    txt = ''
    funcs = []
    seen_set = set()

    def add_func(f):
        if f not in seen_set:
            funcs.append(f)
            # funcs.sort(key=lambda x: x.generation) # update (주석처리), 역전파는 순서가 중요했으나 DOT 언어에서는 edge가 표시되므로 상관없음
            seen_set.add(f)

    add_func(output.creator)
    txt += _dot_var(output, verbose) # update

    while funcs:
        func = funcs.pop()
        txt += _dot_func(func) # update
        for x in func.inputs:
            txt += _dot_var(x, verbose) # update

            if x.creator is not None:
                add_func(x.creator)

    return 'digraph g {\n' + txt + '}' # update

def plot_dot_graph(output, verbose=True, to_file='graph.png'):
    """
    plot_dot_graph : dot + edge 그래프를 표현하는 함수

    Parameter
    ---------
    tmp_dir
        os.path.join을 활용하여 directory 경로를 가지고 있는 변수
        여기서 os.path.expanduser('~'), '.abc'는 ~/.abc라는 디렉터리를 의미
        ※ '~' : 사용자의 홈 디렉터리를 의미하는 '~'를 expanduser를 활용해 절대 경로로 풀어서 해석
    os.path.exists 구문 : tmp_dir 경로에 파일이 존재하지 않을 경우에 폴더를 추가하는 구문
    graph_path : tmp_graph.dot 파일의 경로를 설정하는 변수

    extension : 파일의 포맷 형식을 뽑기 위한 변수
    cmd : 최종 Graphviz를 그리되 dot 파일을 extension에 지정된 확장자로 표현하기 위한 command 명령어
    subprocess.run
        파이썬에서 외부 프로그램을 호출하기 위해 사용된 함수
        ※ doc: https://python.flowdas.com/library/subprocess.html#subprocess.run
           subprocess.run(args, *, ...)
           : args가 기술하는 명령어를 실행하는 함수로써 명령이 완료될 때까지 기다린 다음 return 수행
             return 값은 CompleteProcess 객체
    """
    dot_graph = get_dot_graph(output, verbose)

    # dot 데이터를 파일에 저장
    # tmp_dir = os.path.join(os.path.expanduser('~'), '.DL_level3')
    tmp_dir = os.path.join('.', 'images')
    if not os.path.exists(tmp_dir):
        os.mkdir(tmp_dir)
    graph_path = os.path.join(tmp_dir, to_file[:-4] + '.dot') 

    with open(graph_path, 'w') as f:
        f.write(dot_graph)

    # dot 명령 호출
    extension = os.path.splitext(to_file)[1][1:] # 확장자(png, pdf 등)
    cmd = f'dot {graph_path} -T {extension} -o images/{to_file}'
    subprocess.run(cmd, shell=True)


# =============================================================================
# Utility functions for numpy (numpy magic)
# =============================================================================
def sum_to(x, shape):
    """Sum elements along axes to output an array of a given shape.
    Args:
        x (ndarray): Input array.
        shape:
    Returns:
        ndarray: Output array of the shape.

    Reference: https://github.com/chainer/chainer/blob/v6.4.0/chainer/utils/array.py#L51-L65
    """
    ndim = len(shape)
    lead = x.ndim - ndim
    lead_axis = tuple(range(lead))

    axis = tuple([i + lead for i, sx in enumerate(shape) if sx == 1])
    y = x.sum(lead_axis + axis, keepdims=True)
    if lead > 0:
        y = y.squeeze(lead_axis) # https://numpy.org/doc/stable/reference/generated/numpy.squeeze.html
    return y


def reshape_sum_backward(gy, x_shape, axis, keepdims):
    """Reshape gradient appropriately for myPackage.functions.sum's backward.
    Args:
        gy (myPackage.Variable): Gradient variable from the output by backprop.
        x_shape (tuple): Shape used at sum function's forward.
        axis (None or int or tuple of ints): Axis used at sum function's
            forward.
        keepdims (bool): Keepdims used at sum function's forward.
    Returns:
        myPackage.Variable: Gradient variable which is reshaped appropriately
    """

    ndim = len(x_shape)
    tupled_axis = axis

    if axis is None:
        tupled_axis = None
    elif not isinstance(axis, tuple):
        tupled_axis = (axis,)

    if not (ndim == 0 or tupled_axis is None or keepdims):
        actual_axis = [a if a >= 0 else a + ndim for a in tupled_axis]
        shape = list(gy.shape)
        for a in sorted(actual_axis):
            shape.insert(a, 1)
    else:
        shape = gy.shape

    gy = gy.reshape(shape)  # Variable.reshape(shape)
    return gy


def logsumexp(x, axis = 1):
    xp = cuda.get_array_module(x)
    m = x.max(axis=axis, keepdims=True)
    y = x - m
    xp.exp(y, out=y)
    s = y.sum(axis=axis, keepdims=True)
    xp.log(s, out=s)
    m += s
    return m


# =============================================================================
# others
# =============================================================================
def pair(x):
    if isinstance(x, int):
        return (x, x)
    elif isinstance(x, tuple):
        assert len(x) == 2
        return x
    else:
        raise ValueError


