with open ("superstar.txt", "r") as r:
    r = r.readlines()    
print (f"množstvo suťažiacich je {len(r)}")
početHlasov = {}
for i in range (len(r)):
    r[i] = r[i].replace("\n", "")
    hlas = (r[i][len(r[i])-2])
    if hlas in početHlasov:
        početHlasov[hlas] += 1
    else:
        početHlasov[hlas] = 1
topContestant, topContestantLetter = 0, ""
for i in početHlasov:
    if početHlasov[i] > topContestant:
        topContestant = početHlasov[i]
        topContestantLetter = i
print (f"Súťaž vyhral {topContestantLetter} s {topContestant} hlasmi")