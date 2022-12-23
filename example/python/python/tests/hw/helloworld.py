""" Hello World """


def hello(greeting, place):
    """ Flexible greeting """
    return greeting + ' ' + place


def main():
    """ Return the known string """
    print(hello('Hello', 'World'))


# Main for cli
if __name__ == '__main__':
    main()
