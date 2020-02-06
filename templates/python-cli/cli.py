"""Remind lazy programmers to document their code.
Usage:
    remind.py [-hv] [--eternal | --n_reminders=<n>] <name>
Arguments:
    name    Somebody who needs to be reminded to document their code
Options:
    -h --help            show this message and exit.
    --version            show version information and exit.
    -v --verbose         show unnecessary extra information.
    --eternal            give reminders forever.
    --n_reminders=<n>    number of reminders to give. [default: 5]
"""
from docopt import docopt


def main():
    # docopt saves arguments and options as key:value pairs in a dictionary
    args = docopt(__doc__, version='0.1')
    verbose = args['--verbose']
    name = args['<name>']
    if verbose:
        print('You are about to be reminded to document your code')
    # do the thing
    if args['--eternal']:
        if verbose:
            print('This may take a while...')
        while True:
            print(f'Document your code, {name}!')
    else:
        for _ in range(int(args['--n_reminders'])):
            print(f'Document your code, {name}')
    if verbose:
        print('You have been reminded to document your code')


if __name__ == '__main__':
    main()
