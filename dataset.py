# dataset.py
# Работа с обучающей выборкой
class Dataset:
    def __init__(self):
        self.data = []

    def add_sample(self, sample):
        self.data.append(sample)
