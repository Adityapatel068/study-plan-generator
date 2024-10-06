q = ("Welcome To Study Plan Generator Made By Aditya".center(135,'_'))
print(q)
i = int(input("enter the hours you can study each day:- "))
subjects = []
n = int(input("How many subjects/topics do you want to study? "))
for i in range(n):
    subject = input(f"Enter subject {i+1}: ")
    subjects.append(subject)
print(f"Your study subjects are: {subjects}")
hours_per_subject = i / len(subjects)
study_plan = {subject: hours_per_subject for subject in subjects}

print(f"Here’s your time allocation: {study_plan}")
# Step 3: Generate daily schedule
def generate_schedule(study_plan):
    print("\nDaily Study Plan:")
    for subject, hours in study_plan.items():
        print(f"{subject}: {hours:.2f} hours")


