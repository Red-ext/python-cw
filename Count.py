amount=int(input("Please enter an amount"))

note1=amount//100
note2=(amount%100)//50
note3=((amount%100)%50)//10

print("Rs. 100 note", note1)
print("Rs. 50 note", note2)
print("Rs. 10 note", note3)