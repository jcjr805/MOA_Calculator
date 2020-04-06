#def calculator(self, range, target, mils):
 #       self.range = range
  #      self.target = target
   #     self.mils = mils

print("Please enter a 1 if the measurement will be calculated in yards. ")
print("Please enter a 2 if the measurement will be calculated in meters. ")
measurement = input("What is the height of the target in inches: ")
target = float(input("What is the height of the target in inches: "))
mils = float(input("what is the height of the target in mils: "))

def yard():
    range = (target * 27.77) / mils
    return range

def meters():
    range = (target * 25.4) / mils
    return range

if measurement == '1':
    print(yard())
else:
    print(meters())
