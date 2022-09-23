import sys
import marko
from rich import inspect
from rich.console import Console

from abstract_generator import abstract_generator



class md_to_latex_generator(abstract_generator):

    def __init__(self, filename: str, line_per_col: int):
        super().__init__(line_per_col=line_per_col)
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
        latex_file=filename[0:filename.lower().rfind('.md')] + '-md.tex'
        self.do_generate(data['items'], main_title, latex_file)



def main():
    if len(sys.argv) < 2:
        print(f"Syntax error.")
        print("Usage: gen_cs <yaml file>")
        sys.exit(1)
    if len(sys.argv) >= 3:
        line_per_col=int(sys.argv[2])
    else:
        line_per_col=abstract_generator.LINE_NUMBER_PER_COLUMN
    generator=md_to_latex_generator(sys.argv[1], line_per_col)
    # generator.generate()

if __name__ == '__main__':
    main()