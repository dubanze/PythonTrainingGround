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

# PROGRAM WROZBY
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


# RZUCANIE MONETA I LICZENIE "ORLOW" I "RESZEK"
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

# GRA ZGADNIJ LICZBĘ W OKREŚLONEJ ILOŚCI PROB
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

# PROGRAM LICZACY ZA UŻYTKOWNIKA
# startint = int(input("Podaj liczbę początkową: "))
# endint = int(input("Podaj liczbę końcową: "))
# step = int(input("Podaj krok z jakim mam liczyć: "))

# print("Wypisuję liczby zgodnie z podanym zakresem: \n")
# for i in range(startint, endint+1, step):
#     print(i)

# input("Naciśnij klawisz, aby zakończyć.")

# ##### PROGRAM ODWRACAJACY LANCUCH ZNAKOW
# usrword = input("Podaj słowo: ")
# end = len(usrword)
# newword = ""

# for letter in usrword:
#     end -= 1
#     newword = newword + usrword[end]

# print(newword)
# input("Naciśnij klawisz, aby zakończyć.")

# MODYFIKACJA WYMIESZANYCH LITER
# import random

# # utwórz sekwencję słów do wyboru
# WORDS = ("python",
#          "anagram",
#          "łatwy",
#          "skomplikowany",
#          "odpowiedź",
#          "ksylofon")

# HINTS = {"python": "gatunek weza, w ktorym progamujesz",
#          "anagram": "wyraz powstajacy w wyniku poprzestawiania liter",
#          "łatwy": "kiedy test nie jest trudny, tylko...",
#          "skomplikowany": "inaczej bardzo zlozony",
#          "odpowiedź": "zwykle probujemy ja od kogos uzyskac",
#          "ksylofon": "gra sie na nim cymbalkami"}
# word = random.choice(WORDS)
# correct = word
# jumble = ""  # pusty lancuch na pomieszane slowo
# hinttrigger = 0

# while word:
#     position = random.randrange(len(word))
#     jumble += word[position]
#     word = word[:position] + word[(position + 1):]

# # rozpocznij grę
# print(
#     """
#            Witaj w grze 'Wymieszane litery'!

#    Uporządkuj litery, aby odtworzyć prawidłowe słowo.
# (Aby zakończyć zgadywanie, naciśnij klawisz Enter bez podawania odpowiedzi.)
# """
# )
# print("Zgadnij, jakie to słowo:", jumble, "\nJeśli potrzebujesz podpowiedzi, wpisz słowo help.")

# guess = input("\nTwoja odpowiedź: ")
# while guess != correct and guess != "":
#     if guess == "help":
#         hinttrigger = 1
#         print(HINTS[correct])
#         guess = input("\nTwoja odpowiedź: ")
#     elif guess != correct:
#         print("Niestety, to nie to słowo.")
#         guess = input("Twoja odpowiedź: ")

# if guess == correct and hinttrigger == 0:
#     print("\nElegancko, zgadłeś bez korzystania z podpowiedzi!\nWygrałeś uścisk ręki prezesa!")
# elif guess == correct and hinttrigger == 1:
#     print("\nNom, spoczko, zgadłeś, ale wykorzystałeś do tego podpowiedź.\nNie otrzymujesz dodatkowych punktów!")
# elif guess == "":
#     print("\nSzkoda, ze nie podałeś zadnej odpowiedzi.")

# print("Dziękuję za udział w grze.")

# input("\nAby zakończyć program, naciśnij klawisz Enter.")

# GRA W ZGADYWANIE SLOWA NA PODSTAWIE ILOSCI LITER
# import random
# from typing import Counter

# WORDS = ("samochód",
#          "krzesło",
#          "masakra",
#          "skomplikowany",
#          "wiertarka",
#          "materac")

# word = random.choice(WORDS)
# correct = word

# print("Słowo, które masz odgadnąć, zawiera " + str(len(correct)) + " liter.")


# print("Mozesz pięciokrotnie podać jakąś literę, a ja powiem Ci ile razy \
#     znajduje się ona w tym słowie. Potem będziesz musiał je zgadnąć.")

# letter = input("Podaj literę: ").lower()

# if word.count(letter) > 0:
#     print("Tak, litera " + letter + " znajduje się w tym słowie.")
# else:
#     print("Nie, litera " + letter + " nie znajduje się w tym słowie.")

# # if letter != "":
# #     print("Litera " + letter + " występuje w tym słowie " + str(word.count(letter)) + " razy.")

# tries = 1

# while letter != "" and tries < 5:
#     letter = input("Mozesz podać następną: ").lower()
#     if word.count(letter) > 0:
#         print("Tak, litera " + letter + " znajduje się w tym słowie.")
#     else:
#         print("Nie, litera " + letter + " nie znajduje się w tym słowie.")
#     # print("Litera " + letter + " występuje w tym słowie " + str(word.count(letter)) + " razy.")
#     tries += 1

# if letter == "":
#     print("Szkoda, ze nie podałeś zadnej litery.")

# if tries == 5:
#     usrword = input("Odgadnij teraz proszę jakie to słowo?: ")
#     if usrword.lower() == correct:
#         print("Brawo! Zgadłeś.")
#     elif usrword.lower() != correct:
#         print("Niestety, spróbuj ponownie!")

# input("Naciśnij Enter, aby zakończyć.")

# PROGRAM WYPISUJACY LOSOWO SLOWA, A NASTEPNIE USUWAJACY JE
# import random

