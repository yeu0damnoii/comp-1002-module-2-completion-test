def maximum_score(scores):
    scores_int = []
    for score in scores:
        scores_int.append(int(score))
    return max(scores_int)



def process_scores(in_filename="scores.txt", out_filename="maximums.txt"):
    outfile = open("maximums.txt", "w")
    infile = open("scores.txt", "r")

    maximum_scores = []
    maximum_of_maximum_scores = []
    for line in infile:
        line=line.strip()
        if line:
            student_score = line.split(',')
            maximum=maximum_score(student_score[1:])
            maximum_scores .append([student_score[0], maximum])
            maximum_of_maximum_scores.append(maximum)
    outfile.write(f'{max(maximum_of_maximum_scores)}\n')
    for item in maximum_scores:
        line = item[0] + ',' + str(item[1]) + '\n'
        outfile.write(line)

    return maximum_scores 

process_scores()
        

