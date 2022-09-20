from multiprocessing.dummy import Array
import statistics
#Sum and Average

number1=float(input("Enter the first number: "))
number2=float(input("Enter the second number: "))
number3=float(input("Enter the third number: "))
sum=number1+number2+number3
avg=(sum)/3
list_of_numbers=[number1,number2,number3]
avg2=statistics.mean(list_of_numbers)

print("Sum is: "+str(sum))
print("Average without the built in function is: "+str(avg)) #without the built in function
print("Average with the built in function is: "+str(avg2)) #with the built in function