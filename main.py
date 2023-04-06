# import edifice
from edifice import App, Component, Label, TextInput, View, Slider

from my_app import MyApp
from data_model import DataModel
from data_value import DataValue






if __name__ == "__main__":
    App(
        MyApp(
            dataModel = DataModel(
                value1 = DataValue("0.0"),
                value2 = DataValue("0.0"),
                value3 = DataValue("0.3"),
            )
        )
    ).start()