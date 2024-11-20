# Probability of a single event
def single_event_probability(favorable_outcomes, total_outcomes):
    """
    Calculate the probability of a single event.
    Args:
        favorable_outcomes (int): Number of favorable outcomes.
        total_outcomes (int): Total number of possible outcomes.
    Returns:
        float: Probability of the event.
    """
    if total_outcomes == 0:
        return 0
    return favorable_outcomes / total_outcomes

# Conditional Probability: P(A|B) = P(A ∩ B) / P(B)
def conditional_probability(prob_a_and_b, prob_b):
    """
    Calculate the conditional probability of A given B.
    Args:
        prob_a_and_b (float): Probability of A and B occurring together.
        prob_b (float): Probability of event B.
    Returns:
        float: Conditional probability P(A|B).
    """
    if prob_b == 0:
        return 0
    return prob_a_and_b / prob_b

# Example Usage
# 1. Single Event Probability
favorable_outcomes = 3  # Example: Rolling a 3, 4, or 5 on a six-sided die
total_outcomes = 6      # Total outcomes on a six-sided die
probability = single_event_probability(favorable_outcomes, total_outcomes)
print(f"Probability of rolling a 3, 4, or 5: {probability:.2f}")

# 2. Conditional Probability
prob_a_and_b = 0.2  # Probability of A and B happening
prob_b = 0.5        # Probability of B happening
conditional_prob = conditional_probability(prob_a_and_b, prob_b)
print(f"Conditional Probability P(A|B): {conditional_prob:.2f}")

# 3. Example: Probability of independent events
# If A and B are independent: P(A ∩ B) = P(A) * P(B)
prob_a = 0.3  # Probability of event A
prob_b = 0.4  # Probability of event B
prob_a_and_b_independent = prob_a * prob_b
print(f"Probability of A and B (independent): {prob_a_and_b_independent:.2f}")

# 4. Example: Complement Rule
# P(A') = 1 - P(A)
prob_a_complement = 1 - prob_a
print(f"Probability of not A (P(A')): {prob_a_complement:.2f}")

# 5. Example: Total Probability
# P(A ∪ B) = P(A) + P(B) - P(A ∩ B)
prob_a_or_b = prob_a + prob_b - prob_a_and_b
print(f"Probability of A or B (P(A ∪ B)): {prob_a_or_b:.2f}")
