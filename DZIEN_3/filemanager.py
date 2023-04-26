class FileManager:
    def __init__(self,filname,mode,encod):
        self.filname = filname
        self.mode = mode
        self.encod = encod
        self.file = None

    def __enter__(self):
        self.file = open(self.filname,self.mode,encoding=self.encod)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with FileManager('testowy.txt','w','utf-8') as f:
    f.write('to jest test\ni druga linia\ni trzecia linia...')

with FileManager('dodawany.txt','a','utf-8') as f:
    f.write('kolejna linia do pliku ...\n')

with FileManager('dodawany.txt','r','utf-8') as f:
    print(f.read())
