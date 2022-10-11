print("Welcome to Ali's Tip Calculator")
total_bill = int(input("Enter the bill amount in rupees: Rs. "))
to_split = input("Do you wanna split the bill amount ? (Y/N): ")
if to_split in ['y', 'Y', 'N', 'n']:
    num_of_person = int(input("Enter the number of person to split along : "))
else:
    num_of_person = 1

tip = int(input("What is the percentage of tip, you wanna give? 2,5,10,12,15: "))
print()

# print("The Bill Amount is {0}".format())
to_pay = total_bill + ((tip / 100) * total_bill)
if to_split:
    each_pay = to_pay / num_of_person
    to_pay = each_pay

print("Each Bill Amount is ", to_pay)
