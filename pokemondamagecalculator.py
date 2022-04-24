import random

print("""A lvl 80 Bagon(dragon, Sp. Atk:200) attacks a lvl 75 absol(dark, Sp. def: 195)
 with rock head with a power of 120 and gains a same type attack bonus. 
 It hits the target normally but deals a not very effective damage. The weather of the field is normal.
\n """)

#damage
level = 80
power = 120
A = 200
D = 195

#modifier
target = 1
weather = 1.5
badge = 1
critical = random.randint(1,2)
random_number = round(random.uniform(0.85 , 1.00),2)
stab = 1
type = 2
other = 1

modifier = round(target*weather*badge*critical*random_number*stab*type*other)
damage = round((((((2*level)/5)+2)*power*A/D)/50)+2)*modifier

print("Target:", target)
print("weather", weather)
print("badge:", badge)
print("critical:", critical)
print("random:", random_number)
print("stab:", stab)
print("type:", type)
print("other:", other)
print("\nmodifier:", modifier)
print("\nBagon deals", damage, "to absol")

