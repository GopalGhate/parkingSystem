from vehichle import Vehicle

class Car(Vehicle):
    def __init__(self, color, reg_no, type) -> None:
        super().__init__(color, reg_no, type)

    def get_type(self) -> str:
        return self.type

    def __repr__(self) -> str:
        return str(self.__dict__)