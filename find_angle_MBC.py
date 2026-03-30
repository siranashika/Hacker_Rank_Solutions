import math
ab = float(input())
bc = float(input())
angle = math.degrees(math.atan2(ab, bc))
print(str(int(round(angle))) + chr(176))
