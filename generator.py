# A generator of even numbers 
def make_generator(nums):
    for i in range(nums):
        yield i * 2

even_nums = make_generator(20)
print (even_nums) # prints a generator object

print (next(even_nums)) # 0
print (next(even_nums)) # 2
print (next(even_nums)) # 4

for even in even_nums:
    print (even)  # This would start from 6

even_nums_list = list(even_nums) # Would use memory
print (even_nums_list) # [] as the generator has been exhausted

# Simpler way of making a generator
square_generator = (x * x for x in [1, 2, 3, 4, 5])
print (square_generator)