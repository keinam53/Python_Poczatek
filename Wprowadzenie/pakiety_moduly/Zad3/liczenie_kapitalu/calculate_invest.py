def calculate_investment(initial_value, procent, time):
    final_value = initial_value * (1 + procent / 100) ** time
    return final_value
