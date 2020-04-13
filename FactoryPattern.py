import abc

"""
   Creational Pattern using a Factory

   Abstract class that used as interface
   This class makes sure that child classes have
   my_method implemented
"""
class Character:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def getAbilities(self):
        return

class Mage(Character):
   def getAbilities(self):
      return ["Fireball","Ice Spear","Freeze"]


class Hunter(Character):
  def getAbilities(self):
      return ["Volley", "Aimed Shot", "Frost Trap"]


class CharacterFactory:
    tmp = None

    @staticmethod
    def createCharacter(charType):
        if charType == 'Mage':
           tmp = Mage()
        if charType == 'Hunter':
          tmp = Hunter()

        return tmp


if __name__ == "__main__":
    print('*************************************')
    print("Creational Pattern Using a Factory")
    print('*************************************')
    mage = CharacterFactory.createCharacter('Mage')
    print("THe Mage's abilities are: ", end='')
    print(mage.getAbilities())

    hunter = CharacterFactory.createCharacter('Hunter')
    print("THe Hunter's abilities are: ", end='')
    print(hunter.getAbilities())
    print('*************************************')


