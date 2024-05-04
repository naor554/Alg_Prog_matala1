def deep_sorted(x:any)->str:
    # Put your code here
    """
    A function that recursively sorts a nested data structure.

    >>> deep_sorted({})
    '{}'

    >>> deep_sorted([])
    '[]'

    >>> deep_sorted(())
    '()'

    >>> deep_sorted(set())
    'set()'

    >>> deep_sorted({"name": "John", "age": 30})
    '{"age": 30, "name": "John"}'

    >>> deep_sorted([3, 2, 1])
    '[1, 2, 3]'

    >>> deep_sorted((3, 2, 1))
    '(1, 2, 3)'

    >>> deep_sorted({3, 2, 1})
    '{1, 2, 3}'

    >>> deep_sorted({"b": 2, "a": 1})
    '{"a": 1, "b": 2}'

    >>> deep_sorted([{"c": 3, "b": 2, "a": 1}, {"d": 4}])
    '[{"a": 1, "b": 2, "c": 3}, {"d": 4}]'

    >>> deep_sorted(({"b": 2, "a": 1}, {"d": 4}))
    '({"a": 1, "b": 2}, {"d": 4})'

    >>> deep_sorted({"b": [3, 2, 1], "a": {"c": 3, "b": 2, "a": 1}})
    '{"a": {"a": 1, "b": 2, "c": 3}, "b": [1, 2, 3]}'
    """
    
    if isinstance(x, dict):
        sorted_dict = {str(key): deep_sorted(value) for key, value in sorted(x.items())}
        return "{" + ", ".join(f'"{key}": {value}' for key, value in sorted_dict.items()) + "}"
    elif isinstance(x, (list, tuple, set)):
        sorted_x = sorted(deep_sorted(item) for item in x)
        if isinstance(x, list):
            return "[" + ", ".join(sorted_x) + "]"
        elif isinstance(x, tuple):
            return "(" + ", ".join(sorted_x) + ")"
        elif isinstance(x, set):
            return "{" + ", ".join(sorted_x) + "}"
    else:
        return str(x)


if __name__ == '__main__':
    x=eval(input())
    print(deep_sorted((x)))
