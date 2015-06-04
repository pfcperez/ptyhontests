"""
Multiplayer game (two players)
One letter at the time

Choose Game Lenght, how many rounds [enter a number larger than 0]?  	

Se utilizara el programa de Alice tomando la informacion del archivo txt

The word Games
======================

Round 1

Player 1: 0 Player 2:0

Player 1, Please enter a letter:

Current String "a"

Player 2, Please enter a letter:
Current String "al"

Yeiiiiii

Winning word = "alice"

Player 2 just won that round!! (221 points)

ROund 2
Player 1:0 Player 2: 221
"""
from random import randint

def words_pop(f):
	words = []
	for line in f:
		list_of_words = line.split()
		for w in list_of_words:
			words.append(w.lower())
	print words
	return words


def main():

	print "The word Games"
	print "======================"

	print "Choose Game Lenght, how many rounds [enter a number larger than 0]? "
	times = int(raw_input(' '))
	file2 = open('alice.txt', 'rU')
	words_choose = words_pop(file2)
	words_length = len(words_choose)
	print words_length
	try:

		if times >0:
			index = randint(words_length)
			#print index
			for n in range(1, times):
				print file2

		else:
			print 'Number should greater than 0'
	except:
		print 'Not valid....'

if __name__ == '__main__':
	main()






