class Model:
    todo = []
    status = ' - (_) '
    def readlines_todo(self):
        f = open('list.txt')
        self.todo = f.readlines()
        f.close()

    def add_todo(self, what):
        f = open('list.txt', 'a')
        f.write( self.status + what)
        f.close()

    def completed_todo(self,which):
        self.readlines_todo()
        self.todo[int(which)-1] = self.todo[int(which)-1].replace('_', 'x')
        self.write_file()

    def rem_todo(self,which):
        self.readlines_todo()
        del self.todo[int(which)-1]
        self.write_file()

    def write_file(self):
        f = open('list.txt', 'w')
        f.write(''.join(self.todo))
