#!/usr/bin/env python
# coding: utf-8

# In[12]:


#List is a sequence of data values called items or elements
#List of items are ordered, but it can also be changed
#length of list is the number of items within the list

ListOfFriends = ['Ashwin', 'Hetal', 'Deepesh', 'Hetal', 'Saravana']
print(ListOfFriends)
print(type(ListOfFriends))
print(len(ListOfFriends))


# In[61]:


listOfNumbers = [1,5,3,7,5,8,44,34,67,55,9]
listover10 = []
print(listOfNumbers)
print(type(listOfNumbers))
print(len(listOfNumbers))
listComp = [i for i in listOfNumbers if i > 10]
print(listComp)


# In[74]:


#sort list
data = []
num = int(input("Enter an integer (0 to quit): "))
while num != 0:
    data.append(num)
    data.sort()
    num = int(input("Enter an integer (0 to quit): "))
for 


# In[79]:


num = [100, 23, 35, 456, 123, 123, 243, 100,243, 675, 967, 993]
datasort = [number for number in num]
datasort.sort()
datasort


# # listOfStrings = ['Kate','Jennifer','Ananya','Robert']
# print(len(listOfStrings))
# print(listOfStrings)
# listOfStrings.append('Ashoka')
# print(type(listOfStrings))
# print(len(listOfStrings))
# print(listOfStrings)
# print(type(listOfStrings))
# countOfList = len(listOfStrings)
# print(countOfList)

# In[15]:


listOfCombinedItems = [24, 'basaveshwaranager', 44, 54, "Rajajinagar", "123 Malleshanna"]
print(listOfCombinedItems)
print(type(listOfCombinedItems))
print(len(listOfCombinedItems))


# In[20]:


newTuple = ('kum', 23, '344')
print(newTuple)
print(type(newTuple))
print(len(newTuple))

#convert tuple into list
newList = list(newTuple)
print(newList)
print(type(newList))
len(newList)


# In[16]:


#creating an emply list
list1 = []
print("The type of the empty list is " , type(list1))
print(type(list1))
print(list1)
print(len(list1))


# In[17]:


list1 = []
num = input("Enter number: ")
print(num)
list1.append(num)
print(list1)


# In[21]:


list1 = []
num = input("Enter number: ")
print(num)
for num in range(0, int(num)):
    firstname = input("Enter the first name: ")
    lastname = input("Enter the last name: ")
    position = input("Enter position: ")
    empnum = input("Enter employee number: ")
    list_of_items = [firstname, lastname, position, empnum]
    list1.append(list_of_items)
    print(list1)
    print(type(list1))
    print(len(list1))
for ctr in list1:
    print(ctr)
    


# In[8]:


listpassword = []
num = input("Enter number: ")


for num in range(0, int(num)):
    firstDigit = input("Input your first digit: ")
    secondDigit = input("Input your second digit: ")
    thirdDigit = input("Input your third digit: ")
    fourthDigit = input("Input your fourth digit: ")
    fifthDigit = input("Input your fifth digit: ")
    sixthDigit = input("Input your sixth digit: ")
    seventhDigit = input("Input your seventh digit: ")
    eightDigit = input("Input your eighth digit: ")
    allEightDigits = [firstDigit, secondDigit, thirdDigit, fourthDigit, fifthDigit,  sixthDigit, seventhDigit, eightDigit]
    listpassword.append(allEightDigits)
    print(listpassword)
    if len(listpassword) >= 8:
        print("Password meets the requirements")
    else:
        print("Dont worry")


# In[ ]:


password = ('p','a','s','s','w','o','r','d')
print(len(password))
if len(password) >= 8:
    print("Your password meets the requirements and the length is ", len(password))
else:
    print("Your password length does not meet the requirements.")


# In[27]:


listOfStrings = [1, 'asf', 44,34, '2asdf']
secondSet = ['asd',34,44,'kumar']
listOfStrings.append(secondSet)
print(*listOfStrings)
countOfStrings = len(listOfStrings)

