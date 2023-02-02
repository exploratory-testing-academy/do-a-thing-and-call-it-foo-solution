# Program, that converts numbers to Roman numbers.

def  roman (num):
     if   not (0 < num < 4000 ):
         raise   ValueError ('number out of range')
     if   not   isinstance (num, int):
         raise   TypeError ('non-integers can not be converted')
     ints = (5000, 4000, 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
     nums = ('(V)', 'M(V)', 'M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
     result   =   []
     for i in range (len(ints)):
         count = int(num / ints[i])
         result . append (nums[i] * count)
         num -= ints[i] * count
     return ''. join (result)

