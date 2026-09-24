
def count_bands(scores):
    scores_int = []
    for score in scores:
        scores_int.append(int(score))
    count0_49 = 0
    count50_64=0
    count65_74 =0
    count75_84=0
    count85_100=0
    for score in scores_int:
        if 0<=score<=49:
            count0_49+=1
        elif 50<=score<=64:
            count50_64+=1
        elif 65<=score<=74:
            count65_74+=1
        elif 75<=score<=84:
            count75_84+=1
        else:
            count85_100+=1
    return [count0_49,count50_64,count65_74,count75_84,count85_100]
    

def process_scores(in_filename="scores.txt", out_filename="distributions.txt"):
    outfile = open("distributions.txt", "w")
    infile = open("scores.txt", "r")
    for line in infile:
        line=line.strip()
        if line:
            student_score = line.split(',')
            student_counts=count_bands(student_score[1:]) #example line of student_counts: 1,1,0,0,1
            for count in student_counts[:-1]:           
                outfile.write(f'{count},')
            outfile.write(f'{student_counts[-1]}') 
            outfile.write(f'\n')
process_scores()      