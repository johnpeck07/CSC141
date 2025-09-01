
name_with_whitespace = "\t\n  John Doe  \n\t"
print("Original name with whitespace:")
print(repr(name_with_whitespace))

print("\nUsing lstrip():")
print(repr(name_with_whitespace.lstrip()))

print("\nUsing rstrip():")
print(repr(name_with_whitespace.rstrip()))

print("\nUsing strip():")
print(repr(name_with_whitespace.strip()))