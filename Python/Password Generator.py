import random as r 

main = []
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890$@^`,|%;.~()/\{}:?[]=-+_#!"

for character in characters:
	main.append(character)

lenght = input("Enter password lenght: ")
password = []

for i in range(lenght):
	password.append(r.choice(main))
	print ''.join(password)

print "Final password:"
print ''.join(password)
