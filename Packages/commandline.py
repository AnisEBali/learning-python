from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument('--output', '-o', required = True, help="The destination file for the output of this program")
# Adds a new Command Prompt argument
# Required = the file cannot run without it or it will error
parser.add_argument('--text', '-t', required = True, help="The text to write to the file")

args = parser.parse_args()
# Stores whatever input into args

with open(args.output, 'w') as newText:
    newText.write(args.text+'\n')

print(f'Wrote "{args.text}" to file "{args.output}"')
# Example:
# C:\Users\--\Documents\GitHub\learning-python\Packages>commandline.py -o somefile.txt -t "some text to write to thefile"