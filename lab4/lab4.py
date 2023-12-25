import time

class VirtualKeyboard:
    def __init__(self):
        self.actions = {}
        self.history = []

    def assign_action(self, key, action):
        self.actions[key] = action
        print(f"Клавиша {key} назначена на действие {action.__name__}")

    def press_key(self, key):
        if key in self.actions:
            action = self.actions[key]
            action()
            self.history.append((key, action))
            print(f"Нажата клавиша {key}")

    def undo_last_action(self):
        if self.history:
            key, _ = self.history.pop()
            print(f"Отменено действие для клавиши {key}")

# Пример использования
keyboard = VirtualKeyboard()

# Определение переназначаемых действий для клавиш и комбинаций клавиш
def action1():
    print("Выполнено действие 1")

def action2():
    print("Выполнено действие 2")

def action3():
    print("Выполнено действие 3")

keyboard.assign_action("F1", action1)
keyboard.assign_action("Ctrl+Alt+X", action2)
keyboard.assign_action("Shift+Z", action3)

# Демонстрация работы клавиатуры с задержкой между нажатиями
keyboard.press_key("F1")  # Выполнено действие 1
time.sleep(1)  # Задержка в 1 секунду

keyboard.press_key("Ctrl+Alt+X")  # Выполнено действие 2
time.sleep(1)  # Задержка в 1 секунду

keyboard.press_key("Shift+Z")  # Выполнено действие 3
time.sleep(1)  # Задержка в 1 секунду

# Откат последнего действия
keyboard.undo_last_action()  # Отменено действие 3
time.sleep(1)  # Задержка в 1 секунду

# Демонстрация переназначения клавиш и комбинаций клавиш с перезапуском
keyboard.assign_action("F1", action3)
keyboard.assign_action("Ctrl+Alt+X", action1)

keyboard.press_key("F1")  # Выполнено действие 3
time.sleep(1)  # Задержка в 1 секунду

keyboard.press_key("Ctrl+Alt+X")  # Выполнено действие 1
time.sleep(1)  # Задержка в 1 секунду

# Перезапуск клавиатуры
keyboard = VirtualKeyboard()

keyboard.press_key("F1")  # Выполнено действие 1 (новое переназначение)
time.sleep(1)  # Задержка в 1 секунду

keyboard.press_key("Ctrl+Alt+X")  # Выполнено действие 2 (новое переназначение)
time.sleep(1)  # Задержка в 1 секунду

