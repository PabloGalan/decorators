def deco(func):
    def new_function():
        print('running inner()')

    return new_function


@deco
def original_function():
    print('running target()')


original_function()
print(original_function)
