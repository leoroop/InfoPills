# I commenti sono utili anche per "rimuovere" parti di codice che non vogliamo eseguire

##################################################################################################
# x = 10  # Una variabile definita così è detta Globale, ed è visibile ovunque
# if x < 5:
# 	y = x * 2
# y è una variabile globale, ma viene istanziata all'interno di un blocco
# quindi sarà visibile SOLO se si entra effettivamente nel blocco

# print(y)
# z = y * 3
# print(z)

##################################################################################################
# def f(x, y):
# 	k = 4
# 	return (x + y) * k


# def test(arg1, arg2):
# 	print(arg1)
# 	print(k)  # Questa istruzione non funzionerà, generando un errore e facendo uscire l'interprete
# 	print(arg2)

# print(f(4,5))
# test("Ciao", "a tutti")

##################################################################################################
# k = 4  # k è diventata globale


# def f(x, y):
# 	return (x + y) * k


# def test(arg1, arg2):
# 	print(arg1)
# 	print(k)
# 	print(arg2)


# print(f(4, 5))
# test("Ciao", "a tutti")

##################################################################################################
# def f(x, y):
# 	k = 4
# 	return (x + y) * k


# def test(arg1, arg2, k):
# 	print(arg1)
# 	print(k)
# 	print(arg2)


# print(f(4, 5))
# test("Ciao", "a tutti", 4)  # Notare che qui la chiamata è cambiata ed è stato passato il valore 4 come valore per k

def f(x, y, k):
	return (x + y) * k


def test(arg1, arg2, k):
	print(arg1)
	print(k)
	print(arg2)


def main():
	k = 4
	print(f(4, 5, k))
	test("Ciao", "a tutti", k)


if __name__ == '__main__':
	main()
