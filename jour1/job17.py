###JOB17

for i in range(1,100):
    if (i % 3 == 0 and i % 5 == 0) :
        i = "FizzBuzz"
        print(i)
    elif i % 3 == 0 :
        i = "Fizz"
        #print(i)
    elif i % 5 == 0 :
        i = "Buzz"
        #print(i)
   
    else:
        print(i)
