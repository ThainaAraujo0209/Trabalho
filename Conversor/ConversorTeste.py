print("=== Conversor de Temperaturas ===")
print("1 - Converter Fahrenheit para Celsius")
print("2 - Converter Celsius para Fahrenheit")

opcao = input("Escolha uma opção (1 ou 2): ")

if opcao == "1":
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"{fahrenheit}°F equivale a {celsius:.2f}°C")

elif opcao == "2":
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"{celsius}°C equivale a {fahrenheit:.2f}°F")

else:
    print("Opção inválida! Tente novamente.")