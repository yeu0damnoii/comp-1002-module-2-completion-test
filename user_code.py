outfile = open("averages.txt", "w")
infile = open("scores.txt", "r")
lis= infile.readlines()
for line in lis:
    student = line.split(",")
    total = 0
    count = 0
    for i in student[1:]:
        i=int(i)
        count +=1
        total+=i
    if count == 0 or total ==0:
        continue
    else:
        print(count)
        print(total)
        print(round(total/count,1))
        print()


outfile.close()
infile.close()


