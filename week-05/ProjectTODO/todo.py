from model import Model
from viewer import Viewer
import sys

class Todo:
    def __init__(self):
        self.model = Model()
        self.viewer = Viewer()

    def handle_arguments(self):
        if len(sys.argv) ==1:
            self.viewer.print_usage()
        else:
            if sys.argv[1] == '-l':
                self.model.readlines_todo()
                if len(self.model.todo) < 1:
                    self.viewer.for_empty_list()
                else:
                    self.viewer.print_list(self.model.todo)

            if sys.argv[1] == '-a':
                if len(sys.argv) == 3:
                    self.model.add_todo(sys.argv[2] + '\n')
                elif len(sys.argv) > 3:
                    self.viewer.only_1_task()
                else:
                    self.viewer.print_no_task()

            if sys.argv[1] == '-r':
                if len(sys.argv) == 3:
                    try:
                        self.model.rem_todo(sys.argv[2])
                    except ValueError:
                        self.viewer.print_if_value()
                    except IndexError:
                        self.viewer.print_indexerror()

            if sys.argv[1] == '-c':
                if len(sys.argv) == 3:
                    try:
                        self.model.completed_todo(sys.argv[2])
                    except ValueError:
                        self.viewer.print_if_value()
                    except IndexError:
                        self.viewer.print_indexerror()

todo1 = Todo()
todo1.handle_arguments()
