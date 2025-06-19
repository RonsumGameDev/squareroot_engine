'''This is the version I wrote 3 years ago and abandoned. I saw it again today and uploaded the refined version as a module
HERE IS A TRIBUTE TO THE VERSION 0.1 (It sucks and it is impossible to read)'''

n = int(input("Enter a number : "))
a = [1,2,3,4,5,6,7,8,9]
b = " "
p = str(n)
div = 0
rem = 1
if n >= 100:
    s = p[0]`
    t = p[1] + p[2]
    s = int(s)
    t = int(t)
    for i in a:
        if i*i > s:
            div = i-1
            quo = i-1
            rem = s - (div * div)
            break
    
    div *= 20
    b += str(quo)
    rem *= 100
    rem += t
    for i in a:
         if (div+i)*i > rem:
             div += i-1
             quo = i-1
             break
    rem = rem - (div*(i-1))
    
        
    b += str(quo) + "."
    div += i-1
    div *= 10
    rem *= 100
    
    for i in range(1,25):
             
        print("Divide this : ", rem)
        for j in range(1, 25):
            if (div + j)*j > rem:
                 quo = j-1
                 div += j-1
                 print("Quo =", quo)
                 print("Raw" ,div)
                 print("That's what we are dividing with : ",((div) * (j-1)))
                 rem = rem - ((div )*(j-1))
                 print("That's the remainder = ", rem)
                 break
        
        div += j-1
        div *= 10
        rem *= 100
        b += str(quo)


print(b)
