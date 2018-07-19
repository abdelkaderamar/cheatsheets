all: c++14_cheatsheet.pdf c++17_cheatsheet.pdf \
	cmake_cheatsheet.pdf

%.pdf: cpp/%.tex
	pdflatex -shell-escape $?

%.pdf: tools/%.tex
	pdflatex -shell-escape   $<

clean:
