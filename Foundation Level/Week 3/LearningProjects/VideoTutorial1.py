def talk(phrase):
    def say(word):
        print(word)
    words = phrase.split("a")
    for i in words:
        say(i)

talk("I am going to pray Al-Fajr")
