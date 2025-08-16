import math
def check_angles(angle1, angle2):
	sum_of_angles = angle1 + angle2
	if sum_of_angles == 90:
		print("Angles are complementary.")
	elif sum_of_angles == 180:
		print("Angles are supplementary.")
	else:
		print("Angles are not complementary or supplementary.")