print(countOfStrings)


# In[31]:


customer_details = ["Ava McDougle", "ava@email.com", "123-456-7890"]
customer_name = customer_details[0]
print("The customer name is ", customer_name)
customer_email = customer_details[1]
print("The customer email address is ", customer_email)
customer_phone = customer_details[2]
print("The customer phone is ", customer_phone)


# In[34]:


list_of_strings = ["Kate", "Jennifer", "Mike"]
person_1 = list_of_strings[-1]
print(person_1)
list_of_strings = ["Kate", "Jennifer", "Mike"]
person_2 = list_of_strings[-2]
print(person_2)
list_of_strings = ["Kate", "Jennifer", "Mike"]
person_3 = list_of_strings[-3]
print(person_3)


# In[33]:


list_of_strings = ["Kate", "Jennifer", "Mike"]
person_2 = list_of_strings[-2]
print(person_2)


# In[41]:


transactions = [ "1AB23456C0011523D,+$25.00", "1AB23456C5541225D,-$56.00", "1AB23456C8613005D,-$393.00", "1AB23456C3542215D,+$544.23", "1AB23456C0145125D,-$5.55", "1AB23456C3485125D,-$8.76"]
latest_transactions = transactions[-1]
second_latest_transactions = transactions[-2]
third_latest_transactions = transactions[-3]
print(latest_transactions)
print(second_latest_transactions)
print(third_latest_transactions)



# In[38]:


last_3_tansaction = transactions[-1:-4]
print(last_3_tansaction)


# In[45]:


mylist = list(range(1, 11))
print(mylist)
slicedlist = mylist[0:4]
print(slicedlist)


# In[53]:


trans_date=['2021-04-03','2021-12-03', '2021-13-03','2021-15-03','2021-22-03',
'2021-25-03','21-30-03','2021-03-04'] 
trans_amt=[2.45,4.50,5.75,10.00,12.30,4.25,15.25,16.20] 
print(trans_date)

input_to_date = input("What end date would you like to see all the transaction amounts from? (format: YYYY-DD-MM): ")

trans_date_to = trans_date.index(input_to_date)
print(trans_date_to)
print(trans_date[0:int(trans_date_to)+1])
print(trans_amt[0:int(trans_date_to)+1])


# In[63]:


trans_date=['2021-04-03', '2021-12-03', '2021-13-03', '2021-15-03', '2021-22-03', '2021-25-03', '2021-30-03', '2021-03-04']
trans_amt=[2.45,4.50,5.75,10.00,12.30,4.25,15.25,16.20]
print(trans_date)
input_to_date = input("What end date would you like to see all the transaction \ amounts from? (format: YYYY-DD-MM): ")

trans_date_to = trans_date.index(input_to_date)
print(trans_date_to)


slicenum = slice(0,int(trans_date_to)+1)
slicelist = trans_amt[slicenum]
print(slicelist)


# In[68]:


list_of_names = []
print(list_of_names)
print(type(list_of_names))
list_of_names.append('Darshan')
print(list_of_names)
list_of_names.append('Yash')
print(list_of_names)
list_of_names.append('Ganesh')
print(list_of_names)


# In[71]:


info = []
print(info)
print(type(info))
info.append(input("Please enter the customer's first name: "))
info.append(input("Please enter the customer's last name: "))
info.append(input("Please enter the customers date of birth: "))
info.append(input("Please enter the customer's account balance: "))
info.append(input("Please enter the customer's account number: "))
print(info)


# In[77]:


list_of_names = ["John", "Mike"] 
print(list_of_names)
list_of_names.insert(0,"Ashwin")
print(list_of_names)
list_of_names.insert(0, "Amy")
list_of_names
list_of_names.insert(3, "Third rate")
print(list_of_names)


# In[80]:


