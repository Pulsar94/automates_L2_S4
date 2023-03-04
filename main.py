table = {}
alphabet = "abcdefghijklmnopqrstuvxyz"
def register_auto(num):
    table[num] = {}
    with open("automate/5-"+str(num)+".txt") as auto:
        for line in auto.readlines():
            line = "".join(line.split("\n"))
            line = " ".join(line.split("\t"))
            Table_Automate = line.split(" ")
            table[num][Table_Automate[1]] = Table_Automate


def longest_auto(num):
    long = 0
    for auto in table[num]:
        if len(auto) > long:
            long = len(auto)
    return long

def show_table_auto(num):
    print("Affichage table n°"+str(num)+":")
    print("-"+"----"*(longest_auto(num)+3))
    print("|I/O|sta| ", end="")
    for i in range(0,longest_auto(num)+1):
        print(alphabet[i] + " | ", end="")
    print("")
    print("-"+"----"*(longest_auto(num)+3))
    for auto in table[num]:
        print("| ", end="")
        for auto2 in table[num][auto]:
            print(auto2+" | ", end="")
        print("")
    print("-"+"----"*(longest_auto(num)+3))

def show_graph_auto():
    pass

register_auto(1)
show_table_auto(1)