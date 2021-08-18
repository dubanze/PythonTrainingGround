# strlist = []
# intlist = []

# strlist.append(input("Serwis: "))
# strlist.append(input("Apartament: "))
# strlist.append(input("Samolot: "))
# strlist.append(input("Obiady: "))
# strlist.append(input("Podarunki: "))
# strlist.append(input("Gry: "))
# strlist.append(input("Słuzba: "))


# for i in strlist:
#     intlist.append(int(i))

# total = print("Całkowite wydatki: ", sum(intlist))

### PROGRAM WROZBY 
# import random as r

# fortunes = []
# fortunes.append("Dzisiaj będziesz miał sraczkę.")
# fortunes.append("Jutro wygrasz milion.")
# fortunes.append("Dzisiaj skończy Ci się herbata.")
# fortunes.append("Jutro kogoś spotkasz.")
# fortunes.append("Dzisiaj wyłączą Ci prąd.")

# today_fortune = r.choice(fortunes)

# question = input("Siemanko, czy chcesz usłyszeć wrózbę na dzisiaj?\n").lower()

# if question == "tak":
#     print(today_fortune)
# elif question == "nie":
#     print("To się pocałuj w dupę.")
# else:
#     print("Co Ty, głupi jesteś? Nie umiesz odpowiadać na proste pytania?")

# input("Naciś enter, zeby skończyć, igzde.")


### RZUCANIE MONETA I LICZENIE "ORLOW" I "RESZEK"
# from random import choice

# throws = []
# elements = ["orzeł","reszka"]
# iterator = 1

# while iterator <= 100:
#     throws.append(choice(elements))
#     iterator += 1

# print("Tyle wypadło orłów: ", str(throws.count("orzeł")) + ",\n")
# print("a tyle reszek:", str(throws.count("reszka")))

# input("Naciś enter, zeby skończyć, igzde.")

### GRA ZGADNIJ LICZBĘ W OKREŚLONEJ ILOŚCI PROB
# import random

# genint = random.randint(1,100)
# iterator = 1
# while iterator <= 15:
#     usrint = int(input("Podaj liczbę: "))
#     if usrint > genint:
#         print("Za duza liczba!")
#     elif usrint < genint:
#         print("Za mala liczba!")
#     elif usrint == genint:
#         print("Brawo! Zgadles, zajelo Ci to " + str(iterator) + " prób.")
#         break
#     iterator += 1
# else:
#     print("Niestety, nie udało Ci sie zgadnac liczby.")
# input("Naciśnij klawisz aby zakończyć.")


# ### GRA KOMPUTER ZGADUJE LICZBE
# from time import sleep

# def rangewithend(start, end):
#     return range(start, end+1)

# def findMiddle(input_list):
#     middle = float(len(input_list))/2
#     if middle % 2 != 0:
#         return input_list[int(middle - .5)]
#     else:
#         return input_list[int(middle)]

# start = 1
# end = 100
# iterator = 0

# liczba = int(input("Człowieku, podaj liczbe do odgadniecia!\n"))
# while iterator <= 15:
#     iterator += 1
#     chooseint = int(findMiddle(rangewithend(start,end)))
#     print("Zgaduje liczbe " + str(chooseint))
#     if liczba > chooseint:
#         print("Dalem za malo!")
#         start = chooseint
#         sleep(5)
#     elif liczba < chooseint:
#         print("Dalem za duzo!")
#         end = chooseint
#         sleep(5)
#     elif liczba == chooseint:
#         print("Zgadlem! Ta liczba to " + str(chooseint) + ", a zajelo mi to " + str(iterator) + " prob!")
#         break    
# else:
#     print("Nie udalo mi sie zgadnac.")

# input("Nacisnij klawisz aby zakonczyc.")

#####
  




