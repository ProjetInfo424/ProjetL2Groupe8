all : Lire triangle analyse

analyse: Figure.java
	 javac -classpath . Figure.java
	 java Figure


Lire : analyse
	
	
figure : figures.py 
	
	python3 -m py_compile figures.py
	python3 figures.py
	


clean:
	rm -f Figure.class
	rm -f Lire.class
	rm -f figures.pyc

