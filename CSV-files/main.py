#from prettytable import from_csv
#
#with open("characters.csv") as fp:
#    mytable = from_csv(fp)
#print(mytable)

Table = []
file = open("characters.csv","r")
for line in file:
    line = line.strip()
    SH = line.split(",")
    Table.append([SH])

print(Table)