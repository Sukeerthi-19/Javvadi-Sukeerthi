# Function to calculate permutations
def get_permutations(elements, r):
    def permute(current, remaining):
        if len(current) == r:
            result.append(current)
            return
        for i in range(len(remaining)):
            permute(current + [remaining[i]], remaining[:i] + remaining[i+1:])

    result = []
    permute([], elements)
    return result

# Function to calculate combinations
def get_combinations(elements, r):
    def combine(start, current):
        if len(current) == r:
            result.append(current)
            return
        for i in range(start, len(elements)):
            combine(i + 1, current + [elements[i]])

    result = []
    combine(0, [])
    return result

# Input data
items = ['A', 'B', 'C', 'D']

# 1. Calculate permutations
perm_length = 3
permutations_result = get_permutations(items, perm_length)
print(f"Permutations of length {perm_length}:")
for perm in permutations_result:
    print(perm)

# 2. Calculate combinations
comb_length = 3
combinations_result = get_combinations(items, comb_length)
print(f"\nCombinations of length {comb_length}:")
for comb in combinations_result:
    print(comb)
