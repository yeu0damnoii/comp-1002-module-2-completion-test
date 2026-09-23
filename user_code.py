

def calculate_average(scores:list):
    total = 0
    count = 0
    for i in scores:
        i=int(i)
        count +=1
        total+=i
    if total > 0:
        return (round(total/count,1))
    

def process_scores(in_filename="scores.txt", out_filename="averages.txt"):
    outfile = open("averages.txt", "w")
    infile = open("scores.txt", "r")
    #lis= infile.readlines()
    averages = []
    for line in infile:
        line=line.strip()
        if not line:
            continue
        scores = line.split(",")
        avg = calculate_average(scores[1:])
        outfile.write(f"{avg}\n")
        averages.append(avg)
    outfile.close()
    infile.close()
    return averages



