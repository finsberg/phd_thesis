
filename=main


default:
	pdflatex ${filename}
	bibtex chapters/introduction
	bibtex chapters/paper1/article
	pdflatex ${filename}
	pdflatex ${filename}

read:
	evince ${filename}.pdf &

clean:
	clean-files-latex
