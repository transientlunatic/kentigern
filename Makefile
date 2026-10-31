.PHONY: tokens sync check
tokens:
	python3 tokens/build.py
sync: tokens
	cp tokens/tokens.json design-system/tokens.json
check:
	python3 tokens/build.py --check
	diff -q tokens/tokens.json design-system/tokens.json
