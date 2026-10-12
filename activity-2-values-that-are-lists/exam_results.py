exam_results = {
    "steve": [99, 98, 95],
    "violet": [56, 53, 88],
    "aqil": [100, 100, 100],
    "bill": [85, 93, 87]
}

print(exam_results["steve"])
print(exam_results["steve"][0])
print(len(exam_results["steve"]))
print(98 in exam_results["steve"])
print("hello" in exam_results["steve"])

print(exam_results["aqil"][1])

print(sum(exam_results["aqil"]))

print(f"There are {len(exam_results)} students")