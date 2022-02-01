# Import the argparse library
import argparse
import sys

# Overriding the error function in argparse so that it doesn't print the usage every time
class MyParser(argparse.ArgumentParser):
    def error(self, message):
        pass


parser = MyParser()
subparser = parser.add_subparsers(dest="command")

usage = """Usage :-
$ ./task add 2 hello world    # Add a new item with priority 2 and text "hello world" to the list
$ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order
$ ./task del INDEX            # Delete the incomplete item with the given index
$ ./task done INDEX           # Mark the incomplete item with the given index as complete
$ ./task help                 # Show usage
$ ./task report               # Statistics"""


def sortBasedOnPriority(item):
    priority = int(item.split()[0])
    return priority


def getTask(item):
    items = item.split()
    task = " ".join(items[1:])
    priority = f" [{items[0]}]"
    finalString = task + priority
    return finalString


def getLines(file):
    with open(file, "r") as f:
        lines = f.readlines()
        return lines


def putLines(file, lines):
    with open(file, "w") as f:
        f.writelines(lines)


# Adding the syntax of the program
list = subparser.add_parser("ls")

add = subparser.add_parser("add")
add.add_argument("p", type=int)
add.add_argument("task", type=str, nargs="+")

delete = subparser.add_parser("del")
delete.add_argument("index", type=int)

done = subparser.add_parser("done")
done.add_argument("index", type=int)

report = subparser.add_parser("report")

help = subparser.add_parser("help")

# Parsing the commands and arguments from the input :
args = parser.parse_args()

# ls command
if args.command == "ls":
    try:
        lines = getLines("task.txt")
        if len(lines) == 0:
            print("There are no pending tasks!")
        else:
            for i in range(0, len(lines)):
                print(f"{i+1}. {getTask(lines[i])}")
    except FileNotFoundError:
        print("There are no pending tasks!")

# add command
elif args.command == "add":
    if args.p == None or args.task == None:
        print("Error: Missing tasks string. Nothing added!")
    else:
        task = " ".join(args.task)
        data = f"{args.p} {task}\n"
        lines = []
        try:
            lines = getLines("task.txt")
        except FileNotFoundError:
            pass
        lines.append(data)
        lines.sort(key=sortBasedOnPriority)
        putLines("task.txt", lines)
        print(f"""Added task: "{task}" with priority {args.p}""")

# delete command
elif args.command == "del":
    if args.index == None:
        print("Error: Missing NUMBER for deleting tasks.")
    else:
        try:
            if args.index < 1:
                raise ValueError
            lines = getLines("task.txt")
            lines.pop(args.index - 1)
            putLines("task.txt", lines)
            print(f"Deleted task #{args.index}")

        except:
            print(
                f"Error: task with index #{args.index} does not exist. Nothing deleted."
            )


# done command
elif args.command == "done":
    if args.index == None:
        print("Error: Missing NUMBER for marking tasks as done.")
    else:
        try:
            if args.index < 1:
                raise ValueError
            lines = getLines("task.txt")
            ele = lines.pop((args.index) - 1)
            putLines("task.txt", lines)

            ele = ele.split()
            ele = " ".join(ele[1:])
            lines = []
            try:
                lines = getLines("completed.txt")
            except FileNotFoundError:
                pass
            lines.append(ele + "\n")
            putLines("completed.txt", lines)
            print("Marked item as done.")

        except:
            print(f"Error: no incomplete item with index #{args.index} exists.")

# report
elif args.command == "report":
    try:
        lines = getLines("task.txt")
        print("Pending :", len(lines))
        for i in range(0, len(lines)):
            print(f"{i+1}. {getTask(lines[i])}")
    except FileNotFoundError:
        print("Pending : 0")

    try:
        lines = getLines("completed.txt")
        print("\nCompleted :", len(lines))
        for i in range(0, len(lines)):
            print(f"{i+1}. {lines[i]}", end="")
    except FileNotFoundError:
        print("\nCompleted : 0")

# help command
elif args.command == "help" or args.command == None:
    sys.stdout.buffer.write(usage.encode("utf8"))
