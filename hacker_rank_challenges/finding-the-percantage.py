if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    ocenki = student_marks[query_name]
    sumaocenki=(sum(ocenki)/3)
    print("{0:.2f}".format(sumaocenki))