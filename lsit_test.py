#Author Jerry
cast = ['A','B','C','D' ]
#print(cast)
print(len(cast))
# print(cast[0])
cast.pop()
# print(cast)
cast.extend(['test','haha'])
# print(cast)
cast.remove('B')
# print(cast)
cast.append('F')
# print(cast)
cast.insert(0,'FRIST')
# print(cast)

movies = ['The Holy Grail',1975,'Terry Jones & Terry Gilliam', 91,['Graham Chapman',
       ['Michael Palin','John Cleese','Terry Gilliam','Eric Idle','Terry Jones']]]

# for each_item in cast:
#     print(each_item)

def print_lol( the_list):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol (each_item)
        else:
            print(each_item)

print_lol(movies)