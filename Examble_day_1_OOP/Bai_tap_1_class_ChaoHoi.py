class Greeting:
    count = 0

    def __init__(self, name):
        self.name = name
        Greeting.count += 1

    def say_hi(self):
        # print("hello", self.name)
        return "hello " + self.name

    def say_bye(self):
        print("good bye", self.name)


if __name__ == "__main__":
    friend = Greeting("Tom")
    print(friend.say_hi())
    friend.say_bye()

    boy_friend = Greeting("Jeck")
    print(boy_friend.say_hi())
    boy_friend.say_bye()

    print(Greeting.count)

    girl_friend = Greeting("Marry")
    print(girl_friend.say_hi())
    girl_friend.say_bye()

    print(Greeting.count)
