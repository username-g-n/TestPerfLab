import math

def inCircle(r_circle,x_point, y_point):
    hypotenuse = math.sqrt(x_point ** 2 + y_point ** 2)
    if hypotenuse < r_circle:
        print("1")
    elif hypotenuse > r_circle:
        print("2")
    elif hypotenuse == r_circle:
        print("0")

def main():
    with open('circle.txt', 'r') as f:
        data = list(map(int,f.read().replace("\n", " ").split()))
    point = open('point.txt')
    r_circle = data[2];
    for line in point:
        lines = list((line.replace("\n", " ").split()))
        x_point = int(lines[0])-data[0]
        y_point = int(lines[1])-data[1]
        inCircle(r_circle,x_point,y_point)

if __name__ == '__main__':
    main()
    input('Press ENTER to exit')