info = ["John", "Smith", "Boston", "Junior Software Developer"]
info.insert(2, input("Please enter an address"))
info.insert(3, input("Please enter a phone number"))


print("First name: " +info[0])
print("Last name: " +info[1])
print("Address: " +info[2])
print("Phone number: " +info[3] )
print("City: " +info[4])
print("Position: " +info[5])


# In[81]:


list_of_names = ["John Smith", "Layla David", "Maria Smith", "Layla David"] 
print(list_of_names)
list_of_names.remove("Layla David")
print(list_of_names)


# In[82]:


input_list = ["Haythem", "Mike", 1, "Layla", "Livia", "Layla", 2, 1, 2, 3, "Mike", "Jesse", "Haythem"]
input_list.remove(1)
input_list.remove(2)
input_list.remove("Layla")
input_list.remove("Mike")
input_list.remove("Haythem")
input_list


# In[83]:


produce_list = ["Apple", "Banana", "Cherry", "Date", "Eggplant", "Fig", "Apple", "Grape "]
del produce_list[1]
produce_list


# In[87]:



produce_list = ["Apple", "Banana", "Cherry", "Date", "Eggplant", "Fig", "Apple", "Grape "]
print(produce_list)
popped_product = produce_list.pop(6)
produce_list
popped_product


# In[89]:


list_of_names_1 = ["Haythem", "Mike"] 
print(list_of_names_1)
list_of_names_2 = ["Jesse", "Layla"] 
print(list_of_names_2)

list_of_names = list_of_names_1 + list_of_names_2
print(list_of_names)


# In[95]:


numbers = list()
numbers
print(type(numbers))

for i in range(0,11):
    numbers.append(i)
print(numbers)
    


# In[97]:


numbers = [i for i in range(0,11)] 
print(numbers)


# In[98]:


numbers = [i for i in range(0,55)]
print(numbers)


# In[100]:


names = ["Miriam","Mary","Dave","Nick"] 
print(names)
names.sort()
print(names)


# In[103]:


names = ["Miriam","Mary","Dave","Nick"] 
britishNames = names
print(names)
print(britishNames)


# 

# In[104]:


names.append("ravish")
print(names)
print(britishNames)


# In[111]:


a = [1,2,3]
b = []
for i in a:
    b.append(i)

print(a)
print(b)

a[0] = 0

print(a)
print(b)


# In[8]:


#list comprehension
numbers =list()
type(numbers)
for i in range(0,10):
    numbers.append(i)
print(numbers)
listComp = [i for i in range(0,10)]
listComp


# In[9]:


tupleComp = (i for i in range(0,10))
tupleComp


# In[12]:


names = ['king','queen','prince','princess']
names_upper = [name.upper() for name in names]
names_upper


# In[46]:


names_upper = []
names = ['king','queen','prince','princess']
for i in names:
    names_upper.append(i.upper())
    names_upper.sort()
print(names_upper)


# In[36]:


positive = []
negative = []
numbers = [2,-2,3,-3,4,-4,5,-5,6,-6,7,-7]
positive = [number for number in numbers if number >= 0]
print(positive)
negative = [number for number in numbers if number < 0]
print(negative)


# In[35]:


for number in numbers:
    if number >= 0:
        positive.append(number)
    elif number < 0:
        negative.append(number)
print("Positive numbers are : " ,positive)
print("Negative numbers are : " ,negative)


# In[38]:


numbers = [1,2,-1,6,-5,-2]
label = ['True' if number >= 0 else 'False' for number in numbers]
label


# In[52]:


names = ["Miriam","Mary","Dave","Nick"] 
sorted_name = []
for name in names:
    sorted_name.append(name)
    sorted_name.sort()
print(sorted_name)


# In[56]:


names = ["Miriam","Mary","Dave","Nick"] 
sorted_name = [name for name in names]
sorted_name.sort()
print(sorted_name)


# In[ ]:




