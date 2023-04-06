from typing import Callable
from edifice import App, Component, Label, TextInput, View, Slider

from data_value import DataValue

class MyEditField(Component):
    def __init__(self,
        label: str,
        value: DataValue,
        onChanged: Callable[[str | float], None],
    ):
        self.__label = label
        self.__value = value
        super().__init__()
        self.__onChanged = onChanged

    def render(self):
        return View(layout="row")(            
                Label(self.__label),
                Slider(
                    value = self.__value.toFloat,
                    on_change = self.__onValueChanged
                ),
                TextInput(
                    text = self.__value.toStr,
                    on_change = self.__onValueChanged,
                    # on_edit_finish = self.set_state,
                ),
            )

    def __onValueChanged(self, value):
        print(f'new value: {value}')
        self.__value.update(value)
        if self.__onChanged: 
            self.__onChanged(value)
