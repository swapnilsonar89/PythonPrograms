ls=range(1,101)

for i in ls:
    if i%3==0 and i%5==0:
        print(i,'FizzBuzz')
    elif i%3==0:
        print(i,"Fizz")
    elif i%5==0:
        print(i,'Buzz')
