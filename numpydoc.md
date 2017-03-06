# Using numpydoc with sphinx

- `pip install numpydoc`
- Add `numpydoc` to Sphinx extensions list in `conf.py`
- Add an `automodule` entry for the module you wish to document (see
  [sphinx_template](https://raw.githubusercontent.com/choldgraf/sphinx_template/master/docs/source/API.rst)).
- Run `make html` and watch the magic happen.

## Hints

1. Add `-W` to the Sphinx options in the Sphinx Makefile to make sure you
   catch all warnings.
1. Define `__all__` for all modules to ensure that functions get
   picked up by Sphinx automodule.

## References

- [HOWTO Document NumPy](https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt)
- [Example NumPy docstring](https://github.com/numpy/numpy/blob/master/doc/example.py#L38)
- Gallery of examples:
  - [NumPy Reference](https://docs.scipy.org/doc/numpy/reference/)
  - [SciPy Reference](https://docs.scipy.org/doc/scipy/reference/)
  - [scikit-learn](http://scikit-learn.org/stable/modules/classes.html)
  - [scikit-image](http://scikit-image.org/docs/stable/api/api.html)
  - [Pandas](http://pandas.pydata.org/pandas-docs/stable/api.html)

