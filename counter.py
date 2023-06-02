def countEmail():
    # This first line is provided for you
    name = input("Enter file:")
    if len(name) < 1 : name = "mbox-short.txt"
    handle = open(name)
    senders = dict()
    for line in handle:
        if line.startswith("From "):
            words = line.split()
            senders[words[1]] = senders.get(words[1],0) +1
    big = -1
    bigsender = None
    for k,v in senders.items():
        if v > big:
            big = v
            bigsender = k
    print(bigsender,big)
   


## if you want to test locally run > python counter.py
if __name__ == "__main__":
    countEmail()
