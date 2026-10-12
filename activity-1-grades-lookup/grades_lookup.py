student_grades = {
    "Elara": 85,
    "Kwame": 92,
    "Siobhan": 78,
    "Kai": 96,
    "Kyle" : 73
}

student_grades["Kwame"] = 96 # could also just change the value in theh original hash table

print(student_grades["Kwame"])
print(student_grades.get("Aisha", "Not found"))

result = student_grades["Elara"]
print(result)

print(student_grades.get("Aisha", "Not found"))

print(student_grades["Kyle"])