# Program to Calculate resistance in a circuit whether it be the resistors are in series or parallel

def res(R1, R2):
     sum = R1 + R2
     if (UserOption =="series"):
         return sum
     else:
         return (R1 * R2)/(R1 +R2)
      
      

ResistorValue1 = int(input("Enter value of first resistor : "))
ResistorValue2 = int(input("Enter value of second resistor : "))
UserOption = str(input("Enter series or parallel : "))
print("\n")
R = res(ResistorValue1, ResistorValue2)
print("The total resistance is", R)
