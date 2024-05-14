def test_syntax_error():
    try:
        print("Hello, world!"
    except SyntaxError as e:
        print("SyntaxError occurred:", e)

def test_indentation_error():
    try:
        def my_function():
        print("Hello, world!")
    except IndentationError as e:
        print("IndentationError occurred:", e)

def test_name_error():
    try:
        print(x)
    except NameError as e:
        print("NameError occurred:", e)

def test_type_error():
    try:
        result = 5 + "10"
    except TypeError as e:
        print("TypeError occurred:", e)

def test_zero_division_error():
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        print("ZeroDivisionError occurred:", e)

def test_file_not_found_error():
    try:
        with open("nonexistent_file.txt", "r") as file:
            content = file.read()
    except FileNotFoundError as e:
        print("FileNotFoundError occurred:", e)

def test_index_error():
    try:
        my_list = [1, 2, 3]
        print(my_list[3])
    except IndexError as e:
        print("IndexError occurred:", e)

def test_key_error():
    try:
        my_dict = {"a": 1, "b": 2}
        print(my_dict["c"])
    except KeyError as e:
        print("KeyError occurred:", e)

def test_value_error():
    try:
        number = int("abc")
    except ValueError as e:
        print("ValueError occurred:", e)

def test_attribute_error():
    try:
        class MyClass:
            pass

        obj = MyClass()
        print(obj.attribute)
    except AttributeError as e:
        print("AttributeError occurred:", e)

def test_import_error():
    try:
        import non_existent_module
    except ImportError as e:
        print("ImportError occurred:", e)

def test_keyboard_interrupt():
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("KeyboardInterrupt occurred")

def test_assertion_error():
    try:
        assert 1 == 2, "Assertion failed: 1 is not equal to 2"
    except AssertionError as e:
        print("AssertionError occurred:", e)

def test_memory_error():
    try:
        huge_list = [0] * 10**10
    except MemoryError as e:
        print("MemoryError occurred:", e)

def test_overflow_error():
    try:
        result = 10**1000
    except OverflowError as e:
        print("OverflowError occurred:", e)

if __name__ == "__main__":
    test_syntax_error()
    test_indentation_error()
    test_name_error()
    test_type_error()
    test_zero_division_error()
    test_file_not_found_error()
    test_index_error()
    test_key_error()
    test_value_error()
    test_attribute_error()
    test_import_error()
    test_keyboard_interrupt()
    test_assertion_error()
    test_memory_error()
    test_overflow_error()
