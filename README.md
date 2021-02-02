# [Re] Assortative matching and search



## Running the code: quick guide

To create a new environment with all necessary packages called RescienceGeoffroy, in a terminal and in the *code* directory type (this requires Anaconda, does not work with Miniconda)

```bash
$ conda update conda
$ conda env create -f environment.yml
```

Activate the environment with

```bash
$ conda activate RescienceGeoffroy
```

Create all figures in the article, which should take ca. 30sec. The figures are saved in article/figures for easy comparison with the figures in the text.

```bash
$ python main.py
```




## Running the code: in detail

This implementation is written in Python 3 and requires Numpy and Matplotlib.

The packages required to run this implementation and the versions on which they were tested on are:

- python=3.7.4
- numpy=1.17.2
- matplotlib=3.1.1

The environment.yml file tries to load exactly these versions, but later versions will likely also work.

The source code was tested on Ubuntu 18.04.



#### Available files

**main.py** : this script creates all figures.
Usage: python main.py (ca. 30sec)

**run_TU.py** : is called by main.py to create figures with *transferable utility*. If run independently, a simulation with is be computed with parameters defined at the bottom of the script.
Usage: python run_TU.py (ca. 2sec)

**run_NTU.py** : is called by main.py to create figures with *non-transferable utility*. If run independently, a simulation with is be computed with parameters defined at the bottom of the script.
Usage: python run_NTU.py (ca. 2sec)
