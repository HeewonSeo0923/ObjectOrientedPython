import datetime

class Robot:
    def __init__(self, name:str='bot', color:str='gray') -> None:
        self.name = name
        self.color = color
        self.made_year = datetime.date.today().year

    def say_hello(self) -> None:
        print(f'Hello! My name is {self.name}.', end=' ')
        print(f'I was born in {self.made_year}')

    def change_name(self, name:str):
        self.name = name

    def how_old(self) -> int:
        return datetime.date.today().year - self.made_year

if __name__ == '__main__' :
    robots = [Robot(), Robot('SamBot', 'blue')]
    robots[0].change_name('KBot')

    for r in robots:
        r.say_hello()
