habit_info = ("Football", 6.7, 10, True)
print("\n\nHabits:", habit_info)

weekly_habits = (1,0,1,1,0,1,0)
completed = 0
missed = 0
print("1 = Completed\n0 = Missed")
print("Weekly habits:", weekly_habits)
print("Days in tuple:", len(weekly_habits))

print("\nDay 1-",weekly_habits[0])
print("Day 5-",weekly_habits[4])
print("Day 1-3:",weekly_habits[0:3])
print("Day 4-7:",weekly_habits[3:6])

habit_info = habit_info + ('Daily', 2300, 1.03, True)
completed = weekly_habits.count(1)
missed = weekly_habits.count(0)

did = 0
not_ = 0

for day in weekly_habits:
    if day == 0:
        not_+=1
    else:
        did+=1

print('\nDays completed:', did)
print('Days missed:', not_)
if did > not_:
    print("Good job on following your habits!\n")
else:
    print("Keep trying to improve. This isn't good.\n")

print('='*20)
print("WEEKLY HABIT TRACKER")
print("\nHabit name:", habit_info[0])
print("Weekly Record:", weekly_habits)
print("Completed:", did)
print("Missed", not_)
print('='*20)