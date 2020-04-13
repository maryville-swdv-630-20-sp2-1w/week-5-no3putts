from __future__ import annotations
from typing import Optional


class Singleton(type):
    """
        This is my attempt at a singleton
    """

    _instance: Optional[BattlegroundOne] = None

    def __call__(self) -> BattlegroundOne:
        if self._instance is None:
            self._instance = super().__call__()
        return self._instance


class BattlegroundOne(metaclass=Singleton):
    def enterBattleground(self, name):
        print('Entering battle ground 1 as' + name)


class BattlegroundTwo():
    def enterBattleground(self, name):
        print('Entering battle ground 2 as ' + name)


if __name__ == "__main__":
    # Testing the singleton
    print('*************************************************************')
    print("Singleton Test 1, create two objects of type BattlegroundOne")
    print("bg1 = BattlegroundOne()")
    print("bg2 = BattlegroundOne()")
    print('*************************************************************')
    bg1 = BattlegroundOne()
    bg2 = BattlegroundOne()

    print("Singleton: Address of bg1: ", bg1)
    print("Singleton: Address of bg2: ",  bg2)

    if id(bg1) == id(bg2):
        bg1.enterBattleground('Kuka')
        bg2.enterBattleground('Puka')
        print("Singleton works, both battle grounds are the same instance.")
    else:
        print("Singleton failed, battle grounds are different instances.")
    print('*************************************************************')
    print()
    print('*************************************************************')
    print("Non Singleton Test 2, create two objects of type BattlegroundTwo")
    print("bg1 = BattlegroundTwo()")
    print("bg2 = BattlegroundTwo()")
    print('*************************************************************')
    bg1 = BattlegroundTwo()
    bg2 = BattlegroundTwo()

    print("Non Singleton: Address of bg1: ",  bg1)
    print("Non Singleton: Address of bg2: ",  bg2)
    if id(bg1) == id(bg2):
        bg1.enterBattleground('Kuka')
        bg2.enterBattleground('Puka')
        print("Singleton works, both battle grounds are the same instance.")
    else:
        print("Singleton failed, battle grounds are different instances.")
    print('*************************************************************')