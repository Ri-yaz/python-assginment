

def char_freq(str):
    dict = {}
    for n in str:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(char_freq('hello.world'))

def string_both_ends(str):
  if len(str) < 2:
    return ''

  return str[0:2] + str[-2:]

print(string_both_ends('HELLOWORLD'))
print(string_both_ends('HE'))
print(string_both_ends('H'))



def add_string(str1):
  length = len(str1)

  if length > 2:
    if str1[-3:] == 'ing':
      str1 += 'ly'
    else:
      str1 += 'ing'

  return str1
print(add_string('ly'))
print(add_string('sel'))
print(add_string('lying'))



def not_poor(str1):
  snot = str1.find('not')
  spoor = str1.find('rich')
  

  if spoor > snot and snot>0 and spoor>0:
    str1 = str1.replace(str1[snot:(spoor+4)], 'rich')
    return str1
  else:
    return str1
print(not_poor('The person is not that rich!'))
print(not_poor('The person is poor!'))



def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][1]

print(find_longest_word(["here", "there", "near"]))

def remove_char(str, n):
      first_part = str[:n] 
      last_part = str[n+1:]
      return first_part + last_part
print(remove_char('people', 0))
print(remove_char('people', 3))
print(remove_char('people', 5))



def change_sring(str1):
      return str1[-1:] + str1[1:-1] + str1[:1]
	  
print(change_sring('hello'))
print(change_sring('world'))

def odd_values_string(str):
  result = "" 
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result

print(odd_values_string('register'))
print(odd_values_string('jackel'))

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print( word_count('Hello i am from nepal'))






def insert_sting_middle(str, word):
	return str[:7] + word + str[7:]

print(insert_sting_middle("Hello    me", "its"))
print(insert_sting_middle('I am a ', 'boy'))


def sum(items):
    sum_num = 0
    for x in items:
        sum_num += x
    return sum_num
print(sum([5,7,-8]))

def multiply(items):
    tot = 1
    for x in items:
        tot *= x
    return tot
print(multiply([4,3,-8]))


def max_num( list ):
    max = list[ 0 ]
    for a in list:
        if a > max:
            max = a
    return max
print(max_num([2, 4, -1, 0]))


def max_num( list ):
    max = list[ 0 ]
    for a in list:
        if a < max:
            max = a
    return max
print(max_num([6, 7, -8, 3]))


def match_words(words):
  ctr = 0

  for word in words:
    if len(word) > 1 and word[0] == word[-1]:
      ctr += 1
  return ctr

print(match_words(['pqr', 'xyz', 'aba', '1221']))



def last(n): return n[-1]

def sort(tuples):
  return sorted(tuples, key=last)

print(sort([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))


a = [1,2,3,4,5,3]

dup_items = set()
uniq_items = []
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)

print(dup_items)

l = []
if not l:
  print("List is empty")
  

  first_list = [1, 22, 4, 2, 4]
new_list = list(first_list)
print(first_list)
print(new_list)


one_list = [{},{},{}]
two_list1 = [{0,2},{},{}]
print(all(not d for d in one_list))
print(all(not d for d in two_list1))

num = [1,2,3,4]
print(['add{0}'.format(i) for i in  num])


num1 = [1, 32, 5, 71, 91, 10]
num2 = [25, 40, 50, 20]
num1[-1:] = num2
print(num1)


d = {"he", "she"}
print(d)
d.update({"me"})
print(d)


new={"he"}
new2={'we'}
new3={'me'}
new4 = {}
for d in (new, new2, new3, new4): new4.update(d)
print(new4)

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
  if x in d:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
      is_key_present(3)
is_key_present(5)



d = {'Ram': 1, 'Hari': 2, 'Shyam': 3} 
for name, value in d.items():
     print(name, 'corresponds to ', d[name]) 


d=dict()
for x in range(1,16):
    d[x]=x**2
print(d) 


a = {'a', 'b'}
b= {'x', 'y'}
d = a.copy()
d.update(b)
print(d)


a_dict = {'a' :6,'b' :7, 'c' :3}
print(sum(a_dict.values()))

a_dict = {'a' :6,'b' :7, 'c' :3}
print(multiply(a_dict.values()))

inDict = {'a':1,'b':2,'c':3,'d':4}
print(inDict)
if 'c' in inDict: 
    del inDict['c']
print(inDict)


tuple = 1, 5, 8
print(tuple)
num1, num2, num3 = tuple
print(num1 + num2 + num3)

tuplex = (4, 6, 2, 8, 3, 1) 
print(tuplex)
tuplex = tuplex + (9, 6, 5)
print(tuplex)


word = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
str =  ''.join(word)
print(str)


tuplex = "w", 3, "s", "c", "h", "o", "o", "l"
print(tuplex)
tuplex = tuplex[:2] + tuplex[3:]
print(tuplex)

tuplex = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
slice = tuplex[3:5]
print(slice)

def maximum(a, b, c): 
    list = [a, b, c] 
    return max(list) 
a = 103
b = 30
c = 123
print(maximum(a, b, c)) 

def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print(sum((8, 2, 3, 0, 7)))

def mul(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total
print(mul((8, 2, 7)))

def str_rev(str1):

    rstr1 = ''
    index = len(str1)
    while index > 0:
        rstr1 += str1[ index - 1 ]
        index = index - 1
    return rstr1
print(str_rev('hello world'))


def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])

string_test('He is from Nepal.')


def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x
print(unique_list([1,2,2,3,3,4,4,5,4,6,7]))



def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True             
print(test_prime(4))

def even_num(l):
    enum = []
    for n in l:
        if n % 2 == 0:
            enum.append(n)
    return enum
print(even_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))

