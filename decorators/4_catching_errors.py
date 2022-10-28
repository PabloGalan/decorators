def catches(catch):
    def decorate(f):
        def new_func(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            except catch as e:
                print(f'Caught an error: {repr(e)}')
                # raise e # Uncomment to propagate the error

        return new_func

    return decorate


@catches((RuntimeError, TypeError))
def main(arguments):
    if len(arguments) > 1:
        print(f'We have some arguments: {arguments}')
    else:
        raise RuntimeError('No arguments!!!')


if __name__ == '__main__':
    import sys

    main(sys.argv)
