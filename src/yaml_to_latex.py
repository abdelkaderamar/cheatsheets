import sys
import yaml

from rich.console import Console

from abstract_generator import abstract_generator

class yaml_to_latex_generator(abstract_generator):

    def __init__(self, filename):
        super().__init__()
        self.console = Console()
        self.console.print("Initialializing the generator")
        with open(filename, 'r') as yaml_file:
            self.yaml_content=yaml.safe_load(yaml_file)
        self.console.print(self.yaml_content)
        # self.console.print(self.yaml_content['items'][0]['item']['content'])
        # self.console.print(self.yaml_content['items'][1]['item']['content'])

    def generate(self, filename):
        main_title=self.yaml_content['title']
        items=self.yaml_content['items']
        # latex_file=filename[0:filename.lower().rfind('.yaml')] + '-yaml.tex'
        latex_file=self.get_outputfilename(filename=filename, tex_template='yaml.tex', extension='.yaml')
        self.do_generate(main_title=main_title, items=items, lang='', latex_filename=latex_file)


        
def main():
    if len(sys.argv) < 2:
        print(f"Syntax error.")
        print("Usage: gen_cs <yaml file>")
        sys.exit(1)
    if len(sys.argv) >= 3:
        line_per_col=int(sys.argv[2])
    else:
        line_per_col=abstract_generator.LINE_NUMBER_PER_COLUMN
    print(line_per_col)
    generator=yaml_to_latex_generator(sys.argv[1])
    generator.generate(sys.argv[1])

if __name__ == '__main__':
    main()
