def main() -> None:
    n = int(input())
    solutions = []
    output = 0
    for i in range(n):
        solutions.append(input())

    for s in solutions:
        if s.count('1') >= 2:
            output += 1

    print(output)
if __name__ == '__main__':
    main()