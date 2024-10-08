word = input('Enter the word that contain \'h\': ')
while 'h' not in word.lower() or len(word) <= 1:
    if 'h' not in word.lower():
        print('This word doesn\'t contain \'h\'')
    if len(word) <= 1:
        print('The word should be more than 1 character')
    word = input('Enter the next word: ')
else:
    print('Thank you! The word contains \'h\'.')
