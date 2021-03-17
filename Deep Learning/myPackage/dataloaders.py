import math
import random
import numpy as np


class DataLoader:
    """
    DataLoader class

    Args
    ----
    dataset : Dataset 인터페이스를 만족하는 인스턴스(이 말인 즉슨, __getitem__ & __len__ 메서드를 구현한 클래스로부터 생성된 인스턴스를 의미)
    batch_size : 배치 크기
    shuffle : 에포크별로 데이터셋을 뒤섞을지 여부
    """
    def __init__(self, dataset, batch_size, shuffle=True):
        self.dataset = dataset
        self.batch_size = batch_size
        self.shuffle = shuffle
        self.data_size = len(dataset)
        self.max_iter = math.ceil(self.data_size / batch_size)

        self.reset()

    def reset(self):
        self.iteration = 0
        if self.shuffle:
            self.index = np.random.permutation(len(self.dataset))
        else:
            self.index = np.arange(len(self.dataset))

    def __iter__(self):
        return self

    def __next__(self):
        if self.iteration >= self.max_iter:
            self.reset()
            raise StopIteration

        i, batch_size = self.iteration, self.batch_size
        batch_index = self.index[i * batch_size:(i + 1) * batch_size]
        batch = [self.dataset[i] for i in batch_index]
        x = np.array([example[0] for example in batch])
        t = np.array([example[1] for example in batch])

        self.iteration += 1
        return x, t

    def next(self):
        return self.__next__()


