import time


il = "What is your name?"


# Prints the string.

print(il)

# Asks for the user's name.

name = input("Name: ")

# Prints the string and the user's name.

print("Ah Your name is"  +" " + name + ".")

#wait for 7 seconds

time.sleep(7)

# Prints the string.

print("Soooooooo")

# Prints the string

print("What do we do now?")


# MORE STUFF!!!!

class Subscribers:
    def __init__(self, subscriber, gibe_gorilla_snacks_money, donate_fake):
        self.subscriber = subscriber
        self.gibe_gorilla_snacks_money = gibe_gorilla_snacks_money
        self.donate_fake = donate_fake

# Creating an instance of the Subscribers class
subscriber_info = Subscribers("1000IQ", "GIVE ME $$$ NOW!!! 10000$ FEE", "FAKE THERE IS NO DONATE GORILLA SNACKS")

# Printing the attributes of the instance
print("Subscriber:", subscriber_info.subscriber)
print("Gorilla Snacks Money Request:", subscriber_info.gibe_gorilla_snacks_money)
print("Donate Fake Message:", subscriber_info.donate_fake)