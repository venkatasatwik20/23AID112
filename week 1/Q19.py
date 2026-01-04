#Q19
grades = [85, 92, 78, 65, 88, 91, 73, 89, 55, 94]

results = {
    "A": 0,
    "B": 0,
    "C": 0,
    "Below 70": 0
}

for grade in grades:
    if grade >= 90:
        results["A"] += 1
    elif grade >= 80:
        results["B"] += 1
    elif grade >= 70:
        results["C"] += 1
    else:
        results["Below 70"] += 1

for key, value in results.items():
    print(f"{key}: {value}")
