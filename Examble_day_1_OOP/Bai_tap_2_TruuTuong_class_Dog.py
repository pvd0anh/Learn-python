class Animal:  # trừu tượng mang tính chất chỉ là khung
    def say(self):  # vào lớp con mới cài đặt
        pass

    def print_infor(self):
        print("I say", self.say())


class DOG(Animal):
    def __init__(self, name):
        self.name = name

    def say(self):
        return "Gau Gau !"


class CAT:
    def __init__(self, name):
        self.name = name

    def say(self):
        return "Meow Meow !"


if __name__ == "__main__":
    lst = []
    lst.append(DOG("KIKI"))
    lst.append(DOG("GAUGAU"))
    lst.append(CAT("MEOMEO"))
    lst.append(CAT("MÈO MÈO"))

    for animal in lst:
        if isinstance(animal, DOG):
            print("I am a dog")
        elif isinstance(animal, CAT):
            print("I am a cat")

        print("my name is: " + animal.name)
        # print("I say " + animal.say())
        animal.print_infor()
        print("*" * 20)
