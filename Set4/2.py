#Write a function which receives a variable number of strings as arguments. Find unique 
#characters in each string.


def unique(*string_list):
    new=[]
    stringunique = []
    for string in string_list:
        for p in string:
            if p not in stringunique:
                stringunique.append(p)
        new=' '.join(stringunique)
    print(new)

unique_char = unique('Hello', 'World', 'how', 'are', 'you')

    