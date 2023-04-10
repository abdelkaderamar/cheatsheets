import sys
from rich import inspect
from rich.console import Console
import argparse

from abstract_generator import abstract_md_to_tex_generator



class md_to_latex_generator(abstract_md_to_tex_generator):

    COLOURFUL_TEMPLATE_FILE = 'colourful-template.tex'
    COLOURFUL_UPDATE_TEMPLATE_FILE = 'colourful-updated-template.tex'

    def __init__(self, filename: str, tex_template = COLOURFUL_TEMPLATE_FILE):
        super().__init__(filename=filename, tex_template=tex_template)


def main():
    parser = argparse.ArgumentParser(description='Process a markdown file and generate tex file using Colourful (or Colourful Update) template')
    parser.add_argument('--colourful', '-c', default=True, action='store_true', dest='colourful', help='Use Colourful template (default)')
    parser.add_argument('--colourful-upd', '-u', action='store_true', dest='colourful_updated', help='Use Colourful Updated template ')
    parser.add_argument('markdown_file', help='Markdown file to parse')
    args = parser.parse_args()
    # print(args.colourful)
    # print(args.colourful_updated)
    # print(args.markdown_file)

    if args.colourful_updated:
        generator=md_to_latex_generator(args.markdown_file, md_to_latex_generator.COLOURFUL_UPDATE_TEMPLATE_FILE)
    elif args.colourful:
        generator=md_to_latex_generator(args.markdown_file)

if __name__ == '__main__':
    main()