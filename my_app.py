from edifice import Component, Label, TextInput, View, Slider, Button
from data_model import DataModel
from my_edit_field import MyEditField


class MyApp(Component):
    def __init__(self,
        dataModel: DataModel,
    ):
        super().__init__()
        self.__model = dataModel
        self.__rendered = 0
        self.__enableOnChangeCallback = True

    def render(self):
        self.__rendered += 1
        print(f"rendered: {self.__rendered}")
        return View(layout="column")(
            MyEditField(
                label = "Text input value 1:",
                value = self.__model.value1,
                onChanged = self.__onValue1Changed if self.__enableOnChangeCallback else None
            ),
            MyEditField(
                label = "Text input value 2:",
                value = self.__model.value2,
                onChanged = self.__onValue2Changed if self.__enableOnChangeCallback else None
            ),
            MyEditField(
                label = "Text input value 3:",
                value = self.__model.value3,
                onChanged = self.__onValue3Changed if self.__enableOnChangeCallback else None
            ),
            Button(
                title = "solve",
                on_click = self.__onSolveButtonClicked if self.__enableOnChangeCallback else None
            )
        )

    def __setState(self):
        self.__enableOnChangeCallback = False
        self.setState()
        self.__enableOnChangeCallback = True

    def __onSolveButtonClicked(self):
        self.__model.__doMath1()
    
    def __onValue1Changed(self, value):
        print(f'new value: {value}')
        self.__setState()

    def __onValue2Changed(self, value):
        print(f'new value: {value}')
        self.__model.changeValue2(value)
        self.__setState()

    def __onValue3Changed(self, value):
        print(f'new value: {value}')
        self.__model.changeValue3(value)
        self.__setState()
