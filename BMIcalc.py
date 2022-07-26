
weight = float(input("How much do you weigh?: "))
weight_units = str(input("Is this in Lbs(L) or Kgs(K)?: "))

height = str(input("How tall are you?: "))
height_units = str(input("Is this in Feet and inches(F) or Meters(M)?: "))

if weight_units == "L":
    weight*= 0.45
    weight_units = "K"
if height_units == "F":
    apost = height.find("'")
    height_in_meters = float(height[apost-1])*0.3048
    print(height_in_meters)
    height_in_meters += float(height[apost+1:])*0.0254
    print(height_in_meters)
    height = str(height_in_meters)

BMI = weight/(float(height)**2)
print(BMI)