from os import path


class Day:
    def getPaths(self, f):
        self.input_path = path.join(path.dirname(f), "inputs", "input")
        self.test_input_path = path.join(path.dirname(f), "inputs", "input.test")

    def __init__(self, test=False) -> None:

        try:
            if test:
                self.input_file_content = open(self.test_input_path).read()
            else:
                self.input_file_content = open(self.input_path).read()
        except:
            print(f"Cannot read input file for {self.name} - {self.description}")
