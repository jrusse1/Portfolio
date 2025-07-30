grades = [92, 94, 99, 100, 89]
grade_avg = sum(grades)/len(grades)
if grade_avg >= 90 and grade_avg <= 100:
	lettergrade = "A"
if grade_avg >= 80 and grade_avg < 90:
	lettergrade = "B"	
if grade_avg >= 70 and grade_avg < 80:
	lettergrade = "C"	
if grade_avg >= 60 and grade_avg < 70:
	lettergrade = "D"	
if grade_avg < 60:
	lettergrade = "F"	
print("Your grade is:", lettergrade)
