class Control:
    def setPosition(self, x, y):
        print(f"Установка позиции по ({x}, {y})")

    def getPosition(self):
        print("Получение позиции")

# Создание класса-фабрики для генерации контролов
class ControlFactory:
    def createForm(self):
        pass

    def createLabel(self):
        pass

    def createTextBox(self):
        pass

    def createComboBox(self):
        pass

    def createButton(self):
        pass

# Создание классов контролов для различных операционных систем
class WindowsControlFactory(ControlFactory):
    def createForm(self):
        return WindowsForm()

    def createLabel(self):
        return WindowsLabel()

    def createTextBox(self):
        return WindowsTextBox()

    def createComboBox(self):
        return WindowsComboBox()

    def createButton(self):
        return WindowsButton()

class LinuxControlFactory(ControlFactory):
    def createForm(self):
        return LinuxForm()

    def createLabel(self):
        return LinuxLabel()

    def createTextBox(self):
        return LinuxTextBox()

    def createComboBox(self):
        return LinuxComboBox()

    def createButton(self):
        return LinuxButton()

class MacOSControlFactory(ControlFactory):
    def createForm(self):
        return MacOSForm()

    def createLabel(self):
        return MacOSLabel()

    def createTextBox(self):
        return MacOSTextBox()

    def createComboBox(self):
        return MacOSComboBox()

    def createButton(self):
        return MacOSButton()

# Создание классов контролов для каждой операционной системы
class MacOSForm(Control):
    def addControl(self, control):
        print(f"Добавление контролла Control в форму MacOS")

class MacOSLabel(Control):
    def setText(self, text):
        print(f"Установка текста '{text}' для метки MacOS")

    def getText(self):
        print("Получение текста из метки MacOS")

class MacOSTextBox(Control):
    def setText(self, text):
        print(f"Установка текста '{text}' для текстового поля MacOS")

    def getText(self):
        print("Получение текста из текстового поля MacOS")

    def onValueChanged(self):
        print("Событие OnValueChanged для текстового поля MacOS")

class MacOSComboBox(Control):
    def setSelectedIndex(self, index):
        print(f"Установка выбранного индекса {index} для комбинированного поля MacOS")

    def getSelectedIndex(self):
        print("Получение выбранного индекса из комбинированного поля MacOS")

    def setItems(self, items):
        print(f"Установка элементов {items} для комбинированного поля MacOS")

    def getItems(self):
        print("Получение элементов из комбинированного поля MacOS")

class MacOSButton(Control):
    def setText(self, text):
        print(f"Установка текста '{text}' для кнопки MacOS")

    def getText(self):
        print("Получение текста из кнопки MacOS")

    def click(self):
        print("Событие клика для кнопки MacOS")

# Создание экземпляров контролов для различных операционных систем
macOSFactory = MacOSControlFactory()
macOSForm = macOSFactory.createForm()
macOSLabel = macOSFactory.createLabel()
macOSTextBox = macOSFactory.createTextBox()
macOSComboBox = macOSFactory.createComboBox()
macOSButton = macOSFactory.createButton()

# Симуляция вызова методов контролов
macOSForm.setPosition(10, 10)
macOSForm.addControl(macOSLabel)
macOSLabel.setText("Пример текста")
macOSLabel.getText()
macOSTextBox.setPosition(20, 20)
macOSTextBox.setText("Введенный текст")
macOSTextBox.getText()
macOSTextBox.onValueChanged()
macOSComboBox.setPosition(30, 30)
macOSComboBox.setSelectedIndex(0)
macOSComboBox.getSelectedIndex()
macOSComboBox.setItems(["Элемент 1", "Элемент 2"])
macOSComboBox.getItems()
macOSButton.setPosition(40, 40)
macOSButton.setText("Нажми меня")
macOSButton.getText()
macOSButton.click()

