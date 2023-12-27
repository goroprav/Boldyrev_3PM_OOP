import time



class VirtualKeyboard:
    def __init__(self):
        self.actions = {}
        self.history = []
        self.state = None  # Новое поле для хранения текущего состояния

    def assign_action(self, key, action):
        # Сохраняем текущее действие перед его изменением
        if key in self.actions:
            self.history.append((key, self.actions[key]))
        else:
            self.history.append((key, None))
        self.actions[key] = action
        print(f"Клавиша {key} назначена на действие {action.__name__}")

    def press_key(self, key):
        if key in self.actions:
            # Сохраняем текущее состояние перед выполнением действия
            self.history.append(self.state)
            action = self.actions[key]
            self.state = action()  # Предполагает, что действие возвращает новое состояние
            print(f"Нажата клавиша {key}")

    def undo_last_action(self):
        if self.history:
            last_key, last_action = self.history.pop()  # Возвращаем состояние обратно
            if last_key in self.actions and self.actions[last_key] == last_action:
                self.state = self.history.pop()
            else:
                self.actions[last_key] = last_action
            print("Последнее действие отменено")



# Пример использования
keyboard = VirtualKeyboard()

# Определение переназначаемых действий для клавиш и комбинаций клавиш
def action1():
    print("Выполнено действие 1")
    return "Состояние после выполнения действия 1"

def action2():
    print("Выполнено действие 2")
    return "Состояние после выполнения действия 2"

def action3():
    print("Выполнено действие 3")
    return "Состояние после выполнения действия 3"

keyboard.assign_action("F1", action1)
keyboard.assign_action("Ctrl+Alt+X", action2)
keyboard.assign_action("Shift+Z", action3)

# Демонстрация работы клавиатуры с задержкой между нажатиями
keyboard.press_key("F1")  # Выполнено действие 1
time.sleep(1)  # Задержка в 1 секунду

keyboard.press_key("Ctrl+Alt+X")  # Выполнено действие 2
time.sleep(1)  # Задержка в 1 секунду

keyboard.assign_action("Shift+Z", action1)

keyboard.undo_last_action()  # Отменено действие 3
time.sleep(1)  # Задержка в 1 секунду

keyboard.press_key("Shift+Z")  # Выполнено действие 3
time.sleep(1)  # Задержка в 1 секунду

