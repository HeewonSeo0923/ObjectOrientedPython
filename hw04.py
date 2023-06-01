import random

class Die:
    def __init__(self):
        self.__face = random.randrange(1, 7)

    def roll(self) -> None:
        self.__face = random.randrange(1, 7)

    @property
    def face(self):
        return self.__face


class YahtzeeDice:
    def __init__(self):
        self.__dice = [Die() for _ in range(5)]

    def roll_dices(self, dice_indices:int) -> int:
        for index in dice_indices:
            self.__dice[index].roll()

    def show_faces(self):
        for die in self.__dice:
            print(die.face, end=' ')
        print()

    def get_faces(self):
        return [die.face for die in self.__dice]

    def count_faces(self, value:int) -> int:
        count = 0
        for die in self.__dice:
            if die.face == value:
                count += 1
        return count

    def sum_faces(self) -> int:
        total = 0
        for die in self.__dice:
            total += die.face
        return total



if __name__ == '__main__':
    dices = YahtzeeDice()
    dices.show_faces()  # 주사위 눈 출력
