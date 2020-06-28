
user_input = input("Where are you from? ")
print("I am from ", user_input.upper())
print("I am from ", user_input.lower())

name = input("Input comma separated sequence of words")
words = [word for word in name.split(",")]
print(",".join(sorted(list(set(words)))))



def html_tags(string, tag):
	output = "<"+ tag + ">" + string + "</"+ tag + ">"
	return output
	print(html_tag('rdxexrc','b'))


listx = [5, 10, 7, 4, 15, 3]
print(listx)
tuplex = tuple(listx)
print(tuplex)

tuplex = tuple("hello place")
print(tuplex)
index = tuplex.index("p")
print(index)



tuplex = tuple("countrymen")
print(tuplex)
print(len(tuplex))

def maximum(a, b, c): 
  
    if (a >= b) and (a >= c): 
        largest = a 
  
    elif (b >= a) and (b >= c): 
        largest = b 
    else: 
        largest = c 
          
    return largest 

def test_range(n):
    if n in range(1,10):
        print( " %s is in the range"%str(n))
    else :
        print("The number is outside the given range.")
test_range(9)




a Python function that accepts a string and calculate the number of
upper case letters and lower case letters.