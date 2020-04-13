"""
    The Facade - Fishing will handle all the require subsystem to
    make a character fish
"""
class Fishing(object):
    def prepareToFish(self):
        self.lure = Lure()
        self.lure.attachLure()

        self.pole = Pole()
        self.pole.castPole()

"""
    Sample Subsystem 1...n
"""
class Lure(object):
    def attachLure(self):
        print("Attaching lure to hook")


class Pole(object):
    def castPole(self):
        print("Casting Pole")


if __name__ == "__main__":
    print('*************************************')
    print("Structural Pattern Using a Facade")
    print('*************************************')
    fish = Fishing()
    fish.prepareToFish()
