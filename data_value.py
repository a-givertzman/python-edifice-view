class DataValue:
    def __init__(self, value: str):
        self.__value = value
        self.__out: float = 0.0
        self.__converted = False

    def update(self, value: str | float):
        if (isinstance(value, str)):
            self.__converted = False
            self.__value = value
            print(f'[StrConversion] input is str')
        else:
            self.__converted = True
            self.__out = value
            print(f'[StrConversion] input is numeric')

    @property
    def toFloat(self):
        if (not self.__converted):
            print(f'[StrConversion] converting: {self.__value}')
            try:
                out = float(self.__value)
                self.__out = out
            except ValueError as err:
                print(f'[StrConversion] error: {err}')
            self.__converted = True
        return self.__out
    
    @property
    def origin(self):
        return self.__value

    @property
    def toStr(self):
        return f'{self.__out}'