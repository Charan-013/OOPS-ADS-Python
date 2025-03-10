# -------------------------------
# Text Editor with Undo/Redo Functionality (Python)
#
# This implementation uses:
# 1. A Command class to record each editing operation.
# 2. A TextEditor class that maintains a text buffer and two histories:
#    - undo_history: A linked list of performed operations.
#    - redo_history: A linked list of undone operations.
#
# The undo_history and redo_history are implemented using a custom linked list
# (OperationHistory) that supports adding an operation record at the head and
# removing the most recent record, achieving a last-in–first-out behavior.
#
# -------------------------------

# Node class for our linked list
class Node:
    def __init__(self,cmd):
        self.cmd = cmd
        self.next = None

# Custom linked list that will simulate a LIFO history (without using the term 'stack')
class OperationHistory:
    def __init__(self):
        self.head = None

    def add_operation(self, command):
        node = Node(command)
        node.next = self.head
        self.head = node

    def remove_last_operation(self):
        if self.head != None:
            last = self.head
            self.head = self.head.next
            return last.cmd
        return 
    
    def clear(self):
        self.head = None
        return

    def is_empty(self):
        return self.head == None

# Command class to record each edit operation
class Command:
    def __init__(self, operation, index, text):
        self.operation = operation
        self.index = index
        self.text = text

class TextEditor:
    def __init__(self):
        self.undo_history = OperationHistory()
        self.redo_history = OperationHistory()
        self.text = ""

    def insert(self, index, new_text):
        if index < 0 or index > len(self.text):
            print("Invalid index for insert")
            return False
        self.text = self.text[:index] + new_text + self.text[index:]
        command = Command("insert", index, new_text)
        self.undo_history.add_operation(command)
        self.redo_history.clear()
        return True

    def delete(self, index, length):
        if index < 0 or length < 0 or index >= len(self.text) or index + length > len(self.text):
            print("Invalid index or length for delete")
            return False
        deleted_text = self.text[index:index + length]
        self.text = self.text[:index] + self.text[index + length:]
        command = Command("delete", index, deleted_text)
        self.undo_history.add_operation(command)
        self.redo_history.clear()
        return True

    def undo(self):
        if self.undo_history.is_empty():
            print("Nothing to undo")
            return False
        last = self.undo_history.remove_last_operation()
        if last.operation == "insert":
            self.text = self.text[:last.index] + self.text[last.index + len(last.text):]
            self.redo_history.add_operation(Command("insert", last.index, last.text))
        elif last.operation == "delete":
            self.text = self.text[:last.index] + last.text + self.text[last.index:]
            self.redo_history.add_operation(Command("delete", last.index, last.text))
        return True

    def redo(self):
        if self.redo_history.is_empty():
            print("Nothing to redo")
            return False
        last = self.redo_history.remove_last_operation()
        if last.operation == "insert":
            self.text = self.text[:last.index] + last.text + self.text[last.index:]
            self.undo_history.add_operation(Command("insert", last.index, last.text))
        elif last.operation == "delete":
            self.text = self.text[:last.index] + self.text[last.index + len(last.text):]
            self.undo_history.add_operation(Command("delete", last.index, last.text))
        return True


    def get_text(self):
        """Returns the current state of the text buffer."""
        return self.text
