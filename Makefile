
filename=main


default:
	pdflatex ${filename}
	bibtex chapters/introduction
	bibtex chapters/paper1/article
	bibtex chapters/paper2/main
	bibtex chapters/paper3/main
	bibtex chapters/paper4/main
	pdflatex ${filename}
	pdflatex ${filename}

read:
	evince ${filename}.pdf &

clean:
	clean-files-latex
