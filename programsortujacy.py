# '''
# ostatnia wersja zrobionego filtra powtarzających się wystąpień
# '''

with open("3_paragraph_of_lorem.txt", "r") as opened_file:
    list_of_lines = []
    list_of_words = []
    for line in opened_file:
        list_of_lines.append(line)
        split_line = line.split()
        for word in split_line:
            list_of_words.append(word)
            split_word = word.split()
testListDict = {}
for item in list_of_words:
  try:
    testListDict[item] += 1
  except:
    testListDict[item] = 1

for word, number in testListDict.items():
     if number > 1:
        print(word)
        # assert word == "tincidunt"

# with open("3_paragraph_of_lorem.txt", "r") as opened_file:
#     # print(opened_file.read())
#     list_of_lines = []   #zmienna list of lines
#     list_of_words = []   #zmienna list of words
#     # word_counter = 0
#     for word in opened_file:
#         split_word = word.split()
#         list_of_words.append(word)
#         print(list_of_words)
        # for word in split_word:
        #
            # print(list_of_words)
#
# print([word for word in list_of_words if list_of_words.count(word) > 1 ])
# list_of_words = []
# for word in list_of_words:
#     if list_of_words.count(word) > 1:
#         print(word)
# #
# #
# #

# with open("3_paragraph_of_lorem.txt", "r") as opened_file:
#     list_of_lines = []
#     list_of_words = []
#     for line in opened_file:
#         list_of_lines.append(line)
#         split_line = line.split()
#         for word in split_line:
#             list_of_words.append(word)
#             split_word = word.split()
# testListDict = {}
# for item in list_of_words:
#   try:
#     testListDict[item] += 1
#   except:
#     testListDict[item] = 1
# for word, number in testListDict.items():
#     if number > 1:
#         print(word)

    # except:
    #     powtorki[word] = 1
# for word in lista_slow:
#     if


# Najpierw otwieramy plik. do zmiennej otwarty_plik
# lista_slow = []
# for otwarty_plik: wszystkie słowa z tego pliku musimy podzielić na listę z elementami które dzielą się co każdą spację w tym pliku
# Kiedy już mamy utworzoną listę lista_slow = ["slowo1", "slowo2" itd]
# To należy porównać for words in lista_slow
# instrukcja: czy words count jest > 1
# if True
#     print(words)

# porównywanie word_count?!??

# Podaj różnicę między użyciem continue, break i pass.
# Czym się różnią te trzy metody.

# Możesz jeszcze w programie rzucać wyjątkiem. Albo w funkcji.
# Jakbyś chciał przed czymś zabezpieczyć.
# Od tego jest raise