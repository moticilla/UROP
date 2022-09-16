import csv

word_freq = {
"Hello": 56,
"at": 23,
"test": 43,
"this": 43
}

#print(word_freq)

csv_filename = 'my_csv_experiment.csv'
with open(csv_filename) as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)