infile = r"/Users/johnathanmo/Downloads/Collins Scrabble Words.txt"
outfile = r"WordHuntWords.txt"

with open(infile) as fin, open(outfile, "w+") as fout:
    for line in fin:
        print(line)
        if len(line) > 3:
            fout.write(line)
        else:
            print("no")