# Possible outcomes of rolling a standard six-sided die
die1_outcomes = {1, 2, 3, 4, 5, 6}
die2_outcomes = {4, 5, 6, 7, 8, 9}  # Example: outcomes shifted for a hypothetical die

# Union of outcomes (all unique outcomes possible from both dice)
union_outcomes = die1_outcomes | die2_outcomes
print("Union of outcomes (all unique results):", union_outcomes)

# Intersection of outcomes (common outcomes between the two dice)
intersection_outcomes = die1_outcomes & die2_outcomes
print("Intersection of outcomes (common results):", intersection_outcomes)
