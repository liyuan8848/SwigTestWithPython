all:
	swig -python swigdemo.i
	python setup.py build_ext --inplace
