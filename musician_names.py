def get_formatted_name(first_name, last_name):
    ###Make a formatted first and last name function
    full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)