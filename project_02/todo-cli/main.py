import json
import click
import os

TODO_CLI="todo.json"

def load_task():
    if not os.path.exists(TODO_CLI):
        return []
    with open(TODO_CLI,"r") as file:
        return json.load(file)

def save_task(tasks):
    with open(TODO_CLI,"w") as file:
        json.dump(tasks,file,indent=4)

@click.group()
def cli():
    """Cli base application"""
    pass

@click.command()
@click.argument("task")
def add(task):
    tasks=load_task()
    tasks.append({"task":task ,"done":False})
    save_task(tasks)
    click.echo(f"task added : {task}")

@click.command()
def list():
    tasks=load_task()
    if not tasks:
        click.echo("No Task found")
        return
    for index, task in enumerate(tasks,1):
        status="✅" if task["done"] else "❌"
        click.echo(f"{index} . {task['task']} [{status}]")

@click.command()
@click.argument("task_number",type=int)
def complete(task_number):
    tasks=load_task()
    if task_number > 0 and task_number <= len(tasks):
        tasks[task_number -1]['done']=True
        save_task(tasks)
        click.echo(f"Task  {task_number} has been done Sucessfully. ")
    else:
        click.echo("Invalid task number.")


@click.command()
@click.argument("task_number",type=int)
def remove(task_number):
    tasks=load_task()
    if task_number >0 and task_number <=len(tasks):
        remove_task=tasks.pop(task_number -1)
        save_task(tasks)
        click.echo(f"Removed task : {task_number}.{remove_task['task']}")
    else:
        click.echo("Invalid task number.")



cli.add_command(add)
cli.add_command(complete)
cli.add_command(remove)
cli.add_command(list)


if __name__ =="__main__":
    cli()
