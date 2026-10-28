def prob_a_or_b(a, b , all_possible_outcomes):
    prob_a = len(a)/len(all_possible_outcomes)

    prob_b = len(b)/len(all_possible_outcomes)

    inner = a.intersection(b)

    prob_inner = len(inner)/len(all_possible_outcomes)

    return(prob_a + prob_b - prob_inner)

evens = {2,4,6}
greater_than_2 = {3,4,5,6}
all_possible_rolls = {1,2,3,4,5,6}

print("Probability of getting an even number or a number greater than 2")
print(prob_a_or_b(evens, greater_than_2, all_possible_rolls))