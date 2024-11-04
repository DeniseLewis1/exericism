def translate(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    words = text.split()
    new_text = []

    for word in words:
        if word[0] in vowels or word.startswith('xr') or word.startswith('yt'):
            new_text.append(word + 'ay')
            break
    
        index = word.find('qu')
    
        if index >= 0:
            new_text.append(word[index + 2 :] + word[: index + 2] + 'ay')
            continue
        
        starting_consonants = ''
        index = 0
    
        for letter in word:
            if letter not in vowels:
                if letter == 'y' and index > 0:
                    new_text.append(word[index:] + starting_consonants + 'ay')
                    break
                starting_consonants += letter
                index += 1
            else:
                new_text.append(word[index:] + starting_consonants + 'ay')
                break

    return ' '.join(new_text)


