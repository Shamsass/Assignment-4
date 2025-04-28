# # Get the numeric value since input() returns a value in string form
# earth_weight = float(earth_weight_str)

# # Having a variable for each piece of information is a good habit
# mars_weight = earth_weight 
# # * MARS_MULTIPLE
# rounded_mars_weight = round(mars_weight, 2)


# # Note the string concatenation!
# print('The equivalent weight on Mars: ' + str(rounded_mars_weight))
# Get the numeric value since input() returns a value in string form
earth_weight_str = input("Enter your weight on Earth: ")
earth_weight = float(earth_weight_str)

# Mars gravity is about 0.38 times Earth's gravity
MARS_MULTIPLE = 0.38

# Correct calculation of Mars weight
mars_weight = earth_weight * MARS_MULTIPLE
rounded_mars_weight = round(mars_weight, 2)

# Display the result
print('The equivalent weight on Mars: ' + str(rounded_mars_weight))
