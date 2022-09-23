from re import template


class abstract_generator:

    LINE_NUMBER_PER_COLUMN=82

    def __init__(self, line_per_col=LINE_NUMBER_PER_COLUMN):
        self.line_per_col=line_per_col
        self.line_count=0
        self.column_count=1
        with open('template_cheatsheet.tex', 'r') as template_file:
            self.template_content=template_file.read()
        self.start=self.template_content.index('%%BEGIN_ITEM%%')
        print(self.template_content.index('%%END_ITEM%%'))
        self.end=self.template_content.index('%%END_ITEM%%') + len('%%END_ITEM%%')
        self.templat_item=self.template_content[self.start:self.end]
        self.generated_content=self.template_content[0:self.start]

    
    def do_generate(self, items, main_title, latex_file):
        # Add items & columnbreaks
        for item in items:
            if self.column_count == 4:
                self.column_count = 1
                self.line_count = 0
                self.generated_content += "\\end{multicols}\n"
                self.generated_content += "\\newpage\n"
                self.generated_content += "\\vspace*{1cm}\n"
                self.generated_content += "\\begin{multicols}{3}"
            print(self.generated_content)
            self.generated_content+=self.generate_item(item, self.templat_item)

        self.console.print(f"current column_count = {self.column_count}")
        for i in range(self.column_count,3):
            self.console.print("Adding a column break")
            self.generated_content += self.add_columnbreak()
            self.generated_content += '\\,'
        
        self.generated_content+=self.template_content[self.end:]
        #self.console.print(self.generated_content)
        
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
        item_lines_count=item_latex.count('\n')
        print(f'line count={item_lines_count}')
        if (self.line_count + item_lines_count > self.line_per_col):
            self.line_count = 0
            self.column_count = self.column_count + 1
            if self.column_count != 4:
                item_latex = item_latex + self.add_columnbreak()
        else:
            self.line_count += item_lines_count
        return item_latex


    def add_columnbreak(self):
        columnbreak = '\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n'
        columnbreak += '\\columnbreak\n'
        columnbreak += '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n'
        return columnbreak