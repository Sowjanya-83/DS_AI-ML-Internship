
"""
a={"name":"sowjanya"}
print(a)
b={"age":22}
print(b)

student={"name":"Amit","age":21,"courses":"MCA"}
print(student["name"])
student["age"]=23
student["city"]="Bangalore"
print(student)
marks={"Maths":90,"Science":85,"English":88}
print(marks.get("Maths"))
print(marks.get("History",0))
      for subject,score in marks.items():
          print(subject,score)
          """
""" 
#input dictionary from user
n=int(input("Enter number of customers: "))
user_purchases={}

for _ in range(n):
    name=input("Enter customer name: ")
    amount=int(input(f"Enter purchase amount for {name}: "))
    user_purchases[name]=amount

print("Customer Purchase Data :",user_purchases)
top_customers=max(user_purchases,key=user_purchases.get)
print("Top Customer :",top_customers)
min_customers=min(user_purchases,key=user_purchases.get)
print("Min Customer :",min_customers)   
"""
numbers={1,3,2,2,4,5,1,3}
print(numbers)
numbers.add(6)
print(numbers)