import sys
import marko
from rich import inspect
from rich.console import Console

from abstract_generator import abstract_md_to_tex_generator



class md_to_latex_generator(abstract_md_to_tex_generator):

    def __init__(self, filename: str, tex_template = 'cheatsheet-template.tex'):
        super().__init__(filename=filename, tex_template=tex_template)



def main():
    if len(sys.argv) < 2:
        print(f"Syntax error.")
        print("Usage: gen_cs <md file> [tex_template]")
        sys.exit(1)
    
    if len(sys.argv) >= 3:
        generator=md_to_latex_generator(sys.argv[1], tex_template=sys.argv[2])
    else:
        generator=md_to_latex_generator(sys.argv[1])
    # generator.generate()

if __name__ == '__main__':
    main()