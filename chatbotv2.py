#!/use/bin/env python3
# -*- coding:utf-8 -*-
import random
class Chatbot:
    """ Eine Klasse für einen Chatbot
    Verwendung:
    bot = Chatbot(reaktionen, Zufallsantworten)
    """
    def __init__(self,reaktionen,zufallsantworten):
        #konstruktor
        #this//self referenz auf sich selbst
        self.__reaktionen =dict(reaktionen)
        self.__zufallsantworten=list(zufallsantworten)
    
    def set_Message(self,message):
        """set_Message
           wierd verwende, um dem bot die eingabe des benutzers zu 
           übergeben
           Verwendung:
           bot.set_Mesage(nutzereingabe)
        """
        self.__message=str(message)
    def get_Response(self):
        """get_Response
        wird verwendet, um dem Chatbot die richtige Antwort
        zu entlocken
        Verwendung:
        response = bot.getResonse()
        """
        self.__message= self.__message.lower()
        self.__words=self.__message.split()
        self.__intelligentAnswers=False

        for word in self.__words:
            if word in self.__reaktionen:
                self.__intelligentAnswers=True
                self.__response = self.__reaktionen[word]
        if not self.__intelligentAnswers:
            self.__response=random.choice(self.__zufallsantworten)
        
        return self.__response 

