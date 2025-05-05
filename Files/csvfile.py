import csv
# csv = data file where the data is separated by commas
# NEVER name your file like the module you try to import


with open('10_02_us.csv') as csvFile:
    reader = csv.reader(csvFile)

print(type(reader))
# -> Result: <class '_csv.reader'>

with open('10_02_us.csv') as csvFile:
    #reader = csv.reader(csvFile)
    #for row in reader:
    #    print(row)
    ##^prints everything in the csv file, very long!!
    ## But it doesn't print everything nicely because tabs in the csv file
    ## Use this to remove the "\t"s:
    reader = csv.reader(csvFile, delimiter = '\t')
    for row in reader:
        print(row)
    
    #reader = csv.reader(csvFile, delimiter = '\t')
    ## You can skip lines:
    #next(reader)
    ## You can skip as many lines as you want: 
    #for row in reader:
    #    print(row)

    ## Turn this into a list:
    #reader = csv.DictReader(csvFile, delimiter = '\t')
    #for row in reader:
    #    print(row)


