# Sphinx Template

Materials to help you go from zero to full documentation as quickly as possible.

This repository contains the following directories:

* docs/
  * The Sphinx source of the documentation.
* my_package/
  * An example Python package.  We'll grab docstrings from this package and generate documentation for it.
* examples/
  * Visual examples that illustrate the use of `my_package`.  These examples will be turned into a gallery.

Of particular interest may be the `docs/source/conf.py` file, which is used to
configure Sphinx.

The documentation may be built by doing:

```
cd docs
make html
```
