# Check if the sum of the angles is equal to 180 degrees
# and none of the angles are zero
angle_a = int(input("Enter first angle: "))
angle_b = int(input("Enter second angle: "))
angle_c = int(input("Enter third angle: "))
#if (angle_a + angle_b + angle_c) == 180 and all(angle > 0 for angle in [angle_a, angle_b, angle_c]):
if (angle_a + angle_b + angle_c) == 180:
    print("Triangle is Valid")
else:
	print("Triangle is Invalid")