all : Lire triangle

Lire : Lire.java
	javac -classpath . Lire.java
	java Lire
	


triangle : figures.py 
	
	python3 -m py_compile figures.py
	python3 figures.py
	


clean:
	
	rm -f Lire.class
	rm -f figures.pyc

