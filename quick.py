import json

opted_out_file = open("opted_out.txt", "r")
opted_out_authors = opted_out_file.read().split("\n")
opted_out_file.close()

print(opted_out_authors)

with open("opted_out.json", "w") as file:
	json.dump(opted_out_authors, file, indent = 3)