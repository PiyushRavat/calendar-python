import calendar  
# Enter the month and year  
yyyy= int(input("Enter year: "))  
mm = int(input("Enter month: "))  
   
print(calendar.month(yyyy,mm))



print("*****TELEPHONE DIRECTORY***)"
list1 = [];
list2=[]
dict1={}
temp=100
n=input("Enter the number of contacts : ")
for i in range(0,n):
    name1=raw_input("Enter your name: ")
    num=input("Enter your phone number: ")
    list1.extend([name1])
    list2.extend([num])
    dict1=dict(zip(list1,list2))#to convert two list into dictionary
print dict1
print """
         1:Add a contact
         2:Search a contact
         3:Delete a contact
         4:Update a contact
         5:View directory
         6:Exit"""

