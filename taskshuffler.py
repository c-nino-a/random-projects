import random

tasks=["youtube watch later elimination","watch anime","do python random projects","watch movie","repair computer","draw stuff","database course","organize room","do python courses","read books real stuff","database course","do python random projects","read books fantasy","watch self help youtube","read school stuff","do system projects","watch fun youtube","read books real stuff","draw stuff","world build","quiz yourself on school stuff","watch animeworld build","quiz yourself on school stuff",'read books fantasy','try opencv','watch fun youtube','do system projects','repair computer','try opencv','watch movie','youtube watch later elimination','organize notion','organize notion','organize room','read school stuff','do python courses','watch self help youtube']
tasks=list(set(tasks))

random.shuffle(tasks)
for task in tasks:
    print(task)