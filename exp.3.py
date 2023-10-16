# Define the string
my_string = "welcome to python world"

# Initialize a counter
alphabet_count = 0

# Loop through each character in the string
for char in my_string:
    if char.isalpha():
        alphabet_count += 1

# Print the result
print("Number of alphabets:", alphabet_count)
# Define the string
my_string = "welcome to python world"

# Define the range
start_index = 3
end_index = 8

# Extract the characters
extracted_characters = my_string[start_index:end_index+1]

# Print the result
print("Extracted characters:", extracted_characters)
# Define the string
my_string = "welcome to python world"

# Check if the string is alphanumeric
is_alphanumeric = my_string.isalnum()

# Print the result
if is_alphanumeric:
    print("The string is alphanumeric.")
else:
    print("The string is not alphanumeric.")
