.PHONY: tokens sync check lint test beamer beamer-light
tokens:
	python3 tokens/build.py
sync: tokens
	cp tokens/tokens.json design-system/tokens.json
check:
	python3 tokens/build.py --check
	diff -q tokens/tokens.json design-system/tokens.json
	python3 tokens/check.py
	python3 scripts/check_design_system.py
lint:
	ruff check .
test:
	python3 -m pytest -q tests
beamer: tokens
	cd latex/beamer && TEXINPUTS=.:../../tokens/dist//: xelatex -interaction=nonstopmode -halt-on-error example.tex && TEXINPUTS=.:../../tokens/dist//: xelatex -interaction=nonstopmode -halt-on-error example.tex
beamer-light: tokens
	cd latex/beamer && sed 's/\\usetheme{kentigern}/\\usetheme[light]{kentigern}/' example.tex > example-light.tex && TEXINPUTS=.:../../tokens/dist//: xelatex -interaction=nonstopmode -halt-on-error example-light.tex && TEXINPUTS=.:../../tokens/dist//: xelatex -interaction=nonstopmode -halt-on-error example-light.tex
