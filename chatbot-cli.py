#!/use/bin/env python3
# -*- coding:utf-8 -*-

from chatbotv2 import Chatbot
def main():
#Listen
    zufallsantworten =["oh wirklich..",
                            "interessant",
                            "das kann man so sehen",
                            "Ich verstehe"]
    reaktionen = {"hallo":"aber hallo!",
                      "geht":"was verstehst du darunter?",
                   "schmeckt":"ich habe keinen Geschmackssinn"}
    #ausgabe begrüssung
    print("Wilkommen beim Chatbot (v2)")
    print("Zum Beenden geben sie Bye ein..")
    print("Worüber wollen sie sprechen?\n")

    #chatbot objekt
    bot=Chatbot(reaktionen,zufallsantworten)
    #logik
    nutzereingabe =""
    while nutzereingabe!="bye":
            nutzereingabe=""
            while nutzereingabe== "":
                nutzereingabe=input("Ihre Frage oder Antwort: ")
            if nutzereingabe=="bye":break
            bot.set_Message(nutzereingabe)
            print(bot.get_Response())

        #ausgabe verabschiedung
    print("bis zum nächsten mal")


main()
