from re import template
from rich.console import Console


class abstract_generator:

    LINE_NUMBER_PER_COLUMN=82

    def __init__(self, tex_template='cheatsheet-template.tex'):
        self.console = Console()
        self.console.print("Initialializing the generator")

        with open('templates/' + tex_template, 'r') as template_file:
            self.template_content=template_file.read()
        self.start=self.template_content.index('%%BEGIN_ITEM%%')
        print(self.template_content.index('%%END_ITEM%%'))
        self.end=self.template_content.index('%%END_ITEM%%') + len('%%END_ITEM%%')
        self.templat_item=self.template_content[self.start:self.end]
        self.generated_content=self.template_content[0:self.start]

    
    def do_generate(self, items, lang, main_title, latex_filename):
        # Add items & columnbreaks
        for item in items:
            self.console.print(item)
            if item == 'columnbreak':
                self.generated_content += self.add_columnbreak()
                continue
            if item == 'newpage':
                self.generated_content += self.add_newpage()
                continue
            if item == 'end-section':
                self.generated_content += self.add_endsection()
                continue
            if isinstance(item, dict):
                if 'item' in item:
                    self.generated_content+=self.generate_item(item, self.templat_item)
                elif 'section' in item:
                    section_name=item['section']
                    self.generated_content+=self.add_section(section_name)
                elif 'subsection' in item:
                    subsection_name=item['subsection']
                    self.generated_content+=self.add_subsection(subsection_name)

        self.generated_content+=self.template_content[self.end:]
        
        title=main_title
        self.generated_content=self.generated_content.replace('%%MAIN_TITLE%%', title)
        self.generated_content=self.generated_content.replace('%%LANG%%', lang)
        with open(latex_filename, 'w') as gen_file:
            gen_file.write(self.generated_content)

    def generate_item(self, item, template_item: str):
        title=item['item']['title']
        content=item['item']['content']
        item_latex=template_item.replace('%%BEGIN_ITEM%%','').replace('%%END_ITEM%%', '')
        item_latex = item_latex.replace('%%ITEM_TITLE%%', title)
        item_latex = item_latex.replace('%%ITEM_CONTENT%%', content)
        return item_latex

    def get_outputfilename(self, filename: str, tex_template: str, extension: str) -> str:
        suffix='-' + tex_template.replace('-template', '')
        latex_filename=filename[0:filename.lower().rfind(extension)] + suffix
        idx=latex_filename.rfind('/')
        if idx != -1:
            latex_filename=latex_filename[0:idx] + "/tex" + latex_filename[idx:]
        else:
            latex_filename='tex/' + latex_filename
        return latex_filename

    def add_columnbreak(self):
        columnbreak = '\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n'
        columnbreak += '\\columnbreak\n'
        columnbreak += '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n'
        return columnbreak
    
    def add_newpage(self):
        newpage = "\\end{multicols}\n"
        newpage += "\\newpage\n"
        newpage += "\\vspace*{1cm}\n"
        newpage += "\\begin{multicols}{3}"
        return newpage
    
    def add_endsection(self):
        return "\n\n\\end{textbox}\n\n"

    def add_section(self, section_name:str) -> str:
        return "\n{\centering\\section{" + section_name + "}}\n"

    def add_subsection(self, section_name:str) -> str:
        return "\n\\subsection{" + section_name + "}\n"

class abstract_md_to_tex_generator(abstract_generator):

    def __init__(self, filename: str, tex_template = 'cheatsheet-template.tex'):
        super().__init__(tex_template=tex_template)
        self.console = Console()

        with open(filename, 'r') as f:
            md_content=f.readlines()

        data={}
        data['items']=[]
        lang=''
        for i in range(len(md_content)):
            l=md_content[i]
            if l.lower().startswith('main_title: '):
                main_title=l[len('main_title: '):]
            if l.lower().startswith('lang:'):
                lang=l[len('lang:'):].strip()
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
                    elif l.lower().startswith('#- section:'):
                        section_name=l[len('#- section:'):].strip().rstrip()
                        item={'section': section_name}
                        data['items'].append(item)
                        break
                    elif l.lower().startswith('#- subsection:'):
                        subsection_name=l[len('#- subsection:'):].strip().rstrip()
                        item={'subsection': subsection_name}
                        data['items'].append(item)
                        break
                    elif l.lower().startswith('#- begin-section:'):
                        section_name=l[len('#- begin-section:'):].strip().rstrip()
                        item={'begin-section': section_name}
                        data['items'].append(item)
                        break
                    elif l.lower().startswith('#- end-section'):
                        item = 'end-section'
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
        latex_filename=self.get_outputfilename(filename=filename, tex_template=tex_template, extension='.md')
        self.do_generate(data['items'], lang=lang, main_title=main_title, latex_filename=latex_filename)
