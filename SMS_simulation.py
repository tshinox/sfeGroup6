# An SMS Simulator


class SMSMessage(object):

    def __init__(self, hasBeenRead, messageText, fromNumber):
        self.stat = hasBeenRead
        self.text = messageText
        self.Number = fromNumber

    def MarkASRead(self):
        self.stat = True


def add_sms(lst, SMS):
    lst.append(SMS)
    return


def get_count(SMSes):
    return len(SMSes)


def get_message(obj):
    return obj.text


def get_unread_message(obj):
    if not obj.stat:
        return obj.text


def remove(lst, txt):
    return lst.remove(txt)


no_1 = SMSMessage(False, "Hello", "0798653452")
no_2 = SMSMessage(False, "WYD", "0845673864")
no_3 = SMSMessage(False, "How are you?", "0631873298")

SMSStore = []
userChoice = ""

while userChoice != "quit":
    userChoice = input("what would you like to do - read/send/quit?")
    if userChoice == "read":
        Open = input("You have " + str(get_count(SMSStore)) + " message(s),open? - yes/no")
        if Open == "yes":
            for i in SMSStore:
                print(i.text, i.Number, sep=" from ")
                if i == 1:
                    no_1.MarkASRead()
                    remove(SMSStore, i.text)
                elif i == 2:
                    no_2.MarkASRead()
                    remove(SMSStore, i.text)
                elif i == 3:
                    no_3.MarkASRead()
                    remove(SMSStore, i.text)
    elif userChoice == "send":
        add_sms(SMSStore, no_1)
        add_sms(SMSStore, no_2)
        add_sms(SMSStore, no_3)
        print("Messages sent.")
    elif userChoice == "quit":
        print("Goodbye")
    else:
        print('Oops - incorrect input')
