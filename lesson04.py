test = "This is something text!"

# Indexing
print(len(test))
print(test[0])
print(test[-1])

# Slicing
print(test[8:17])    # Slice "something" words.
print(test[8:])      # Slice all the string from "8" index.

# Step slicing
print(test[::2])     # Slicing with "step"  (mark in the last sign), Slice the ever character with the step "2".
print(test[16:7:-1])  # Also we can print in the reverse range, mark is negative "step index".
