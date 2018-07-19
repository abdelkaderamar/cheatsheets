all: c++14_lang_cheatsheet.pdf c++17_lang_cheatsheet.pdf \
	cmake_cheatsheet.pdf

%.pdf: cpp/%.tex
	pdflatex -shell-escape $?

%.pdf: tools/%.tex
	pdflatex -shell-escape   $<

clean:
	rm -f *.aux *.log

