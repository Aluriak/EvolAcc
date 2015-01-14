VIEWER=evince
SOURCE=project_definition

all: source clean

clean:
	- rm *.aux *.log 

source:
	pdflatex $(SOURCE).tex && pdflatex $(SOURCE).tex
	$(VIEWER) $(SOURCE).pdf


