lines_seen = set() # holds lines already seen
outfile = open("aroma_zone_link.txt", "w")
count = 0
count_total = 0
for line in open("aroma_zone_link_clean.txt", "r"):
    count_total += 1
    if line not in lines_seen: # not a duplicate
        count += 1
        outfile.write(line)
        lines_seen.add(line)
outfile.close()
print("Record totali: " + str(count_total))
print("Record rimasti: " + str(count))