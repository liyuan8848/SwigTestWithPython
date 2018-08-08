#!/usr/bin/env  python

from distutils.core import setup, Extension

swigdemo_module = Extension('_swigdemo',
                           sources=['swigdemo_wrap.c', 'uart_packet.c'],
                           )

setup (name = 'swigdemo',
       version = '0.1',
       author      = "SWIG Docs",
       description = """Simple swig example from docs""",
       ext_modules = [swigdemo_module],
       py_modules = ["swigdemo"],
       )
