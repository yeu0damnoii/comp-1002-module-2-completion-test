def calculate_average(scores):
    if not scores:
        return 0.0
    total = sum(int(s) for s in scores)
    return total / len(scores)

def process_scores(in_filename="scores.txt", out_filename="averages.txt"):
    averages = []
    with open(in_filename, "r") as infile:
        for line in infile:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            scores = parts[1:]
            avg = calculate_average(scores)
            averages.append(round(avg, 1))
            
    with open(out_filename, "w") as outfile:
        for avg in averages:
            outfile.write(f"{avg:.1f}\n")
            
    return averages



