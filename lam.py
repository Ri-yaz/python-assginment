r = lambda a : a + 15
print(r(20))
r = lambda x, y : x * y
print(r(10, 20))


def func_compute(n):
 return lambda x : x * n
result = func_compute(2)
print("Double the number of 100 =", result(100))

subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print("Original list of tuples:")
print(subject_marks)
subject_marks.sort(key = lambda x: x[1])
print("\nSorting the List of Tuples:")
print(subject_marks)

models = [{'make':'Nokia', 'model':216, 'color':'Black'}, {'make':'Mi Max', 'model':'2', 'color':'Gold'}, {'make':'Samsung', 'model': 7, 'color':'Blue'}]
print("Original list of dictionaries :")
print(models)
sorted_models = sorted(models, key = lambda x: x['color'])
print("\nSorting the List of dictionaries :")
print(sorted_models)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list of integers:")
print(nums)
print("\nEven numbers from the said list:")
even_nums = list(filter(lambda x: x%2 == 0, nums))
print(even_nums)
print("\nOdd numbers from the said list:")
odd_nums = list(filter(lambda x: x%2 != 0, nums))
print(odd_nums)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list of integers:")
print(nums)
print("\nSquare every number of the said list:")
square_nums = list(map(lambda x: x ** 2, nums))
print(square_nums)
print("\nCube every number of the said list:")
cube_nums = list(map(lambda x: x ** 3, nums))
print(cube_nums)

starts_with = lambda x: True if x.startswith('j') else False
print(starts_with('people'))
starts_with = lambda x: True if x.startswith('h') else False
print(starts_with('hello'))

num = lambda q: q.replace('.','',1).isdigit()
print(num('26587'))
print(num('-34234'))
num1 = lambda r: num(r[1:]) if r[0]=='-' else num(r)
print(num1('-16.4'))
print(num1('-24587.11'))

from functools import reduce
 
fib_series = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]],
                                range(n-2), [0, 1])
 
print("Fibonacci series upto 2:")
print(fib_series(10))



first_num = [1, 2, 3, 5, 7, 8, 9, 10]
sec_num = [1, 5, 2, 3]
print("Original arrays:")
print(first_num)
print(sec_num)
result = list(filter(lambda x: x in first_num, sec_num)) 
print ("\nIntersection of the said arrays: ",result)