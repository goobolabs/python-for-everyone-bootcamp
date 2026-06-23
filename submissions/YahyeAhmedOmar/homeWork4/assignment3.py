# grade_tools.py

def is_passing(score):
    return score >= 50

# Grade Rules:
# 90+ = A
# 70+ = B
# 50+ = C
# Below 50 = F

def grade_label(score):
    if score >= 90:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 50:
        return "C"
    else:
        return "F"

scores = [95, 75, 55, 30]

for score in scores:
    print("Score:", score)
    print("Passing:", is_passing(score))
    print("Grade:", grade_label(score))
    print("-----")