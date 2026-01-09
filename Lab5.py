# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
n = 5

def hollow_square(n):
    result= "" 

    for i in range (n):
        for j in range (n):
             if j==0 or i==0 or i==n-1 or j==n-1:
                result += "*"   
             else:   
                 result += " "
    
        result += "\n"


    return result.rstrip()

print (hollow_square(5))

# 1
# 12
# 123
# 1234
n=4
def number_pattern(n):
   result=""

   for i in range(n):
       for j in range(i + 1):
           
           if j==0:
               result += "1"
           else:
               result += ""

           if j==1:
               result += "2"
           else:
               result += ""

           if j==2:
               result += "3"
           else:
               result+= ""
           if j==3:
               result += "4"
           else:
               result+= ""

       result += "\n"

   return result.rstrip ()

print (number_pattern(4))


       
           

# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
   total = 0
   count = 1
   while count <= n:
        total += count
        count += 1

   return total
print (sum_of_natural_numbers(5))
    




# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    result = ""
    for i in range(n):
        for j in range(n - i - 1):
                result += " "

        for j in range(2 * i + 1):
                result += "*"
            

        result += "\n"

    return result.rstrip ()

print (centered_star_pyramid(4))

