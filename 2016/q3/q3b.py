import re
def main():
    num_triangles = 0
    with open("inputQ3.txt", "r") as f:
        while True:
            line1 = f.readline()
            if not line1:
                break
            line1 = line1.strip()
            line1 = re.findall(r'\d+', line1)
            line1 = [int(x) for x in line1]

            line2 = f.readline()
            line2 = line2.strip()
            line2 = re.findall(r'\d+', line2)
            line2 = [int(x) for x in line2]

            line3 = f.readline()
            line3 = line3.strip()
            line3 = re.findall(r'\d+', line3)
            line3 = [int(x) for x in line3]

            a1 = line1[0]
            a2 = line2[0]
            a3 = line3[0]

            b1 = line1[1]
            b2 = line2[1]
            b3 = line3[1]

            c1 = line1[2]
            c2 = line2[2]
            c3 = line3[2]
            
            if a1 + a2 > a3 and a1 + a3 > a2 and a2 + a3 > a1:
                num_triangles += 1

            if b1 + b2 > b3 and b1 + b3 > b2 and b2 + b3 > b1:
                num_triangles += 1

            if c1 + c2 > c3 and c1 + c3 > c2 and c2 + c3 > c1:
                num_triangles += 1

    print(num_triangles)

if __name__ == "__main__":
    main()
