#Consider the string ‘brontosaurus’. Write Pythonic code that implements and returns the 
#functionality of histogram using dictionaries for the given string. Also, write the function 
#print_hist() to print the keys and their values in alphabetical order from the values returned 
#by the histogram function

string1 = 'brontosaurus'
d = dict()

#histogram function
def histogram(string1):
    d = {}
    for x in string1:
        if x in d:
            d[x]+=1
        else:
            d[x]= 1
    return d
p=histogram(string1)
print(p)

#print_hist function

def print_hist(a):
    #sorting alphabetically
    sorting = sorted(a.items())
    print(sorting)
   
s = dict(print_hist(p))