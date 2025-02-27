def student_report(name, *scores):
    avg = sum(scores) / len(scores)
    print(f"{name}: Average = {avg}")

student_report("Rahim", 85, 90, 78, 50, 4, 0, 5, 254)