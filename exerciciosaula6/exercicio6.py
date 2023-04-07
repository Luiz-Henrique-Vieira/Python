nota1=float(input("digite a primeira nota principal: "))
nota2=float(input("digite a segunda nota principal: "))

media=(nota1+nota2)/2

if media>=9 and media<=10:
    print("Aprovado")
    print("conceito A")

elif media>=7.5 and media<=8.9:
    print("Aprovado")
    print("conceito B")

elif media>=6 and media<=7.4:
    print("Aprovado")
    print("conceito C")

elif media>=4.0 and media<=5.9:
    print("Aprovado")
    print("conceito D")

else: 
    
    print("reprovado")
    print("conceito E")