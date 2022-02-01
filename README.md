Priority TODO List

- Done as a part of the Selection Process of the Global Digital Corps Software Engineering Fellowship.

- Task : Implement a command-line (CLI) program that lets you manage your tasks.


[![TASK-CLI](https://res.cloudinary.com/sv-co/image/upload/v1638058186/GDC/SE/Admission/gdc-home-page_b6s3go.png)](https://vimeo.com/648902045)
## Getting started

1. Install Python: Python is usually installed by default on most modern systems. To check what your currently have, open a terminal and run the following command:

   ```
   python3 --version
   ```

   This should output some information on the installed Python version.
   You can also install python by following these instructions: https://installpython3.com/


2. Once you are done with the changes you should be able to execute the task app by running the following command from the terminal.

   **On Windows:**

   ```
   .\task.bat
   ```

   **On \*nix:**

   ```
   ./task.sh
   ```

### Create Create symbolic link to the executable file

#### On Windows

To create a symbolic link on Windows, you'll need to run either the Windows Command Prompt, or Windows Powershell **with administrator privileges**. To do so, right-click on the icon for Command Prompt, or Powershell, and choose the _"Run as Administrator"_ option.

**Command Prompt:**

```
> mklink task task.bat
```

**Powershell:**

```
> cmd /c mklink task task.bat
```

#### On \*nix:

Run the following command in your shell:

```
$ ln -s task.sh task
```

## A Note about `/` for Windows Users

In the following sections, you'll see many commands prefixed with `./`, or paths containing the `/` (forward-slash) character.

If you're using the Windows _Command Prompt_, then you'll need to replace `/` with `\` (back-slash) for these commands and paths to work as expected.

On Windows _Powershell_, these substitutions are not required.

## Usage

### 1. Help

Executing the command without any arguments, or with a single argument help prints the CLI usage.

```
$ ./task help
Usage :-
$ ./task add 2 hello world    # Add a new item with priority 2 and text "hello world" to the list
$ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order
$ ./task del INDEX            # Delete the incomplete item with the given index
$ ./task done INDEX           # Mark the incomplete item with the given index as complete
$ ./task help                 # Show usage
$ ./task report               # Statistics
```

### 2. List all pending items

Use the ls command to see all the items that are not yet complete, in ascending order of priority.

Every item should be printed on a new line. with the following format

```
[index] [task] [priority]
```

Example:

```
$ ./task ls
1. change light bulb [2]
2. water the plants [5]
```

index starts from 1, this is used to identify a particular task to complete or delete it.

### 3. Add a new item

Use the add command. The text of the task should be enclosed within double quotes (otherwise only the first word is considered as the item text, and the remaining words are treated as different arguments).

```
$ ./task add 5 "the thing i need to do"
Added task: "the thing i need to do" with priority 5
```

### 4. Delete an item

Use the del command to remove an item by its index.

```
$ ./task del 3
Deleted item with index 3
```

Attempting to delete a non-existent item should display an error message.

```
$ ./task del 5
Error: item with index 5 does not exist. Nothing deleted.
```

### 5. Mark a task as completed

Use the done command to mark an item as completed by its index.

```
$ ./task done 1
Marked item as done.
```

Attempting to mark a non-existed item as completed will display an error message.

```
$ ./task done 5
Error: no incomplete item with index 5 exists.
```

### 6. Generate a report

Show the number of complete and incomplete items in the list. and the complete and incomplete items grouped together.

```
$ ./task report
Pending : 2
1. this is a pending task [1]
2. this is a pending task with priority [4]

Completed : 3
1. completed task
2. another completed task
3. yet another completed task
```
