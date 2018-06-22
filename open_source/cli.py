# -*- coding: utf-8 -*-

"""Console script for open_source."""

# Standard library imports
import sys

# Third party imports
import click

# Local imports
import open_source.open_source as open_source


@click.group()
@click.version_option()
def main(args=None):
    """Console script for open_source."""
    click.echo("Welcome to Open Source toy project!")
    return 0


@click.command()
@click.argument('word', type=click.STRING)
def check_palindrome(word):
    print(open_source.check_palindrome(word))


@click.command()
@click.argument('lower', type=click.INT)
@click.argument('upper', type=click.INT)
def random_int(lower, upper):
    print(open_source.random_int(lower, upper))


@click.command()
@click.argument('word', type=click.STRING, required=False)
def random_letter(word):
    print(open_source.random_letter(word))


main.add_command(check_palindrome)
main.add_command(random_int)
main.add_command(random_letter)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
