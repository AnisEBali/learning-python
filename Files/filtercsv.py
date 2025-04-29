import csv

with open('10_02_us.csv', 'r') as csvFile:
    data = list(csv.DictReader(csvFile, delimiter='\t'))

# Prime number function:
primes = []
for number in range(2, 99999):
    is_prime = True
    for factor in range(2, int(number**0.5) + 1):
        if number % factor == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(number)

# Filter the CSV file if the post code is a prime number and the state MA
data = [row for row in data if int(row['postal code']) in primes and row['state code'] == 'MA']
print(len(data))

# Writing a new CSV file:
with open('10_02_ma_prime.csv', 'w') as writeCSV:
    writer = csv.writer(writeCSV)
    for row in data:
        writer.writerow([row['place name'], row['county']])
# Changes direcly into the same file!