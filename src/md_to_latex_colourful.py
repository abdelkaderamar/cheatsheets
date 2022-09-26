import sys
from rich import inspect
from rich.console import Console
import argparse

from abstract_generator import abstract_generator



class md_to_latex_generator(abstract_generator):

    COLOURFUL_TEMPLATE_FILE = 'colourful-template.tex'
    COLOURFUL_UPDATE_TEMPLATE_FILE = 'colourful-updated-template.tex'

    def __init__(self, filename: str, tex_template = COLOURFUL_TEMPLATE_FILE):
        super().__init__(tex_template=tex_template)
        self.console = Console()

        with open(filename, 'r') as f:
            md_content=f.readlines()

        data={}
        data['items']=[]
        for i in range(len(md_content)):
            l=md_content[i]
            if l.startswith('main_title: '):
                main_title=l[len('main_title: '):]
            if l.startswith('#---------') and i < len(md_content)-1:
                print('parsing an item')
                i+=1
                current_title=''
                current_content=''
                l=md_content[i]
                while not l.startswith('#---------') and i < len(md_content)-1:
                    if l.strip() == '#- columnbreak':
                        item = 'columnbreak'
                        data['items'].append(item)
                        break
                    elif l.strip() == '#- newpage':
                        item = 'newpage'
                        data['items'].append(item)
                        break

                    if l.startswith('title:'):
                        current_title=l[len('title:'):].strip().rstrip()
                    elif l.strip() != '' :
                        current_content+=l
                    i+=1
                    l=md_content[i]
                    
                print('Title = [%s]' % current_title)
                print('Content = [%s]' % current_content)
                if current_content is not None and current_content != '':
                    item={}
                    item['title']=current_title
                    item['content']=current_content
                    data['items'].append({'item': item})
        items=data['items']
        print(f"{len(items)} items")
        latex_file=self.get_outputfilename(filename=filename, tex_template=tex_template, extension='.md')
        self.do_generate(data['items'], main_title, latex_file)



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