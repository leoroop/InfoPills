import sys

if len(sys.argv) != 4:
    print("ERRORE: numero di argomenti non corretto")
    exit(-1)

print("Operazione: " + sys.argv[1] + " " + sys.argv[2] + " " + sys.argv[3])

operand1 = int(sys.argv[1])
operator = sys.argv[2]
operand2 = int(sys.argv[3])

if operator == "+":
    print("Risultato: %d" % (operand1 + operand2))
elif operator == "-":
    print("Risultato: %d" % (operand1 - operand2))
elif operator == "*" or operator == "x":
    print("Risultato: %d" % (operand1 * operand2))
elif operator == "/":
    print("Risultato: %.2f" % (operand1 / operand2))
else:
    print("ERRORE: operazione sconosciuta")
