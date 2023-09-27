import math

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Vector:
    def __init__(self, x1, y1, z1, x2=None, y2=None, z2=None):
        if x2 is not None and y2 is not None and z2 is not None:
            self.x = x2 - x1
            self.y = y2 - y1
            self.z = z2 - z1
        else:
            self.x = x1
            self.y = y1
            self.z = z1
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def vichitanie(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def obratnost(self):
        return Vector(-self.x, -self.y, -self.z)
    
    def dlina(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def edinich_vector(self):
        length = self.length()
        return Vector(self.x / length, self.y / length, self.z / length)
    
    def scalar_x(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def vector_x(self, other):
        return Vector(self.y * other.z - self.z * other.y, self.z * other.x - self.x * other.z, self.x * other.y - self.y * other.x)
    
    def smeshan_x(self, other1, other2):
        return self.scalar_x(other1.vector_x(other2))
    
    def kollinear(self, other1):
        vector3=self.vector_x(other1)
        if (vector3.x==0 and vector3.y==0 and vector3.z==0):
            return True
        else:
            return False
        
    def complanar(self,other1,other2):
        if self.smeshan_x(other1,other2)==0: return True
        else: return False  
    
    def rasstoianie(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2)
    
    def ugol(self, other):
        scalar_x = self.scalar_x(other)
        length_product = self.length() * other.length()
        return math.acos(scalar_x / length_product)
    


# Создание объектов Point
# Функция для ввода координат точки
def input_point_coordinates():
    x = float(input("Введите координату x: "))
    y = float(input("Введите координату y: "))
    z = float(input("Введите координату z: "))
    return Point(x, y, z)

# Функция для ввода вектора
def input_vector():
    print("Выберите способ задания вектора:")
    print("1. По координатам")
    print("2. По двум точкам")
    choice = int(input("Ваш выбор: "))

    if choice == 1:
        x = float(input("Введите координату x: "))
        y = float(input("Введите координату y: "))
        z = float(input("Введите координату z: "))
        return Vector(x, y, z)
    elif choice == 2:
        print("Введите координаты первой точки:")
        point1 = input_point_coordinates()
        print("Введите координаты второй точки:")
        point2 = input_point_coordinates()
        return Vector(point1.x, point1.y, point1.z, point2.x, point2.y, point2.z)
    else:
        print("Некорректный выбор")
        return None

# Основной цикл программы
while True:
    print("Выберите операцию:")
    print("1. Сложение векторов")
    print("2. Вычитание векторов")
    print("3. Получение обратного вектора")
    print("4. Построение единичного вектора")
    print("5. Скалярное произведение векторов")
    print("6. Векторное произведение векторов")
    print("7. Смешанное произведение векторов")
    print("8. Длина вектора")
    print("9. Определение коллинеарности векторов")
    print("10. Определение компланарности векторов")
    print("11. Нахождение расстояния между векторами")
    print("12. Нахождение угла между векторами")
    print("0. Выход")
    operation = int(input("Ваш выбор: "))

    if operation == 0:
        break
    elif operation == 1:
        print("Введите координаты первого вектора:")
        vector1 = input_vector()
        print("Введите координаты второго вектора:")
        vector2 = input_vector()
        result_vector = vector1+vector2
        print("Результат сложения векторов:", result_vector.x, result_vector.y, result_vector.z)
    elif operation == 2:
        print("Введите координаты первого вектора:")
        vector1 = input_vector()
        print("Введите координаты второго вектора:")
        vector2 = input_vector()
        result_vector = vector1.vichitanie(vector2)
        print("Результат вычитания векторов:", result_vector.x, result_vector.y, result_vector.z)
    elif operation == 3:
        print("Введите координаты вектора:")
        vector = input_vector()
        result_vector = vector.obratnost()
        print("Обратный вектор:", result_vector.x, result_vector.y, result_vector.z)
    elif operation == 4:
        print("Введите координаты вектора:")
        vector = input_vector()
        result_vector = vector.edinich_vector()
        print("Единичный вектор:", result_vector.x, result_vector.y, result_vector.z)
    elif operation == 5:
        print("Введите координаты первого вектора:")
        vector1 = input_vector()
        print("Введите координаты второго вектора:")
        vector2 = input_vector()
        result = vector1.scalar_x(vector2)
        print("Скалярное произведение векторов:", result)
    elif operation == 6:
        print("Введите координаты первого вектора:")
        vector1 = input_vector()
        print("Введите координаты второго вектора:")
        vector2 = input_vector()
        result_vector = vector1.vector_x(vector2)
        print("Векторное произведение векторов:", result_vector.x, result_vector.y, result_vector.z)
    elif operation == 7:
        print("Введите координаты первого вектора:")
        vector1 = input_vector()
        print("Введите координаты второго вектора:")
        vector2 = input_vector()
        print("Введите координаты третьего вектора:")
        vector3 = input_vector()
        result = vector1.smeshan_x(vector2, vector3) 
        print("Смешанное произведение векторов:", result)
    elif operation == 8:
        print("Введите координаты вектора:")
        vector1 = input_vector()
        result = vector1.dlina()
        print("Длина вектора:", result)
    elif operation == 9:
        print("Введите координаты первого вектора:")
        vector1 = input_vector()
        print("Введите координаты второго вектора:")
        vector2 = input_vector()
        result = vector1.kollinear(vector2)
        if result==True: print("Векторы коллинеарны")
        else: print("Векторы не коллинеарны")    
    elif operation == 10:
        print("Введите координаты первого вектора:")
        vector1 = input_vector()
        print("Введите координаты второго вектора:")
        vector2 = input_vector()
        print("Введите координаты третьего вектора:")
        vector3 = input_vector()
        result = vector1.complanar(vector2,vector3)
        if result==True: print("Векторы компланарны")
        else: print("Векторы не компланарны")   
    elif operation == 11:
        print("Введите координаты первого вектора:")
        vector1 = input_vector()
        print("Введите координаты второго вектора:")
        vector2 = input_vector()
        result = vector1.rasstoianie(vector2)
        print("Расстояяние между векторами:", result)   
    elif operation == 12:
        print("Введите координаты первого вектора:")
        vector1 = input_vector()
        print("Введите координаты второго вектора:")
        vector2 = input_vector()
        result = vector1.ugol(vector2)
        print("Угол между векторами в радианах:", result)
    
    
        
        
        
        
        
        
