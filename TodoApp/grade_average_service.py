def calculate(Dictionary):
    result=0
    for x in Dictionary.values():
        result += x
    final_grade= result / len(Dictionary)
    print(final_grade)