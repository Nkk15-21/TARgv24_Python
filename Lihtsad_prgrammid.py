from datetime import *

tana = date.today() #nimetus () - funktsioon
tanaf = date.today().strftime("%B %d %Y")

print(f"Tere!, Täna on {tana}")
d=tana.day        #nimetus - omadus
m = tana.month
y = tana.year
print(d)
print(m)
print(y)