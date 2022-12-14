from multiprocessing import Event
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

def experience_select(lvl):
    experiences = {
        3 : Experience("Arts and Crafts", "+3 intellect", "None"),
        4 : Experience("Elementary Instruments", "+5 intellect", "None"),
        5 : Experience("Band", "+3 connections", "None"),
        6 : Experience("Cooking Class", "+3 connections", "None"),
        7 : Experience("Story Time", "+2 intellect", "None"),
        8 : Experience("Reading Class", "+5 intellect", "None"),
        9 : Experience("Math Extended Class", "+5 intellect", "None"),
        10 : Experience("Afterschool Choir", "+3 connections", "None"),
        11 : Experience("Afterschool Study Group", "+3 connections", "None"),
        
        14 : Experience("Archery Club", "+6 physique", "None"),
        15 : Experience("Chess Club", "+7 intellect", "None"),
        16 : Experience("Soccer", "+7 physique", "None"),
        17 : Experience("Theatre Tech", "+5 connections", "None"),
        18 : Experience("Drama Club", "+5 connections", "None"),
        19 : Experience("Cross Country", "+7 physique", "None"),
        20 : Experience("Student Council", "+5 connections, +5 leadership, +2 fame", "None"),
        21 : Experience("Journalism", "+6 connections", "None"),
        22 : Experience("Jazz Band", "+6 connections", "None"),
        23 : Experience("Rock Band", "+6 connections", "None"),

        26 : Experience("Robotics Club", "+10 intellect, +5 connections", "None"),
        27 : Experience("MUN", "+10 intellect, +7 connections", "None"),
        28 : Experience("Mu Alpha Theta", "+10 intellect", "None"),
        29 : Experience("Student Council", "+10 connections, +5 leadership, +2 fame", "None"),
        30 : Experience("Track and Field", "+10 physique", "None"),
        31 : Experience("Football", "+10 physique", "None"),
        32 : Experience("Cheerleading", "+10 physique", "None"),
        33 : Experience("Yearbook", "+5 connections", "None"),
        34 : Experience("Orchestra", "+10 connections", "None"),
        35 : Experience("Swimming", "+10 physique", "None"),

        38 : Experience("Acapella", "+7 connections", "None"),
        39 : Experience("Ultimate Frisbee", "+12 physique", "None"),
        40 : Experience("Formula", "+12 intellect, +10 connections", "None"),
        41 : Experience("Campus Newspaper", "+7 connections", "None"),
        42 : Experience("Service Club", "+15 connections", "None"),
        43 : Experience("Photography Club", "+7 connections", "None"),
        44 : Experience("Choir", "+7 connections", "None"),
        45 : Experience("Dance", "+10 physique, +5 connections", "None"),
        46 : Experience("Hockey", "+10 physique, +5 connections", "None"),
        47 : Experience("Habitat for Humanity", "+12 connections", "None"),

        50 : Experience("Student Government", "+15 connections, +10 leadership, +5 fame", "None"),
        51 : Experience("Equestrian Club", "+15 physique, +9 connections", "None"),
        52 : Experience("Aerospace Engineering", "+15 intellect", "None"),
        53 : Experience("Hackathon team", "+13 intellect, +6 connections", "None"),
        54 : Experience("ROTC", "+15 physique, +5 connections", "None"),

        57 : Experience("D1 Sports", "+20 physique, +15 connections, +10 fame, +8 wealth", "None"),
        58 : Experience("Secret Society", "+20 connections, +15 fame, +8 wealth", "None"),
        59 : Experience("Honor Society", "+15 intellect, +15 connections, +5 fame", "None")
    }
    if int(lvl) == 1:
        return experiences[random.randrange(3, 12)]
    elif int(lvl) == 2:
        return experiences[random.randrange(14,24)]
    elif int(lvl) == 3:
        return experiences[random.randrange(26, 36)]
    elif int(lvl) == 4:
        return experiences[random.randrange(38, 48)]
    elif int(lvl) == 5:
        return experiences[random.randrange(50,55)]
    else:
        return experiences[random.randrange(57, 60)]

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
    
class Events():
    def __init__(self, name, loses, gains, desc):
        self.data = {"name" : name,
                     "reqs" : loses,
                     "unlocks" : gains,
                     "pref" : desc}
    
    def __repr__(self):
        s = ""
        for k,v in self.data.items():
            if isinstance(v, tuple):
                v = v[0] + " and " + v[1]
            s += (k + " : " + v + "\n")
        return s 
        
def event_select():
    events = {
        2: Events("Car Crash", "-5 wealth, -10 physique", "None", "None"),
        3: Events("Robotics Competition", "None","10 Intellect, 10 Fame", "Needs 2 students with robotics club experience card. Compare Intellect stat within joined players, and players may add additional points to their intellect temporarily with connections and wealth. These points expire after use."),
        4: Events("Failed in Class", "-10 intellect", "None", "Cannot progress to next level of education for 1 extra turn."),
        5: Events("Soccer Competition", "None", "10 Physique, 5 Fame", "If Physique is > 30, or intellect + physique > 45 then gian points."),
        6: Events("First place in class", "None", "5 Fame", "You placed first place in an exam in class."),
        7: Events("Drugs", "-5 Fame, -10 Physique, -5 intellect", "2 connection", "You started to do drugs."),
        8: Events("Alcohol Poisoning", "-10 Physique", "None", "You got alcohol poisoning from a party."),
        9: Events("Party", "None", "5 Connection, 2 Fame", ""),
        10: Events("Competition", "None", "5 Stats of first stat listed in activity.", "If you are the only person in the group to hold an activity, then add 5 points to the first stat the activity lists. If else, the highest person with the first stat takes 5 points."),
        11: Events("Musical", "None", "5 Fame, 2 connection", "You performed in a musical. Take the stats only if you are a part of drama club, theater tech, or anything related to music"),
        12: Events("Epidemic", "-5 Physique", "None",""),
        13: Events("Prom King/Queen", "None", "10 Fame , 10 connection", "Compare fame points with the players. The player with the highest fame points wins prom king/queen."),
        14: Events("Scandal","-10 Fame, -5 Connection", "None", "There was a scandal involving you. ")
        }
    return events[random.randrange(2, 15)]

if __name__ == "__main__":
    if sys.argv[1] == "school":
        card = school_select(sys.argv[2])
    elif sys.argv[1] == "property":
        card = property_select()
    elif sys.argv[1] == "event":
        card = event_select()
    elif sys.argv[1] == "exp":
        card = experience_select(sys.argv[2])
    print(card)