import abc


class Banana_data_class(metaclass=abc.ABCMeta):
    def __init__(self, data):
        self.set(data)
    @abc.abstractmethod
    def get(self):
        pass

    @abc.abstractmethod
    def type(self) -> str:
        pass

    @abc.abstractmethod
    def set(self, data: str):
        pass


class Banana_number(Banana_data_class):
    def __init__(self, data):
        super().__init__(data)
        self.number = None

    def set(self, data: str):
        if int(data) == float(data):
            self.number = int(data)
        else:
            self.number = float(data)

    def type(self) -> str:
        return "number"

    def get(self):
        return self.number

