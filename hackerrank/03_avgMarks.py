if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    requestedMarks = student_marks[query_name]

    avgScore = sum(requestedMarks)/len(requestedMarks)

    # write in 2 decimel digits
    print(f"{avgScore:.{2}f}")