

class Uncen():
    def __init__(self, cen, vowels):
        self.cen=cen
        self.vowels=vowels
        self.check()
        self.replace()
    
    def check(self):
        clean=""
        count=self.cen.count("*")
        if count!=len(self.vowels):
            SystemExit
        print(count)

    def replace(self):
        while self.cen.count("*") > 0:
            self.cen=self.cen.replace("*",self.vowels[0],1)
            self.vowels=self.vowels.replace(self.vowels[0],"",1)
        print(self.cen)


Uncen("Wh*r* d*d my v*w*ls g*?", "eeioeo")
Uncen("abcd", "")
Uncen("*PP*RC*S*", "UEAE")