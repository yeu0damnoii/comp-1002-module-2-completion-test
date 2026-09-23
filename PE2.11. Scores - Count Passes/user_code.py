def count_passes(scores):
    count = 0
    for score in scores:
        if int(score) >= 50:
            count +=1
    return count

def process_scores(in_filename="scores.txt", out_filename="passes.txt"):
    outfile = open("passes.txt", "w")
    infile = open("scores.txt", "r")
    for line in infile:
        line=line.strip()
        if line:
            student_score = line.split(',')
            pass_score=count_passes(student_score[1:])
            outfile.write(f"{student_score[0]},{pass_score}\n")

    outfile.close()
    infile.close()

process_scores()