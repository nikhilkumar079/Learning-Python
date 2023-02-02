#1. Write a program to accept % from the user and return the grade

def grade(n):
    if n > 90:
        return 'A'
    elif n >= 90 and n>80:
        return 'B'
    elif n>=60 and n<=80:
        return 'C'
    else:
        return 'D'
print("The grade obtained is:",grade(n = int(input())))

#2. Write a program to accept the cost price of a bike and display road tax to be paid.

def road_tax(n):
    if n > 100000:
        return 'The road tax to be paid is 15 %'
    elif n > 50000 and n<=100000:
        return 'The road tax to be paid is 10 %'
    else:
        return 'The road tax to be paid is 5 %'
print(road_tax(int(input())))
    
#3. Write a program to display the monument in given city

city_dict = {
    'Delhi': 'Redfort',
    'Agra': 'Taj Mahal',
    'Jaipur': 'Hawa Mahal',
    'Amritsar': 'Golden Temple',
    'Mysore': 'Mysore Palace',
    'Mumbai': 'Gateway of India',
    'Hyderabad': 'Charminar'
}
city = input().capitalize()
if city in city_dict.keys():
    print(city_dict.get(city))
else:
    print("Entered city is not in list of Top 8")
    
 
#4. Write a program to check how many times a number is divisible by 3 until it becomes less than or equal to 10

def times(n):
    s = 0
    while n >=10:
        n=n//3
        s+=1
    return s
print(times(int(input())))  

#5. Why and when to use while loop

'''While loop is conditional statement which is used to
execute a set of statements as long as a condition is true.'''
'''Example:
Printing the value as long a i is less than 10
    i = 1
    while i < 10:
        print(i)
        i += 1
'''

#6. Use nested loops to print 3 different patterns

#1st pattern

'''
*
* *
* * *
* * * *

'''

n = int(input('Enter number of rows : '))
i = 1
while i <= n :
    j = 1
    while j <= i:
        print("*", end = " ")
        j += 1
    print()
    i += 1
    
#2nd pattern

'''
1 
2 2 
3 3 3 
4 4 4 4 
'''

print("\n2nd Pattern: \n")

i = 1
while i <= n :
    j = 1
    while j <= i:
        print(j, end = " ")
        j += 1
    print()
    i += 1
    
# 3rd Pattern

'''
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
'''

print("\n3rd Pattern: \n")

i = 1
while i <= n :
    j = 1
    while j <= i:
        print(i, end = " ")
        j += 1
    print()
    i += 1
        
#7. Use while loop to display numbers from 10 to 1
n = 10
while n > 0:
    print(n)
    n = n - 1
