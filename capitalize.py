def solve(s):
    
    l = s.split()
    
    l1 = l[0].capitalize()
    l2 = l[1].capitalize()
    
    l.clear()
    l.append(l1)
    l.append(l2)
    
    res =  ' '.join(l)
    
    return (res) 
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
