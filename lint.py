import sys
from pylint import lint

THRESHOLD = 9

if len(sys.argv) < 2:
    raise ArgumentError("Module to evaluate needs to be the first argument")

run = lint.Run([sys.argv[1:]], do_exit=False)
score = run.linter.stats['global_note'] # Yes this is a terrible name for the score

if score < THRESHOLD:
    sys.exit(1)