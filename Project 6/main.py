import sys
import Parser
from pathlib import Path


def main():
    Path("output/").mkdir(parents=True, exist_ok=True)
    Path("input/").mkdir(parents=True, exist_ok=True)

    input = Path('input') / sys.argv[1]
    if input.exists():
        parser = Parser.Parser(input)
        parser.run()
        return

    print('No file found')


if __name__ == '__main__':
    main()
