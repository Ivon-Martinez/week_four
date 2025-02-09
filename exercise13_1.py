#create a new file called pelican to open and append to it
pelican = open('pelican.txt', 'w')

#create a new list that contains the lines we want to append to the pelican file
lines = ["He can take in his beak,\n", "Enough food for a week,\n", "But I'm damned if I see how the helican.\n"]

#we use a try,except,finally block to append lines of text to the file
#if a FileNotFoundError occurs then it will print the line "An error occured"
#the \n helps us continue to the next line because the #write" and "writelines" methods don't add a new line at the end of the text
try:
    pelican.write("A wonderful bird is the pelican,\n")
    pelican.write("His bill holds moe than his belican.\n")
    pelican.writelines(lines)
except FileNotFoundError as err:
    print("An error occured")
finally:
    pelican.close()



