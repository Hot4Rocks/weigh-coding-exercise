# Mock function to simulate the weighing process
fake_bar = 5  # For testing, let's assume the fake bar is number 5

def find_fake_gold_bar(fake_bar):
    groups = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    
    def weigh(left_bars, right_bars, fake_bar):
        # Weighing process
        left_weight = sum(1 if bar != fake_bar else 0.5 for bar in left_bars)
        right_weight = sum(1 if bar != fake_bar else 0.5 for bar in right_bars)
        
        if left_weight < right_weight:
            return "Left"
        elif left_weight > right_weight:
            return "Right"
        else:
            return "Equal"

    # Processing results of weighing first two groups
    result = weigh(groups[0], groups[1], fake_bar)
    
    if result == "Equal":
        guess_group = groups[2]
    elif result == "Left":
        guess_group = groups[0]
    else:
        guess_group = groups[1]

    # Weigh two out of the three remaining bars 
    result = weigh([guess_group[0]], [guess_group[1]], fake_bar)
    
    if result == "Equal":
        fake_bar = guess_group[2]
    elif result == "Left":
        fake_bar = guess_group[0]
    else:
        fake_bar = guess_group[1]
    
    return fake_bar

# Indicate which bar is fake
fake_bar_found = find_fake_gold_bar(fake_bar)
print("The fake gold bar is:", fake_bar_found)
