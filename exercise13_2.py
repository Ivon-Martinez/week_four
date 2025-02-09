#open the file in read mode and read the entire file in one gulp
pelican_file = open("pelican.txt", "r").read()
#use the type function to get the type of the returned data and print it
#the data type is a string
print(type(pelican_file))
#print the contents of the returned data
print(pelican_file)

#open the file in read mode and read the content of the file as a list
pelican_file_list = open("pelican.txt", "r").read().splitlines()
#print the number of items in the list
print(len(pelican_file_list))
#print the items of the list
print(pelican_file_list)

#use a for loop to iterate over the contents of the file and print the output without the last blank line by slicing the last character of the string which is "\n"
for line in open('pelican.txt', 'r'):
    print(line[:-1])

