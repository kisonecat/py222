all: sune.pdf half-turn.pdf

sune.tex: sune.py sune-header.tex sune-footer.tex
	python sune.py > sune.tex

sune.pdf: sune.tex
	pdflatex sune.tex
	pdflatex sune.tex

half-turn.tex: half-turn.py half-turn-header.tex half-turn-footer.tex
	python half-turn.py > half-turn.tex

half-turn.pdf: half-turn.tex
	pdflatex half-turn.tex
	pdflatex half-turn.tex
