import re
def main():
    num_triangles = 0
    with open("inputQ3.txt", "r") as f:
        for line in f:
            line = line.strip()
            line = re.findall(r'\d+', line)
            line = [int(x) for x in line]
            a = line[0]
            b = line[1]
            c = line[2]
            if a + b > c and a + c > b and b + c > a:
                num_triangles += 1
    print(num_triangles)

if __name__ == "__main__":
    main()
