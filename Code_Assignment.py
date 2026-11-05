# ---------------------------------------------------------------------
# PART 1: THE BASICS (Arithmetic Operators)
# ---------------------------------------------------------------------

# TODO 1: Add 150 and 250.
q1 = 150 + 250

# TODO 2: Subtract 42 from 100.
q2 = 100 - 42

# TODO 3: Multiply 12 by 12.
q3 = 12 * 12

# TODO 4: Divide 1000 by 5.
q4 = 1000 / 5

# TODO 5: Use the Exponent operator (**) to find 5 to the power of 3.
q5 = 5 ** 3

# TODO 6: Use the Modulo operator (%) to find the remainder of 100 divided by 9.
q6 = 100 % 9

# TODO 7: Use Floor Division (//) to find out exactly how many times
# 8 goes into 75 (ignoring the remainder).
q7 = 75 // 8

# ---------------------------------------------------------------------
# PART 2: COMPARING THINGS (Booleans)
# ---------------------------------------------------------------------

# TODO 8: Check if 100 is strictly greater than (>) 99.
q8 = 100 > 99

# TODO 9: Check if 25 is less than or equal to (<=) 25.
q9 = 25 <= 25

# TODO 10: Use the Equality operator (==) to check if 7.5 is equal to 7.5.
q10 = 7.5 == 7.5

# TODO 11: Use the Not Equal To operator (!=) to check if 10 is NOT equal to 20.
q11 = 10 != 20

# TODO 12: Write an expression checking if the remainder of 15 / 4 is equal to 3.
q12 = 15 % 4 == 3

# ---------------------------------------------------------------------
# PART 3: VARIABLES AND MATH
# ---------------------------------------------------------------------

base_damage = 15
strength_multiplier = 3
armor = 10

# TODO 13: Calculate total damage. Multiply base_damage by strength_multiplier,
# then subtract the armor. (Use the variables!)
q13 = base_damage * strength_multiplier - armor

max_health = 100
current_health = 35

# TODO 14: The player drinks a potion that restores 50 health.
# Write an expression adding 50 to current_health.
q14 = current_health + 50

# TODO 15: Check if the player's health after drinking the potion (q14)
# is greater than or equal to max_health. This should evaluate to False.
q15 = q14 >= max_health

# ---------------------------------------------------------------------
# PART 4: STRING MANIPULATION (New!)
# Python operators do special things to text (strings).
# ---------------------------------------------------------------------

# TODO 16: Use the + operator to concatenate (join) "Hello" and " World".
# Make sure to include the space!
q16 = "Hello" + " World"

# TODO 17: Use the * operator to multiply the string "Echo! " by 3.
q17 = "Echo! " * 3

# TODO 18: Use the len() function to find out how many characters
# are in the string "Supercalifragilisticexpialidocious".
q18 = len("Supercalifragilisticexpialidocious")

# TODO 19: Check if the length of the string "Python" is equal to 6.
q19 = len("Python") == 6

# ---------------------------------------------------------------------
# PART 5: LOGICAL OPERATORS (and, or, not)
# ---------------------------------------------------------------------

# TODO 20: Write a statement using 'and' that evaluates to True.
q20 = 5==5 and 10==10

# TODO 21: Write a statement using 'or' that evaluates to True,
# where ONE of the sides is False.
q21 = 10==10 or 5==4

# TODO 22: Use 'not' to flip a True statement into a False statement.
q22 = not(5==5)

# ---------------------------------------------------------------------
# PART 5: THE ESCAPE ROOM (Grand Finale)
# ---------------------------------------------------------------------

has_red_key = False
has_blue_key = True
code_cracked = True
power_on = False

# TODO 23: The door opens if you have the red key AND the blue key.
# Write the expression. (Should be False)
q23 = has_red_key and has_blue_key

# TODO 24: The computer turns on if the code is cracked OR the power is on.
# Write the expression. (Should be True)
q24 = code_cracked or power_on

