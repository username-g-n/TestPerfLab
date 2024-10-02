def main():
    with open('mass.txt', 'r') as f:
        data = list(map(int,f.read().replace("\n", " ").split()))
    m = sorted(data)[len(data) // 2]
    print(sum(abs(v - m) for v in data))

if __name__ == '__main__':
    main()
    input('Press ENTER to exit')
