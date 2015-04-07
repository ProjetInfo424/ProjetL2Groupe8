all : Lire triangle

Lire : Lire.java
	javac -classpath . Lire.java
	java Lire
	


triangle : triangle.py 
	
	python3 -m py_compile triangle.py
	python3 triangle.py
	


clean:
	
	rm -f Lire.class
	rm -f triangle.pyc

