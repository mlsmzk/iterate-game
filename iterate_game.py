import sys
import random

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
        63 : School("Harvard", "intellect > 25, connections > 20, wealth > 25", "lvl5", "wealth")
    }
    if arg == "c":
        return schools[random.randrange(62,64)]
    if arg == "hs":
        return schools[random.randrange(42,51)]
    if arg == "ms":
        return schools[random.randrange(22,31)]
    if arg == "es":
        return schools[random.randrange(3, 12)]
        

if __name__ == "__main__":
    if sys.argv[1] == "school":
        card = school_select(sys.argv[2])
    print(card)