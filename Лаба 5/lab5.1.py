from abc import ABC, abstractmethod
import ast
class IUserManager(ABC):
    @abstractmethod
    def SignIn(self, user):
        pass

    @abstractmethod
    def SignOut(self, user):
        pass

    @abstractmethod
    def isAuthorized(self):
        pass

class IRepository(ABC):
    @abstractmethod
    def GetAll(self):
        pass

    @abstractmethod
    def Add(self, item):
        pass

    @abstractmethod
    def Remove(self, item):
        pass

    @abstractmethod
    def Update(self, item):
        pass

class User:
    def __init__(self, id, login, password, name):
        self.id = id
        self.login = login
        self.password = password
        self.name = name

class IUserRepository(IRepository):
    @abstractmethod
    def GetById(self, id):
        pass

    @abstractmethod
    def GetByLogin(self, login):
        pass
    
class FileUserRepository(IUserRepository):
    
    def __init__(self, file_name):
        self.file_name = file_name

    def GetAll(self):
        try:
            with open(self.file_name, 'r') as file:
                users = file.readlines()
            users = [ast.literal_eval(user) for user in users]  # Безопасное преобразование каждой строки в словарь
        except FileNotFoundError:
            users = []
        return users

    def Add(self, user):
        with open(self.file_name, 'a') as file:  # Открываем файл в режиме добавления
            file.write(str(user.__dict__) + '\n')  # Записываем словарь пользователя в новую строку

    def Remove(self, user):
        users = self.GetAll()
        users = [u for u in users if u['id'] != user.id]
        with open(self.file_name, 'w') as file:  # Открываем файл в режиме записи для перезаписи существующих данных
            for user in users:
                file.write(str(user) + '\n')  # Записываем словарь каждого пользователя в новую строку

    def Update(self, user):
        users = self.GetAll()
        for i, u in enumerate(users):
            if u['id'] == user.id:
                users[i] = user.__dict__  # Обновляем словарь пользователя
                break
        with open(self.file_name, 'w') as file:  # Открываем файл в режиме записи для перезаписи существующих данных
            for user in users:
                file.write(str(user) + '\n')  # Записываем словарь каждого пользователя в новую 

    def GetById(self, id):
        users = self.GetAll()
        for user in users:
            if user['id'] == id:
                return User(**user)

    def GetByLogin(self, login):
        if login == "last_user":
            users = self.GetAll()
            if users:
                last_user = users[-1]  #получение данных последненго вошедшего пользователя
                return User(**last_user)
            else:
                return None  
        else:
            users = self.GetAll()
            for user in users:
                if user['login'] == login:
                    return User(**user)
            
class AuthManager(IUserManager):
    def __init__(self, user_repository):
        self.user_repository = user_repository
        self.current_user = None

    def SignIn(self, user):
        self.current_user = user

    def SignOut(self, user):
        self.current_user = None

    def isAuthorized(self):
        return self.current_user is not None
def main_menu():
    print("1. Регистрация нового пользователя")
    print("2. Авторизация")
    print("3. Автоавторизация последнего вошедшего пользователя")
    print("4. Сменить пользователя")
    print("5. Выход")

user_repository = FileUserRepository("users.json")
auth_manager = AuthManager(user_repository)

while True:
    main_menu()
    choice = input("Выберите действие: ")
    
    if choice == "1":
        # Логика для регистрации нового пользователя
        id = len(user_repository.GetAll()) + 1  # Автоматическое назначение ID
        login = input("Введите логин: ")
        password = input("Введите пароль: ")
        name = input("Введите имя: ")
        new_user = User(id, login, password, name)
        user_repository.Add(new_user)
    elif choice == "2":
        # Логика для авторизации
        login = input("Введите логин: ")
        password = input("Введите пароль: ")
        user = user_repository.GetByLogin(login)
        if user and user.password == password:
            auth_manager.SignIn(user)
            print("Вы успешно авторизовались.")
        else:
            print("Неверный логин или пароль.")
    elif choice == "3":
        # Логика для автоавторизации последнего вошедшего пользователя
        last_user = user_repository.GetByLogin("last_user")  
        if last_user:
            auth_manager.SignIn(last_user)
            print(f"Вы автоматически авторизовались за последнего пользователя {last_user.name}.")
        else:
            print("Никто не авторизован.")
    elif choice == "4":
        # Логика для смены пользователя
        if auth_manager.isAuthorized():
            print(f"Текущий пользователь {auth_manager.current_user.name} вышел из системы.")
            auth_manager.SignOut(auth_manager.current_user)
        login = input("Введите логин нового пользователя: ")
        password = input("Введите пароль нового пользователя: ")
        user = user_repository.GetByLogin(login)
        if user and user.password == password:
            auth_manager.SignIn(user)
            print("Вы успешно авторизовались.")
        else:
            print("Неверный логин или пароль.")
    elif choice == "5":
        break
    else:
        print("Некорректный выбор. Пожалуйста, выберите существующий вариант.")
