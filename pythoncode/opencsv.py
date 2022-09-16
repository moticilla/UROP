import csv

#with open('my_csv_experiment.csv', mode='r') as infile:
#    reader = csv.reader(infile)
#    with open("/Users/Documents/UROP/my_csv_experiment.csv", mode='w') as outfile:
#        writer = csv.writer(outfile)
#        mydict = {rows[0]:rows[5] for rows in reader}

#experiment_dict = csv.DictReader(open("my_csv_experiment.csv"))

with open("/home/elliep/Documents/UROP/my_csv_experiment.csv", mode='r') as infile:
    reader = csv.reader(infile)
    with open("/home/elliep/Documents/UROP/my_csv_experiment.csv", mode='w') as outfile:
        writer = csv.writer(outfile)
        mydict = {rows[0]:rows[5] for rows in reader}