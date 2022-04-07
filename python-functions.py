#1.

def sum_to():
  n = int(input("Enter a number: "))
  i=1
  sum = 0
  while (i<=n):
    sum = sum + i
    i = i + 1
  print(f'your number is {n}. The sum of all of the numbers that increment up to that number is {sum}')
sum_to()

#2.
def largest():
  list = [2, 4, 5, 6, 7 ] 
  largest_number = list[0]

  for n in list:
    if n > largest_number: 
      largest_number = n

  print(largest_number)

largest()  

# #3
str = 'Banana' #input("Enter your word: ")
letter = 'a' #input("Input the letter you're looking for: ")
def occurrences(str, letter):

  count = 0
  for i in str:
    if i == letter: 
      count = count + 1
  print(f'Count of {letter} in {str} is {count} ')
occurrences(str, letter)


##4

def product(numList):
  result = 1
  for num in numList:
    result = result * num
  return result
nums1 = [1, 2, 3]
nums2 = [2, 3, 4]
print(product(nums1))
print(product(nums2))