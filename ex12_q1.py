# what is wrong with the below

cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
cheese += 'Oke'

print(cheese)

# the first variable is a list
# the += operator is used to append the list
# however it is trying to add a string to a list
# it treats each character as a separate item
# you need to enclose it with square brackets to add to a list as one item/element

cheese += ['Oke']
print(cheese)


# how would you add two new cheeses to the list with a single command?
# include two items in the list you are appending

cheese += ['Brie', 'Camembert']
print(cheese)
cheese.append('brie')
# you could also use the extend method
cheese.extend(['Red Leicester', 'Gouda'])
print(cheese)

