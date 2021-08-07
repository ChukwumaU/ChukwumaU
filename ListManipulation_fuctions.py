magicians_names = ["Presto", "Ernesto", "Dumbledore", "Voldermort", "Zedicus", "Harry"]
#function to print each element in the list
def show_magicians():
    for i in magicians_names:
        print(i)
show_magicians()

#empty list to store data in later
great_magicians = []

#function to add "Make great" to each list element
def make_great():
    for i in magicians_names:
        print("The Great " + i)
make_great()

