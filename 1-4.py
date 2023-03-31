class Point:
    def __init__(self, x:float=0.0, y:float=0.0) -> None:
        self.x = x
        self.y = y

class Account:
    def __init__(self, account_number:str, owner:str, balance:float)->None:
        self.acnt_num = account_number
        self.owner = owner
        self.balance = balance

