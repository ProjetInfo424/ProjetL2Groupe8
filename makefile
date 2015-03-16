all : prog prog2
prog :
prog2 : cercle.py triangle.py rectangle.py
	python -m py compile cercle.py
	python -m py compile triangle.py
	python -m py compile rectangle.py
