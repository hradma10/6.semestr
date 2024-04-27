from TaskManager import TaskManager

def sum(list):
    sum_of_numbers = 0
    for el in list:
        sum_of_numbers += el
    print(sum_of_numbers)
    
manager = TaskManager()

manager.createTaskAndAdd("Uklidit", "Text")

manager.printTasks()

manager.setTaskAsDone(1)

manager.printTasks()

list = [1,5,2,9,1]

sum(list)



