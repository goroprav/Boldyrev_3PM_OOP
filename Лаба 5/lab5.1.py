import pickle

class User:
    def __init__(self, id, login, password, name):
        self.id = id
        self.login = login
        self.password = password
        self.name = name

class IUserRepository:
    def get_all(self):
        pass

    def add(self, user):
        pass

    def remove(self, user):
        pass

    def update(self, user):
        pass

class UserRepository(IUserRepository):
    def __init__(self, file_name):
        self.file_name = file_name
        self.users = self.get_all()

    def get_all(self):
        try:
            with open(self.file_name, 'rb') as file:
                return pickle.load(file)
        except FileNotFoundError:
            return []

    def add(self, user):
        if not self.users:
            user.id = 1
        else:
            user.id = max(u.id for u in self.users) + 1
        self.users.append(user)
        with open(self.file_name, 'wb') as file:
            pickle.dump(self.users, file)

    def remove(self, user):
        self.users = [u for u in self.users if u.id != user.id]
        with open(self.file_name, 'wb') as file:
            pickle.dump(self.users, file)

    def update(self, user):
        for i, u in enumerate(self.users):
            if u.id == user.id:
                self.users[i] = user
                break
        with open(self.file_name, 'wb') as file:
            pickle.dump(self.users, file)

class IUserManager:
    def sign_in(self, user):
        pass

    def sign_out(self, user):
        pass

    def is_authorized(self):
        pass

class UserManager(IUserManager):
    def __init__(self, user_repository):
        self.user_repository = user_repository
        self.current_user = None

    def sign_in(self, user):
        self.current_user = user

    def sign_out(self, user):
        self.current_user = None

    def is_authorized(self):
        return self.current_user is not None

def main():
    user_repository = UserRepository('users.dat')
    user_manager = UserManager(user_repository)

    while True:
        print("1. Регистрация нового пользователя")
        print("2. Вход в аккаунт")
        print("3. Выход из аккаунта")
        print("4. Проверить, вошел ли пользователь в аккаунт")
        print("5. Выйти из приложения")
        choice = input("Выберите действие: ")

        if choice == "1":
            login = input("Введите логин: ")
            password = input("Введите пароль: ")
            name = input("Введите имя: ")
            new_user = User(0, login, password, name)  # id будет назначен автоматически
            user_repository.add(new_user)
            print("Пользователь зарегистрирован успешно. Ему назначен id:", new_user.id)

        elif choice == "2":
            last_user = user_repository.get_all()[-1]  # Получаем последнего вошедшего пользователя
            if last_user and user_manager.is_authorized():
                user_manager.sign_in(last_user)  # Автоавторизация последнего вошедшего пользователя
                print("Вы успешно вошли в аккаунт как", last_user.name)
            else:
                login = input("Введите логин: ")
                password = input("Введите пароль: ")
                user = next((u for u in user_repository.get_all() if u.login == login and u.password == password), None)
                if user:
                    user_manager.sign_in(user)
                    print("Вы успешно вошли в аккаунт.")
                else:
                    print("Неверный логин или пароль.")

        elif choice == "3":
            user_manager.sign_out(user_manager.current_user)
            print("Вы успешно вышли из аккаунта.")

        elif choice == "4":
            if user_manager.is_authorized():
                print("Пользователь вошел в аккаунт.")
            else:
                print("Пользователь не вошел в аккаунт.")

        elif choice == "5":
            break

if __name__ == "__main__":
    main()