# TODO 25: ESCAPE THE ROOM!
# You win if:
# 1. The code is cracked
# 2. AND you have EITHER the red key OR the blue key
# 3. AND the power is NOT on.
# Use parentheses to group your logic!
q25 = code_cracked and (has_red_key or has_blue_key) and not(power_on)


# =====================================================================
# DO NOT EDIT BELOW THIS LINE
# Auto-Grader
# =====================================================================

def run_grader():
    answers = [
        # Part 1
        (1, q1, 400, "What is 150 + 250?", 1),
        (2, q2, 58, "What is 100 - 42?", 1),
        (3, q3, 144, "What is 12 * 12?", 1),
        (4, q4, 200.0, "Use the / symbol for division.", 1),
        (5, q5, 125, "Use the ** symbol for exponents.", 1),
        (6, q6, 1, "Use the % symbol.", 1),
        (7, q7, 9, "Use the // symbol.", 1),
        # Part 2
        (8, q8, True, "Use >", 2),
        (9, q9, True, "Use <=", 2),
        (10, q10, True, "Use ==", 2),
        (11, q11, True, "Use !=", 2),
        (12, q12, True, "Check (15 % 4 == 3)", 2),
        # Part 3
        (13, q13, 35, "(base_damage * strength_multiplier) - armor", 3),
        (14, q14, 85, "current_health + 50", 3),
        (15, q15, False, "Check if q14 >= max_health", 3),
        # Part 4
        (16, q16, "Hello World", "Use + to add strings together. Don't forget the space!", 4),
        (17, q17, "Echo! Echo! Echo! ", "Use * to multiply the string.", 4),
        (18, q18, 34, "Pass the string into len()", 4),
        (19, q19, True, "len('Python') == 6", 4),
        # Part 5
        (24, q20, True, "Make sure both sides of 'and' evaluate to True.", 6),
        (25, q21, True, "Use 'or'. At least one side must evaluate to True.", 6),
        (26, q22, False, "Wrap a True statement in 'not', like: not (1 == 1)", 6),
        # Part 6
        (27, q23, False, "has_red_key and has_blue_key", 7),
        (28, q24, True, "code_cracked or power_on", 7),
        (29, q25, True, "code_cracked and (has_red_key or has_blue_key) and not power_on", 7),
    ]

    section_names = {
        1: "Part 1: Arithmetic",
        2: "Part 2: Comparisons",
        3: "Part 3: Variables",
        4: "Part 4: Strings",
        5: "Part 5: Lists",
        6: "Part 6: Logical Operators",
        7: "Part 7: The Escape Room"
    }

    scores_by_section = {i: {"correct": 0, "total": 0, "errors": []} for i in range(1, 8)}
    total_correct = 0

    for q_num, student_ans, expected, hint, section in answers:
        scores_by_section[section]["total"] += 1

        # Grading logic
        is_correct = False
        if student_ans is not None:
            if expected in [True, False]:
                if type(student_ans) == bool and student_ans == expected:
                    is_correct = True
            elif student_ans == expected:
                is_correct = True

        if is_correct:
            scores_by_section[section]["correct"] += 1
            total_correct += 1
        else:
            if student_ans is None:
                scores_by_section[section]["errors"].append(f"  O Q{q_num} Skipped.")
            else:
                scores_by_section[section]["errors"].append(f"  X Q{q_num} Incorrect. Hint: {hint}")

    print("\n" + "=" * 60)
    print("GRADING REPORT")
    print("=" * 60)

    for section_id, data in scores_by_section.items():
        correct = data["correct"]
        total = data["total"]
        print(f"\n{section_names[section_id]}: {correct}/{total}")

        if correct == total:
            print("Perfect!")
        else:
            for error in data["errors"]:
                print(error)

    print("\n" + "=" * 60)
    print(f"FINAL SCORE: {total_correct} / 29")

    if total_correct == 29:
        print("All Completed. Full Points")
    elif total_correct >= 20:
        print("2/3 Correct")
    else:
        print("Less Than 2/3 Correct")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    run_grader()