# WORDS = ["samochód",
#          "krzesło",
#          "masakra",
#          "skomplikowany",
#          "wiertarka",
#          "materac"]

# length = len(WORDS)

# while length > 0:
#     index = random.randrange(length)
#     print(WORDS[index])
#     del WORDS[index]
#     length -= 1

# input("Naciśnij Enter, aby zakończyć.")


# ##### PROGRAM KREATOR POSTACI
# from time import sleep

# attributes = {"siła" : 0,
#               "zdrowie" : 0,
#               "mądrość" : 0,
#               "zręczność" : 0}

# availpoints = 30

# def printCurrentAttrState():
#     print("Stan wszystkich atrybutów w tym momencie: ")
#     print("ATRYBUT\t\tPUNKTY")
#     for i in attributes:
#         print(i + "\t\t" + str(attributes[i]))
#     sleep(2)

# def printOptions():
#     print("Wybierz opcję z menu ponizej, aby rozpocząć:\n")
#     print("1 - dodanie punktów do atrybutu\n")
#     print("2 - odjęcie punktów do atrybutu\n")
#     print("3 - wyświetl obecny stan wszystkich atrybutów\n")
#     print("0 - wyjście z kreatora\n")

# def printAvailablePoints():
#     print("Obecna ilość punktów w puli to: " + str(availpoints))

# print("Witaj w kreatorze postaci!\n")
# printOptions()

# option = None

# while option != "0":
#     option = input("Co chcesz teraz zrobić?: ")
#     if option == "1" and availpoints > 0:
#         attribute = input("Podaj atrybut na który chcesz przeznaczyć punkty: ")
#         points = int(input("Podaj ile punktów chcesz przeznaczyć z dostępnej puli: "))
#         attributes[attribute] += points
#         availpoints -= points
#         print("Zwiększyłeś ilość punktów atrybytu " + attribute + " o " + str(points) + " punktów.\n" )
#         sleep(1)
#         printAvailablePoints()
#         sleep(3)
#         printOptions()
#     elif option == "1" and availpoints <= 0:
#         print("Brak wolnych punktów! Mozesz je odjąć od któregoś z atrybutów i spróbować ponownie.")
#         sleep(2)
#         printOptions()
#     elif option == "2":
#         attribute = input("Podaj atrybut od którego chcesz odjąć punkty: ")
#         points = int(input("Podaj ile punktów chcesz odjąć od atrybutu i dodać z powrotem do puli: "))
#         attributes[attribute] -= points
#         availpoints += points
#         print("Odjąłeś " +  str(points) + " punktów od atrybytu " + attribute + ".\n")
#         sleep(1)
#         printAvailablePoints()
#         sleep(3)
#         printOptions()
#     elif option == "3":
#         printCurrentAttrState()
#         printOptions()

# print("Do zobaczenia!")
# input("Naciśnij Enter, aby zakończyć.")

#### PROGRAM KTO JEST TWOIM OJCEM?
#### UDOSKONALONY O PODAWANIE KTO JEST DZIADKIEM
# from time import sleep


# familydictionary = {"Marian Trep": "Sławomir Trep",
#                     "Łukasz Nowak": "Paweł Nowak",
#                     "Mateusz Kizio": "Piotr Kizio",
#                     "Krzysztof Sordyl": "Marcin Sordyl",
#                     "Piotr Kizio": "Zenon Kizio"}


# def printOptions():
#     print("Wybierz opcję z menu ponizej, aby rozpocząć:\n")
#     print("1 - dodanie nowej lub aktualizacja istniejącej pary syn-ojciec\n")
#     print("2 - usunięcie pary syn-ojciec\n")
#     print("3 - informacja na temat dziadka syna\n")
#     print("0 - zakończenie programu\n")


# choice = None

# print("Witaj w programie 'Kto jest Twoim tatą?'")
# printOptions()

# while choice != "0":
#     choice = input("Co chcesz teraz zrobić?: ")
#     if choice == "1":
#         newson = input(
#             "Podaj imię i nazwisko syna, które chcesz dodać lub zmodyfikować: ")
#         newfather = input(
#             "Podaj imię i nazwisko ojca, które chcesz dodać lub zmodyfikować: ")
#         familydictionary[newson] = newfather
#         print("Para dodana!")
#         sleep(2)
#         printOptions()
#     if choice == "2":
#         pairtodel = input(
#             "Podaj imię i nazwisko syna z pary, którą chcesz usunąć: ")
#         if pairtodel in familydictionary:
#             del familydictionary[pairtodel]
#             print("Para usunięta!")
#             sleep(2)
#             printOptions()
#         else:
#             print("Para z takim synem nie istnieje!")
#             sleep(2)
#             printOptions()
#     if choice == "3":
#         whoisgrandfather = input(
#             "Podaj imię i nazwisko syna, aby dowiedzieć się kto jest jego dziadkiem: ")
#         if whoisgrandfather in familydictionary:
#             print("Ojcem " + whoisgrandfather + " jest " +
#                   familydictionary[whoisgrandfather], end=",")
#             newson = familydictionary[whoisgrandfather]
#             if newson in familydictionary:
#                 print(" a jego dziadkiem jest " + familydictionary[newson] + "\n")
#                 sleep(2)
#                 printOptions()
#             else:
#                 print(" ale niestety nie posiadam informacji na temat jego dziadka.\n")
#                 sleep(2)
#                 printOptions()
#         else:
#             print("Przykro mi, nie posiadam informacji na temat tego syna.\n")
#             sleep(2)
#             printOptions()


# print("Do widzenia!")
