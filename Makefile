all:
	swig -python swigdemo.i
	python setup.py build_ext --inplace

clean:
	rm _*
	rm -rf build
	rm swigdemo_wrap.c
	
