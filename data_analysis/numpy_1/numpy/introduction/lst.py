temperatures = [32.5 , 31.8 , 33.0, 35.2,  36.6];
total = 0;

for temp in temperatures:
    total += temp

avg = total / len(temperatures)
print(avg)