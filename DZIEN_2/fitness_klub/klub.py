class Klub:
    def __init__(self,nr_kb,nazwa_kb,miasto):
        self.nr_kb = nr_kb
        self.nazwa_kb = nazwa_kb
        self.miasto = miasto
        print(self.przypisanie())
        
    def przypisanie(self):
        return f"przypisanie do klubu nr {self.nr_kb}"
    
    def infoklub(self):
        print(f"klub {self.nazwa_kb}, miasto: {self.miasto}")
