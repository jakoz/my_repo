__author__ = 'Jakub'
import sys
import operator

#python WorkWithFile.py plik.txt
with open(sys.argv[1], 'rt') as f:
    data = f.read()


counter_words = data.split().__len__()
counter_tabs = data.split('\t').__len__()-1
counter_chars = data.__len__()
counter_spaces = data.split(' ').__len__() - counter_tabs - 1 + counter_tabs*1
counter_sentences = 0
counter_letters = 0

my_dictionary = {}
list_of_end_sentences = ['!', '?', '.']

for letter in data:
    ######## ZNAKI SPECJALNE ZADEKLAROWANE W LISCIE #########
    if letter in list_of_end_sentences:
        counter_sentences += 1
    elif letter.isalpha():
        counter_letters += 1
    ######## DODANIE DO SLOWNIKA #########
    if letter in my_dictionary.keys():
        my_dictionary[letter] += 1
    else:
        my_dictionary[letter] = 1

print "Liczba znakow : ", counter_chars
print "Liczba liter : ", counter_letters             #Pominiete spacje, akapity, kropki, przecinki
print "Liczba zdan : ", counter_sentences
print "Liczba slow : ", counter_words
print "Liczba akapitow : ", counter_tabs


#### ZAKLADAM ZE ZDANIE KONCZY SIE POPRAWNIE ( KROPKA, WYKRZYKNIk ) ########
average_amount_of_letters = 0.0
average_amount_of_words = 0.0
try:
    average_amount_of_letters = float(counter_letters)/counter_words
except ZeroDivisionError:
    print "Pusty plik"
try:
    average_amount_of_words = float(counter_words)/counter_sentences
except ZeroDivisionError:
    print "Brak zdan"

print "Srednia ilosc liter w wyrazie : ", average_amount_of_letters
print "Lub przyblizajac : ", round(average_amount_of_letters, 0)
print "Srednia ilosc wyrazow w zdaniu : ", average_amount_of_words
print "Lub przyblizajac : ", round(average_amount_of_words, 0)

sorted_values = sorted(my_dictionary.items(), key=operator.itemgetter(1))
print "Trzy najczesciej wystepujace elementy : ", sorted_values[-3:]
