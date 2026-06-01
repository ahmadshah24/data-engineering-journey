import argparse

parser = argparse.ArgumentParser(description='simple calculator')


parser.add_argument('num1', type=float, help='First number')
parser.add_argument('num2', type=float, help='Second number')
parser.add_argument('operation', type=str, choices=['add', 'subtract', 'multiply', 'divide'], help='Operation to perform')

args = parser.parse_args()

if args.operation == 'add':
    result = args.num1 + args.num2 
elif args.operation == 'subtract':
    result = args.num1 - args.num2
elif args.operation == 'multiply':
    result = args.num1 * args.num2
elif args.operation == 'divide':
    if args.num2 == 0:
        result = 'Error: Division by zero'
    else:
        result = args.num1 / args.num2

    
print(f'The result of {args.operation}ing {args.num1} and {args.num2} is: {result}')

