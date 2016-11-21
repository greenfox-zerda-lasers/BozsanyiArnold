# Create a class the displays the Elevator art and navigation (list of commands)
class Viewer:
    def draw(self,height,ppl,position):
        print('___________________________________')
        print('`._______________________________.\'')
        for i in reversed(range(height)):
            if i == int(position):
                if ppl == 0:
                    print('  _||_||_[_ _]_||_||_______||_||_')
                else:
                    print('  _||_||_[_X_]_||_||_______||_||_')
            else:
                print('   || ||       || ||       || ||')
        print('.\'_______________________________`.')

    def functions(self):
        print('Hi , what would you like to do?\n -To add person to elevator press A + Enter\n -To remove person from the elevator press R + Enter\n -To move to a floor press the number of the floor and the Enter button\n -To eXit please press X + Enter.')
