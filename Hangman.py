name = input("Adını Gir =")
print("Hoşgeldin " + name + " --> Haydi Adam Asmaca Oyunu Oynayalım")

secret_word = ("Metallica")

guess_string = ""

lives = (10)

while lives > 0:

	character_left = 0

	for character in secret_word:

		if character in guess_string:
			print(character)
		else:
			print("-")
			character_left += 1

	if character_left == 0:
		print("You won")
		break


	guess = input("Guess a letter: ")
	guess_string += guess

	if guess not in secret_word:
		lives -= 1
		print("Wrong Guess!")
		print(f"You have {lives} left") ##Formatting ile süslü parantezde değişken belirttik

		if lives == 0:
			print("You died!")
