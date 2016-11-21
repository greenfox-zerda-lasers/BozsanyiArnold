class Viewer:
    def print_usage(self):
        print('after the \'python todo.py\' you could put\n -l if you want to see the list,\n -a if you want to add to the list\n -r if you want to remove from ur list \n -c for complete a task')

    def for_empty_list(self):
        print('You have nothing to do today.')

    def print_list(self,todolist):
        for index, value in enumerate(todolist, start = 1):
            print(str(index) +  value)

    def print_no_task(self):
        print('Unable to add: No task provided.')

    def print_if_value(self):
        print('Please insert a number for which you want to delete.')

    def print_indexerror(self):
        print('Unable to remove: Index is out of bound')
    def only_1_task(self):
        print('Only one task at a time please.')
    def command_please(self):
        pass
