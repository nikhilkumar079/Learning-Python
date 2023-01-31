# for large prime number this is efficent program
n = int(input())
s = False
if n > 1:
  #loop to check factors of given number
    for i in range(2,(n**0.5)+1):
        if (n % i == 0):
            s = True
            break
if s == True:
    print("Not Prime")
else:
    print("Prime")
