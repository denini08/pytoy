import argparse

def test_ok_1():
    p = argparse.ArgumentParser(add_help=False)
    args = p.parse_args([])


def test_violation_1():
    # Define a parent parser
    parent_parser = argparse.ArgumentParser(add_help=False)
    parent_parser.add_argument('--parent_arg', help='Parent argument')

    # Define a child parser inheriting from the parent parser
    child_parser = argparse.ArgumentParser(parents=[parent_parser])
    child_parser.add_argument('--child_arg', help='Child argument')

    # Now, let's make a change to the parent parser after it's been used in the child parser
    parent_parser.add_argument('--new_parent_arg', help='New parent argument')

    # Parse arguments
    args = child_parser.parse_args([])

def test_ok_2():
    parent_parser = argparse.ArgumentParser(add_help=False)
    parent_parser.add_argument('--parent_arg', help='Parent argument')
    parent_parser.add_argument('--new_parent_arg', help='New parent argument')
    child_parser = argparse.ArgumentParser(parents=[parent_parser])
    child_parser.add_argument('--child_arg', help='Child argument')

    # Parse arguments
    args = child_parser.parse_args([])

def test_violation_2():
    parent_parser = argparse.ArgumentParser(add_help=False)
    child_parser = argparse.ArgumentParser(parents=[parent_parser])
    parent_parser.add_argument('--parent_arg', help='Parent argument')

    # Parse arguments
    args = child_parser.parse_args([])

def test_ok_3():
    parent_parser = argparse.ArgumentParser(add_help=False)
    parent_parser.add_argument('--parent_arg', help='Parent argument')
    child_parser = argparse.ArgumentParser(parents=[parent_parser])
    child_parser.add_argument('--child_arg', help='Child argument')

    # Parse arguments
    args = child_parser.parse_args([])

def test_violation_3():
    parent_parser = argparse.ArgumentParser(add_help=False)
    child_parser = argparse.ArgumentParser(parents=[parent_parser], add_help=False)
    # another child parser
    another_child_parser = argparse.ArgumentParser(parents=[child_parser])

    parent_parser.add_argument('--parent_arg', help='Parent argument')
    # Parse arguments
    args = another_child_parser.parse_args([])