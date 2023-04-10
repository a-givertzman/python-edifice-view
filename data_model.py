from data_value import DataValue


class DataModel:
    def __init__(self,
        value1: DataValue,
        value2: DataValue,
        value3: DataValue,
    ) -> None:
        self.value1 = value1
        self.value2 = value2
        self.value3 = value3

    def changeValue1(self, value):
        self.value1.update(value)
        self.__doMath1()

    def changeValue2(self, value):
        self.value2.update(value)
        self.__doMath1()

    def changeValue3(self, value):
        self.value3.update(value)
        self.__doMath3()

    def __doMath1(self):
        value1 = self.value1.toFloat
        value2 = self.value2.toFloat
        for i in range(100000000):
            value3 = (value1 + value2) / 2
        value3 = (value1 + value2) / 2
        self.__updateValuesForView(value1, value2, value3)


    def __doMath3(self):
        value3 = self.value3.toFloat
        value1 = value3 / 2
        value2 = value3 / 2
        self.__updateValuesForView(value1, value2, value3)


    def __updateValuesForView(self, value1, value2, value3):
        self.value1.update(value1)
        self.value2.update(value2)
        self.value3.update(value3)
