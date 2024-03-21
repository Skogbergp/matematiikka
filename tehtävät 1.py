import numpy as np

# muunna radiaanit asteiksi a 2,493      b 0,911
print(np.degrees(2.493))
print(np.degrees(0.911))
print("\n")

# muunna asteet radiaaneiksi 137,7    b  62,3
print(np.radians(137.7))
print(np.radians(62.3))
print("\n")

input = [30, 45, 60, 90, 120, 135, 150, 180, 270, 360]
for i in input:
    print(f"{i}  {np.radians(i)}")

print("\n")
print(np.hypot(1.6, 2.3))
