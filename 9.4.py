###
9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. 
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
###

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

mail = dict()
for line in handle:
    wds = line.split()
    if len(wds) < 3 or wds[0] !='From': continue
    mail[wds[1]] = mail.get(wds[1],0)+1
    
maxcount = None
maxword = None
for key, value in mail.items():
    if maxcount is None or value > maxcount:
        maxword = key
        maxcount = value
        
print(maxword, maxcount)
