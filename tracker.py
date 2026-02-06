user_score = 0

user_steps = int(input("How many steps did you take?: "))
if user_steps >= 10000:
    user_score += 3
user_time = float(input("How many hours did you code?: "))
if user_time >= 1:
    user_score += 4
user_train = input("Did you train today: (Yes/No): ")
if user_train == "Y":
    user_score += 3
    print(user_score)

print(f"Your score today: {user_score}/10")

if user_score == 10:
    print(f"Perfect day. Real growth. Your score.")
else:
    print(f"Good progress. Keep going.")
