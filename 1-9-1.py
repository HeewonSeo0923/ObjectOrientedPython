class Person:
    def __init__(self, name, physic_health, mental_health):
        self.name = name
        self.__physic_health = physic_health
        self.__mental_health = mental_health

    @property
    def condition (self):
        return 