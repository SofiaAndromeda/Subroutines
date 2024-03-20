def calculate_volume(length, width, height):
    v = 2 * (length * width + width * height + height * length)
    return v


print(calculate_volume(3, 2, 1))
print(calculate_volume(10, 10, 10))
print(calculate_volume(4, 4, 4))
