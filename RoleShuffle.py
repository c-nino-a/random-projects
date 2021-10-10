import random

role=["jeman","nino","drake","brent"]
names=["vinny","judge","def","gurl"]

random.shuffle(names)
random.shuffle(role)

for i in range(len(role)):
    print(role[i]+" - "+names[i])
