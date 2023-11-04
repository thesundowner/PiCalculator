import sys
import math
sys.set_int_max_str_digits(0) 
file = open('pi.txt' , 'w')
def pi():
    file.write("The appproximation of PI using Euler's Method. \n Done By Bigg Smoke \n \n")
    sum = 0.0
    i = 1
    while i <= i + 1:
        sum += 1 / math.pow(i , 2)
        result = math.sqrt((sum * 6))
        print( i ,  result )
        i_str = str(i)
        result_str = str(result)
        entry = i_str + " "  + result_str
        file.write(entry + '\n')
        i = i + 1
pi()