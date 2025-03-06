# 多重继承
class Animal(object):
    pass

class Mammal(Animal):
    def run(self):
        print("running")

class Bird(Animal):
    def flying(self):
        print("flying")

class Bat(Mammal, Bird):
    pass

bat = Bat()
bat.run()
bat.flying()

# 在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Bat继承自Bird。
# 但是，如果需要“混入”额外的功能，通过多重继承就可以实现，比如，让Bat除了继承自Bird外，再同时继承Mammal。
# 这种设计通常称之为MixIn。