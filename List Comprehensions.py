# https://www.hackerrank.com/challenges/list-comprehensions/problem

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    print([[i,f,g] for i in range(0, x+1) for f in range(0, y+1) for g in range(0, z+1) if (i+f+g) != n])
