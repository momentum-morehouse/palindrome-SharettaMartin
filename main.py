#Write a program that asks the user for one or more sentences 

print ('Hello!')
#Getting info from user
#Question1
name = input('Please enter your name  ')
print(name)
if(name==name[::-1]):
   print(name, 'is a palindrome.')
else:
  print(name,'is not a palindrome.')

#Question2
num = (input('Enter your age  '))
print(num)
if(num==num[::-1]):
   print(num, 'is a palindrome.')
else:
  print(num,'is not a palindrome.')

#Question3
job = input('Enter your occupation  ')
print(job)
if(job==job[::-1]):
   print(job, 'is a palindrome.')
else:
  print(job,'is not a palindrome.')

#Checks conditions and test for palindrome or no..
#if 
  #print('This is a palindrome.')
#elif:  WHY WON'T ELIF WORK
  #print('This is not a palindrome.')
#WORD CHECK...Bob, Anna, 44, Sharetta, Tonya, Michael

  #Figure out how to make a single condition that applies to all
