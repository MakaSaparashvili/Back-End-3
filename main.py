students = [("Alice", 85),
            ("Bob", 78),
            ("Charlie", 92),
            ("David", 85),
            ("Eve", 78),
            ("Frank", 85),
            ("Mark", 50),
            ("George", 21)]


# Unique Grades:
grades = {score for name, score in students}
print("Unique grades:", grades)

# Top Performers:
top_students = sorted(students, key=lambda x: x[1], reverse=True)[:3]
print("Top performers:", [name for name, score in top_students])

# Failed Students:
failed_students = [(name, score) for name, score in students if score < 51]
print("Failed students:", failed_students)
