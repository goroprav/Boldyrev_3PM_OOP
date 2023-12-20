class Array3d:
    def __init__(self, dim0, dim1, dim2):
        self.dim0 = dim0
        self.dim1 = dim1
        self.dim2 = dim2
        self.array = [[[0 for _ in range(dim2)] for _ in range(dim1)] for _ in range(dim0)]

    def __getitem__(self, idx):
        return self.array[idx]

    def GetValues0(self, i):
        return self.array[i]

    def GetValues1(self, j):
        return [[self.array[i][j] for i in range(self.dim0)] for _ in range(self.dim1)]

    def GetValues2(self, k):
        return [[self.array[i][j][k] for j in range(self.dim1)] for i in range(self.dim0)]

    def GetValues01(self, i, j):
        return self.array[i][j]

    def GetValues02(self, i, k):
        return [self.array[i][j][k] for j in range(self.dim1)]

    def GetValues12(self, j, k):
        return [self.array[i][j][k] for i in range(self.dim0)]

    def SetValues0(self, i, values):
        self.array[i] = values

    def SetValues1(self, j, values):
        for i in range(self.dim0):
            self.array[i][j] = values[i]

    def SetValues2(self, k, values):
        for i in range(self.dim0):
            for j in range(self.dim1):
                self.array[i][j][k] = values[i][j]

    def SetValues01(self, i, j, values):
        self.array[i][j] = values

    def SetValues02(self, i, k, values):
        for j in range(self.dim1):
            self.array[i][j][k] = values[j]

    def SetValues12(self, j, k, values):
        for i in range(self.dim0):
            self.array[i][j][k] = values[i]

    @classmethod
    def ones(cls, dim0, dim1, dim2):
        instance = cls(dim0, dim1, dim2)
        instance.array = [[[1 for _ in range(dim2)] for _ in range(dim1)] for _ in range(dim0)]
        return instance

    @classmethod
    def zeros(cls, dim0, dim1, dim2):
        instance = cls(dim0, dim1, dim2)
        instance.array = [[[0 for _ in range(dim2)] for _ in range(dim1)] for _ in range(dim0)]
        return instance

    @classmethod
    def fill(cls, dim0, dim1, dim2, value):
        instance = cls(dim0, dim1, dim2)
        instance.array = [[[value for _ in range(dim2)] for _ in range(dim1)] for _ in range(dim0)]
        return instance


arr = Array3d(3, 3, 3)

# Заполняем массив значениями
for i in range(arr.dim0):
    for j in range(arr.dim1):
        for k in range(arr.dim2):
            arr[i][j][k] = i * j * k

# Выводим массив
for i in range(arr.dim0):
    for j in range(arr.dim1):
        for k in range(arr.dim2):
            print(arr[i][j][k], end=" ")
        print()
    print()

# Получаем и выводим срезы массива
print(arr.GetValues0(1))
print(arr.GetValues1(1))
print(arr.GetValues2(1))

# Устанавливаем значения для срезов
arr.SetValues0(1, [[1 for _ in range(arr.dim2)] for _ in range(arr.dim1)])
print(arr.GetValues0(1))

# Создаем новые экземпляры класса с массивами, заполненными единицами, нулями и произвольным значением
arr_ones = Array3d.ones(3, 3, 3)
arr_zeros = Array3d.zeros(3, 3, 3)
arr_fill = Array3d.fill(3, 3, 3, 7)

# Выводим эти массивы
for i in range(arr_ones.dim0):
    for j in range(arr_ones.dim1):
        for k in range(arr_ones.dim2):
            print(arr_ones[i][j][k], end=" ")
        print()
    print()

for i in range(arr_zeros.dim0):
    for j in range(arr_zeros.dim1):
        for k in range(arr_zeros.dim2):
            print(arr_zeros[i][j][k], end=" ")
        print()
    print()

for i in range(arr_fill.dim0):
    for j in range(arr_fill.dim1):
        for k in range(arr_fill.dim2):
            print(arr_fill[i][j][k], end=" ")
        print()
    print()

