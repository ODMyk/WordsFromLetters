from os import system
import sys
if sys.argv[0].endswith('.py'):
	path = sys.argv[0]+'\\..\\Text.txt'
else:
	path = sys.argv[0]+'\\Text.txt'
with open(path, "r") as f:
    string = f.read()
mydict = {}
string = string.lower()
lst = []
while True:
    system("cls")
    print(string,"\n")
    print("Chosen symbols: ",lst,"\n")
    x = input("Enter symbol that you need to calculate. Dont forget about language!\nIf you want to start calculating - enter GO\n").lower()
    if x == "go":
        break
    else:
        if len(x)==1:
            if x not in lst:
            	mydict[x] = 0
            	lst.append(x)
        else:
            print("Hmm. It's not a single symbol! Please enter only 1 symbol.")
            input("Press ENTER to continue.")
for el in mydict:
    for text in string:
        if el == text:
            mydict[el] = mydict[el]+1
    val = mydict[el]
    print("\nSymbol '{0}' was used {1} times.".format(str(el), str(val)))
input("\nPress ENTER to exit.")
