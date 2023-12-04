import numpy as np

class Array3d:
    def __init__(self, dim0, dim1, dim2):
        self.dim0 = dim0
        self.dim1 = dim1
        self.dim2 = dim2
        self.array = np.zeros((dim0, dim1, dim2))

    def __getitem__(self, idx):
        return self.array[idx]

    def GetValues0(self, i):
        return self.array[i, :, :]

    def GetValues1(self, j):
        return self.array[:, j, :]

    def GetValues2(self, k):
        return self.array[:, :, k]

    def GetValues01(self, i, j):
        return self.array[i, j, :]

    def GetValues02(self, i, k):
        return self.array[i, :, k]

    def GetValues12(self, j, k):
        return self.array[:, j, k]

    def SetValues0(self, i, values):
        self.array[i, :, :] = values

    def SetValues1(self, j, values):
        self.array[:, j, :] = values

    def SetValues2(self, k, values):
        self.array[:, :, k] = values

    def SetValues01(self, i, j, values):
        self.array[i, j, :] = values

    def SetValues02(self, i, k, values):
        self.array[i, :, k] = values

    def SetValues12(self, j, k, values):
        self.array[:, j, k] = values

    @classmethod
    def ones(cls, dim0, dim1, dim2):
        instance = cls(dim0, dim1, dim2)
        instance.array = np.ones((dim0, dim1, dim2))
        return instance

    @classmethod
    def zeros(cls, dim0, dim1, dim2):
        instance = cls(dim0, dim1, dim2)
        instance.array = np.zeros((dim0, dim1, dim2))
        return instance

    @classmethod
    def fill(cls, dim0, dim1, dim2, value):
        instance = cls(dim0, dim1, dim2)
        instance.array = np.full((dim0, dim1, dim2), value)
        return instance


arr = Array3d(3, 3, 3)

# Заполняем массив значениями
for i in range(arr.dim0):
    for j in range(arr.dim1):
        for k in range(arr.dim2):
            arr[i][j][k] = i * j * k

# Выводим массив
print(arr.array)

# Получаем и выводим срезы массива
print(arr.GetValues0(1))
print(arr.GetValues1(1))
print(arr.GetValues2(1))

# Устанавливаем значения для срезов
arr.SetValues0(1, np.ones((arr.dim1, arr.dim2)))
print(arr.GetValues0(1))

# Создаем новые экземпляры класса с массивами, заполненными единицами, нулями и произвольным значением
arr_ones = Array3d.ones(3, 3, 3)
arr_zeros = Array3d.zeros(3, 3, 3)
arr_fill = Array3d.fill(3, 3, 3, 7)

# Выводим эти массивы
print(arr_ones.array)
print(arr_zeros.array)
print(arr_fill.array)
