num_int = 5
num_dec = 10.5
val_str = "um texto qualquer"
"""
print(type(num_int))
print(type(num_dec))
print(type(val_str))
"""
print("\n")
print("O valor de 'num_int' é:",num_int) #Concatenamos um texto com outro valor qualquer usando uma vírgula para separá-los
print("O valor de 'num_int' é: %i" %num_int) # Usando os marcadores de porcetagem para concatenar str com outros tipos de dados
print("O valor de 'num_int' é: " + str(num_int)) # converte um valor inteiro em str e concatena com o texto anterior

print("\n")
print("Concatenando decimal: ", num_dec)
print("Concatenando decimal: %.2f" %num_dec)
print("Concatenando decimal: " + str(num_dec))

print("\n")
print("Concatenando Strings:", val_str)
print("Concatenando Strings: %s" %val_str)
print("Concatenando Strings: " + str(val_str))
