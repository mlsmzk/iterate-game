import sys
import random

# Intellect
# Physique
# Wealth
# Connections
# Leadership 
# Fame

class Experience():
    def __init__(self, name, gain, loss):
        self.data = {"name" : name,
                     "gain" : gain,
                     "loss" : loss}

    def __repr__(self):
        s = ""
        for k,v in self.data.items():
            s += (k + " : " + v + "\n")
        return s

class Property():
    def __init__(self, name, desc, gain, loss):
        self.data = {"name" : name,
                     "desc" : desc,
                     "gain" : gain,
                     "loss" : loss}
    def __repr__(self):
        s = ""
        for k,v in self.data.items():
            s += (k + " : " + v + "\n")
        return s

def property_select():
    properties = {
        2: Property("Athleticism", "You do a sport during HS or College", "+5 physique, +3 connections", "None"),
        3: Property("Artistic", "You do a art during HS or College", "+3 fame, +3 connections", "None"),
        4: Property("Leadership", "Anytime you draw a leadership experience card, double the leadership gain", "x2 leadership", "None"),
        5: Property("Single Income Family", "If there is a competition event, or in a fight for college, receive a special boost", "+10 stats required to win", "-10 wealth"),
        6: Property("First Generation", "If there is a competition event, or in a fight for college, roll the die to receive a bonus equal to the number on the die", "Number on the die", "-5 wealth, -5 connections"),
        7: Property("Rich Family", "Gain connections and wealth upon drawing this card", "+10 connections, +10 wealth", "None"),
        8: Property("Impoverished", "All gains in wealth are halved", "Roll die in school selection phase. If the number on the die > 4, add the die's number to the desired stat.", "All wealth gains are worth half as much"),
        9: Property("Family Alumni", "In college selection, gain stat value.", "+10 all required stats for college admission", "-5 fame"),
        10: Property("Mafia", "We'd tell you but we'd have to kill you.", "+10 wealth, +15 connections", "-10 fame")
        }
    return properties[random.randrange(2, 11)]

class School():
    def __init__(self, name, reqs, unlocks, pref):
        self.data = {"name" : name,
                     "reqs" : reqs,
                     "unlocks" : unlocks,
                     "pref" : pref}
    
    def __repr__(self):
        s = ""
        for k,v in self.data.items():
            if isinstance(v, tuple):
                v = v[0] + " and " + v[1]
            s += (k + " : " + v + "\n")
        return s 

def school_select(arg):
    schools = {
        3 : School("Potato", "None", ("ms", "lvl2"), "None"),
        4 : School("Broccoli", "None", ("ms", "lvl2"), "None"),
        5 : School("Carrot", "None", ("ms", "lvl2"), "None"),
        6 : School("Cucumber", "None", ("ms", "lvl1"), "None"),
        7 : School("Eggplant", "None", ("ms", "lvl1"), "None"),
        8 : School("Pumpkin", "None", ("ms", "lvl1"), "None"),
        9 : School("Lettuce", "None", ("ms", "lvl1"), "None"),
        10 : School("Cabbage", "None", ("ms", "lvl1"), "None"),
        11 : School("Seaweed", "None", ("ms", "lvl1"), "None"),

        22 : School("Pineapple", "None", ("hs", "lvl2"), "None"),
        23 : School("Tomato", "None", ("hs", "lvl2"), "None"),
        24 : School("Orange", "None", ("hs", "lvl2"), "None"),
        25 : School("Apple", "None", ("hs", "lvl2"), "None"),
        26 : School("Mango", "None", ("hs", "lvl2"), "None"),
        27 : School("Watermelon", "None", ("hs", "lvl2"), "None"),
        28 : School("Banana", "None", ("hs", "lvl2"), "None"),
        29 : School("Grape", "None", ("hs", "lvl2"), "None"),
        30 : School("Strawberry", "None", ("hs", "lvl2"), "None"),

        42 : School("Chadwick", "intellect > 30, or intellect > 20 and leadership > 5, or wealth > 20", ("c", "lvl3"), "wealth"),
        43 : School("Cumin", "total stats > 20", ("c", "lvl3"), "None"),
        44 : School("Cinnamon", "fame > 2, or intellect > 21, or student attended strawberry", ("c", "lvl4"), "fame"),
        45 : School("Black Pepper", "None", ("c", "lvl3"), "None"),
        46 : School("Oregano", "Physique > 10 and intellect > 10", ("c", "lvl3"), "None"),
        47 : School("Basil", "total stats > 30", ("c", "lvl3"), "None"),
        48 : School("Paprika", "total stats > 40", ("c", "lvl3"), "None"),
        49 : School("Garlic", "intellect > 10", ("c", "lvl4"), "None"),
        50 : School("Lavender", "intellect > 15 and connections > 10", ("c", "lvl3"), "connections"),
    
        62 : School("Olin College of Engineering", "intellect > 50, or intellect > 35, wealth > 10 and leadership > 10", "lvl5", "intellect"),
        63 : School("Harvard", "intellect > 25, connections > 20, wealth > 25", "lvl5", "wealth"),
        64 : School("Community College", "total > 30", "lvl5", "None"),
        65 : School("UCLA", "intellect > 35, physique > 10, wealth > 5", "lvl5", "None"),
        66 : School("Stanford", "intellect > 50, wealth > 10, connections > 10, or fame > 12", "lvl5", "fame"),    
        67 : School("UC Riverside", "intellect > 20, total > 40", "lvl5", "None"),
        68 : School("University of Illinois Urbana-Champaign", "intellect > 20, total > 40", "lvl5", "None")
    }
    if arg == "c":
        return schools[random.randrange(62,69)]
    if arg == "hs":
        return schools[random.randrange(42,51)]
    if arg == "ms":
        return schools[random.randrange(22,31)]
    if arg == "es":
        return schools[random.randrange(3, 12)]
        

if __name__ == "__main__":
    if sys.argv[1] == "school":
        card = school_select(sys.argv[2])
    elif sys.argv[1] == "property":
        card = property_select()
    print(card)