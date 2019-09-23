#!/bin/python
cp -r docs/document document
rm -r docs
sphinx-apidoc -F -o ./docs ./roomai
mv document docs/document

cd docs
cat conf.py > tmp
echo "import os" > conf.py
echo "import sys" >> conf.py
echo "sys.path.insert(0, os.path.abspath('..'))" >> conf.py
cat tmp >> conf.py
rm tmp 
make html

cd ..
