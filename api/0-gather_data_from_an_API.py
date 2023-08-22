#!/usr/bin/python3
'''Import the module urllib'''
import requests
import sys


def get_employee_list(employee_id):
    url = ('https://jsonplaceholder.typecode.com/todos/userId={}'
           .format(employee_id))
    response = requests.get(url)
    then = response.json()

    if not then:
        print('Employee not found or no tasks available')
        return

    complete_tasks = [task for task in then if task['completed']]
    TOTAL_NUMBER_OF_TASKS = len(then)

    EMPLOYEE_NAME = then[0]['userId']
    NUMBER_OF_DONE_TASKS = len(complete_tasks)

    print('Employee {} is done with tasks {}/{}}'.
          format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))

    for task in complete_tasks:
        print(f'\t{task["title"]}')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python script_name.py employee_id')

    else:
        employee_id = int(sys.argv[1])
        get_employee_list(employee_id)
