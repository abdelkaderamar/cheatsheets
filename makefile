export TEXINPUTS=.:sty::

ALL_PDF = c++14_lang_cheatsheet.pdf \
	c++17_lang_cheatsheet.pdf \
	cmake_cheatsheet.pdf

all: $(ALL_PDF)

%.pdf: cpp/%.tex
	pdflatex -shell-escape $?

%.pdf: tools/%.tex
	pdflatex -shell-escape   $<

clean:
	rm -f *.aux *.log *.dvi

fullclean: clean
	rm -rf $(ALL_PDF) _minted-*
