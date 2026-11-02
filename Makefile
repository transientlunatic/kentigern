.PHONY: tokens sync check beamer
tokens:
	python3 tokens/build.py
sync: tokens
	cp tokens/tokens.json design-system/tokens.json
check:
	python3 tokens/build.py --check
	diff -q tokens/tokens.json design-system/tokens.json
beamer: tokens
	cd latex/beamer && TEXINPUTS=.:../../tokens/dist//: xelatex -interaction=nonstopmode example.tex && TEXINPUTS=.:../../tokens/dist//: xelatex -interaction=nonstopmode example.tex
