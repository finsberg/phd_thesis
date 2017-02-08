
filename=article


default:
	pdflatex -shell-escape -interaction=nonstopmode ${filename}
	bibtex chapters/introduction
	bibtex chapters/paper1/article
	pdflatex ${filename}
	pdflatex ${filename}

read:
	evince ${filename}.pdf &

clean:
	rm -f *.aux *.blg *.out *.bbl *.log *~
