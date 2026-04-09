a = [1, [2, 3], [4, [5, 6]]]
flat = []
stack = [a]

while stack:
    current = stack.pop()
    if isinstance(current, list):
        # Extend the stack with the list items (reversed to maintain order)
        stack.extend(current[::-1])
    else:
        flat.append(current)

print(flat)
