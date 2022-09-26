from re import template
from rich.console import Console


class abstract_generator:

    LINE_NUMBER_PER_COLUMN=82

    def __init__(self, tex_template='template_cheatsheet.tex'):
        self.console = Console()
        self.console.print("Initialializing the generator")

        with open(tex_template, 'r') as template_file:
            self.template_content=template_file.read()
        self.start=self.template_content.index('%%BEGIN_ITEM%%')
        print(self.template_content.index('%%END_ITEM%%'))
        self.end=self.template_content.index('%%END_ITEM%%') + len('%%END_ITEM%%')
        self.templat_item=self.template_content[self.start:self.end]
        self.generated_content=self.template_content[0:self.start]

    
    def do_generate(self, items, main_title, latex_file):
        # Add items & columnbreaks
        for item in items:
            self.console.print(item)
            if item == 'columnbreak':
                self.generated_content += self.add_columnbreak()
                continue
            if item == 'newpage':
                self.generated_content += self.add_newpage()
                continue
            self.generated_content+=self.generate_item(item, self.templat_item)
        self.generated_content+=self.template_content[self.end:]
        
        title=main_title
        self.generated_content=self.generated_content.replace('%%MAIN_TITLE%%', title)
        with open(latex_file, 'w') as gen_file:
            gen_file.write(self.generated_content)

    def generate_item(self, item, template_item: str):
        title=item['item']['title']
        content=item['item']['content']
        item_latex=template_item.replace('%%BEGIN_ITEM%%','').replace('%%END_ITEM%%', '')
        item_latex = item_latex.replace('%%ITEM_TITLE%%', title)
        item_latex = item_latex.replace('%%ITEM_CONTENT%%', content)
        return item_latex


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