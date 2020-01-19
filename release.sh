
python3 -m pip install --user --upgrade setuptools wheel

python3 setup.py clean --all sdist bdist_wheel
python3 setup.py sdist bdist_wheel

python3 -m pip install --user --upgrade twine

python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*

python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps barbarum-common