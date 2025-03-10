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

from Solution import Node, OperationHistory, Command, TextEditor
# -------------------------------
# Main block with 30 test cases
# -------------------------------

def run_tests():
    test_num = 1

    # Utility function for test reporting.
    def report(condition, expected, actual):
        nonlocal test_num
        if condition:
            print(f"Test {test_num} passed.")
        else:
            print(f"Test {test_num} failed: Expected '{expected}', got '{actual}'.")
        test_num += 1

    # Test 1: Insert into empty text buffer.
    editor = TextEditor()
    editor.insert(0, "Hello")
    report(editor.get_text() == "Hello", "Hello", editor.get_text())

    # Test 2: Invalid insert (index > length).
    editor = TextEditor()
    result = editor.insert(5, "Hello")
    report(not result and editor.get_text() == "", "Invalid index, empty text", editor.get_text())

    # Test 3: Insert at beginning of non-empty text.
    editor = TextEditor()
    editor.insert(0, "World")
    editor.insert(0, "Hello ")
    report(editor.get_text() == "Hello World", "Hello World", editor.get_text())

    # Test 4: Insert at end of text.
    editor = TextEditor()
    editor.insert(0, "Hello")
    editor.insert(len(editor.get_text()), " World")
    report(editor.get_text() == "Hello World", "Hello World", editor.get_text())

    # Test 5: Insert in the middle.
    editor = TextEditor()
    editor.insert(0, "Helo")
    editor.insert(2, "l")
    report(editor.get_text() == "Hello", "Hello", editor.get_text())

    # Test 6: Valid deletion from the middle.
    editor = TextEditor()
    editor.insert(0, "Hello World")
    editor.delete(5, 1)  # Remove the space
    report(editor.get_text() == "HelloWorld", "HelloWorld", editor.get_text())

    # Test 7: Invalid deletion (negative index).
    editor = TextEditor()
    editor.insert(0, "Hello")
    result = editor.delete(-1, 2)
    report(not result and editor.get_text() == "Hello", "Invalid deletion, unchanged text", editor.get_text())

    # Test 8: Invalid deletion (length exceeds).
    editor = TextEditor()
    editor.insert(0, "Hello")
    result = editor.delete(2, 10)
    report(not result and editor.get_text() == "Hello", "Invalid deletion, unchanged text", editor.get_text())

    # Test 9: Deletion with length 0 (should do nothing).
    editor = TextEditor()
    editor.insert(0, "Hello")
    result = editor.delete(2, 0)
    report(result and editor.get_text() == "Hello", "Hello", editor.get_text())

    # Test 10: Undo after insertion.
    editor = TextEditor()
    editor.insert(0, "Hello")
    editor.undo()
    report(editor.get_text() == "", "Empty text after undo", editor.get_text())

    # Test 11: Undo after deletion.
    editor = TextEditor()
    editor.insert(0, "Hello World")
    editor.delete(5, 1)
    editor.undo()
    report(editor.get_text() == "Hello World", "Hello World after undo", editor.get_text())

    # Test 12: Redo after undo of insertion.
    editor = TextEditor()
    editor.insert(0, "Hello")
    editor.undo()
    editor.redo()
    report(editor.get_text() == "Hello", "Hello", editor.get_text())

    # Test 13: Redo after undo of deletion.
    editor = TextEditor()
    editor.insert(0, "Hello World")
    editor.delete(5, 1)
    editor.undo()
    editor.redo()
    report(editor.get_text() == "HelloWorld", "HelloWorld", editor.get_text())

    # Test 14: Consecutive undos until no more operations.
    editor = TextEditor()
    editor.insert(0, "Hello")
    editor.insert(5, " World")
    editor.delete(0, 5)  # Delete "Hello"
    editor.undo()  # Undo delete -> "Hello World"
    editor.undo()  # Undo second insert -> "Hello"
    editor.undo()  # Undo first insert -> ""
    result = editor.undo()  # Nothing to undo
    report(editor.get_text() == "" and not result, "Empty text and no undo", editor.get_text())

    # Test 15: Consecutive redos after multiple undos.
    editor = TextEditor()
    editor.insert(0, "Hello")
    editor.insert(5, " World")
    editor.delete(0, 5)  # Delete "Hello", text becomes " World"
    editor.undo()  # Undo delete -> "Hello World"
    editor.undo()  # Undo second insert -> "Hello"
    editor.undo()  # Undo first insert -> ""
    editor.redo()  # Redo first insert -> "Hello"
    editor.redo()  # Redo second insert -> "Hello World"
    editor.redo()  # Redo delete -> " World"
    report(editor.get_text() == " World", "' World'", editor.get_text())

    # Test 16: Undo with no operations.
    editor = TextEditor()
    result = editor.undo()
    report(not result and editor.get_text() == "", "Nothing to undo", editor.get_text())

    # Test 17: Redo with no operations.
    editor = TextEditor()
    result = editor.redo()
    report(not result and editor.get_text() == "", "Nothing to redo", editor.get_text())

    # Test 18: Complex sequence of operations.
    editor = TextEditor()
    editor.insert(0, "abc")
    editor.insert(3, "def")
    editor.delete(2, 2)
    editor.insert(2, "XYZ")
    editor.undo()
    editor.undo()
    editor.redo()
    editor.redo()
    report(editor.get_text() == "abXYZef", "abXYZef", editor.get_text())

    # Test 19: Insert empty string (should change nothing).
    editor = TextEditor()
    editor.insert(0, "Hello")
    editor.insert(3, "")
    report(editor.get_text() == "Hello", "Hello", editor.get_text())

    # Test 20: Delete entire text.
    editor = TextEditor()
    editor.insert(0, "Hello World")
    editor.delete(0, len(editor.get_text()))
    report(editor.get_text() == "", "Empty text", editor.get_text())

    # Test 21: Undo deletion of entire text.
    editor.undo()
    report(editor.get_text() == "Hello World", "Hello World", editor.get_text())

    # Test 22: Redo after undo of deletion of entire text.
    editor.redo()
    report(editor.get_text() == "", "Empty text", editor.get_text())

    # Test 23: Multiple undos/redos with mixed operations.
    editor = TextEditor()
    editor.insert(0, "Start")
    editor.insert(5, " Middle")
    editor.insert(12, " End")
    editor.delete(0, 5)   # Remove "Start"
    editor.undo()         # Undo delete -> "Start Middle End"
    editor.undo()         # Undo insert " End" -> "Start Middle"
    editor.insert(12, " End!")  # New operation clears redo history
    result = editor.redo()      # Should fail because redo history was cleared
    report(editor.get_text() == "Start Middle End!" and not result,
           "Start Middle End!", editor.get_text())

    # Test 24: Delete with index at end boundary.
    editor = TextEditor()
    editor.insert(0, "Hello")
    editor.delete(4, 1) # Removing last character ('o')
    report(editor.get_text() == "Hell", "Hell", editor.get_text())

    # Test 25: Invalid insert with negative index.
    editor = TextEditor()
    result = editor.insert(-1, "Test")
    report(not result and editor.get_text() == "", "Invalid index, empty text", editor.get_text())

    # Test 26: Valid deletion where index equals text length minus deletion length.
    editor = TextEditor()
    editor.insert(0, "Hello")
    editor.delete(3, 2) # Delete last 2 characters ("lo")
    report(editor.get_text() == "Hel", "Hel", editor.get_text())

    # Test 27: Check that redo history is cleared after a new operation.
    editor = TextEditor()
    editor.insert(0, "Hello")
    editor.insert(5, " World")
    editor.undo()      # Undo second insert -> "Hello"
    editor.insert(5, ", there")
    result = editor.redo()  # Should fail because redo history was cleared
    report(editor.get_text() == "Hello, there" and not result,
           "Hello, there", editor.get_text())

    # Test 28: Sequence of multiple operations.
    editor = TextEditor()
    editor.insert(0, "A")
    editor.insert(1, "B")
    editor.insert(2, "C")
    editor.delete(1, 1)  # Remove "B", expect "AC"
    editor.insert(1, "D")  # Expect "ADC"
    report(editor.get_text() == "ADC", "ADC", editor.get_text())

    # Test 29: Undo/Redo order correctness.
    editor = TextEditor()
    editor.insert(0, "123")
    editor.insert(3, "456")
    editor.delete(2, 2)  # "123456" becomes "1256" (delete characters at index 2 & 3)
    editor.undo()        # Undo delete -> "123456"
    editor.undo()        # Undo second insert -> "123"
    editor.redo()        # Redo second insert -> "123456"
    report(editor.get_text() == "123456", "123456", editor.get_text())

    # Test 30: Edge condition: All operations undone leading to empty text.
    editor = TextEditor()
    editor.insert(0, "Edge")
    editor.delete(0, 4)   # Now empty
    editor.undo()         # Undo delete -> "Edge"
    editor.undo()         # Undo insert -> ""
    report(editor.get_text() == "", "Empty text", editor.get_text())

if __name__ == "__main__":
    run_tests()
