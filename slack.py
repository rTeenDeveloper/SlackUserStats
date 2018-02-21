import csv
import os

inactive = 0
active = 0
bots = 0
users = 0
percentage = 0

with open('<file>') as File:
	reader = csv.reader(File)
	for row in reader:

		if row[3] == '0' and not row[1].startswith('botuser'):
			print("Inactive!")
			inactive += 1

		if row[1].startswith('botuser'):
			bots += 1
			print("Botuser!")

		if row[3] == '1':
			print("Active!")
			active += 1 

		print(row[0] + "\n")
		users += 1

print("Inactive users: " + str(inactive))
users -= bots
print("Total Users: " + str(users))
print("Bot users: " + str(bots))
print("Active Users: " + str(active))
percentage = (float(active) / float(users-bots) * 100)
print("Percentage of active users: " + str(percentage) + '%')
