import sys


def calcolo(op1, opr, op2):
    print("Operazione: %s %s %s" % (op1, opr, op2))
    if opr == "+":
        print("Risultato: %d" % (op1 + op2))
    elif opr == "-":
        print("Risultato: %d" % (op1 - op2))
    elif opr == "*" or opr == "x":
        print("Risultato: %d" % (op1 * op2))
    elif opr == "/":
        print("Risultato: %.2f" % (op1 / op2))

    print("")


if len(sys.argv) != 4:
    print("ERRORE: numero di argomenti non corretto")
    exit(-1)

print("Operazione: " + sys.argv[1] + " " + sys.argv[2] + " " + sys.argv[3])

operand1 = int(sys.argv[1])
operator = sys.argv[2]
operand2 = int(sys.argv[3])

calcolo(operand1, operator, operand2)
