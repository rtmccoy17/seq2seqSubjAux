

fi = open("ptb.plainSents.txt", "r")
fo = open("ptb.fwdRev.txt", "w")

for line in fi:
    sent = line.strip()
    v1 = "FWD " + sent
    v2 = "REV " + sent
    revSent = " ".join(list(reversed(sent.split())))

    fo.write(v1 + "\t" + sent + "\n")
    fo.write(v2 + "\t" + revSent + "\n")

