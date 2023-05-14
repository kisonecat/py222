all: sune.pdf

sune.tex: sune.py sune-header.tex sune-footer.tex
	python sune.py > sune.tex

sune.pdf: sune.tex
	pdflatex sune.tex
	pdflatex sune.tex
