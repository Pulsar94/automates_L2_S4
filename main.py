table = {}
def register_auto(num):
    table[num] = {}
    with open("automate/5-1.txt") as auto:
        for line in auto.readlines():
            line = "".join(line.split("\n"))
            line = " ".join(line.split("\t"))
            Table_Automate = line.split(" ")
            for value in range(len(Table_Automate)-1):
                table[num][Table_Automate[1]].append(Table_Automate[value])


def longest_auto(num):
    long = 0
    for auto in table[num]:
        if len(auto) > long:
            long = len(auto)
    return long

def show_table_auto(num):
    print("---"+"---"*longest_auto(num)+"---")
    for auto in table[num]:
        print("|", end="")
        for auto2 in auto:
            print(auto2+"|", end="")
    print("")
    print("---" + "---" * longest_auto(num) + "---")

def show_graph_auto():
    pass

register_auto(1)
print(table[1])
show_table_auto(1)