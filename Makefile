
INPUT = resume.yaml templates/* configs/*
OUTPUT = output/resume-ehrat.pdf output/resume-ehrat.txt output/resume-ehrat.json
TEX = output/resume-ehrat.tex

all: $(OUTPUT)

#output/resume-ehrat.pdf:


$(OUTPUT): $(INPUT)
	python render-templates.py

deploy: 
	scp $(OUTPUT) braden@origin.behrat.net:/ebs/www/bradenehrat.com/html/
