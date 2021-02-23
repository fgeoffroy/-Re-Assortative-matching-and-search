# [Re] Assortative matching and search


## Replication of Shimer & Smith (2000) and Smith (2006)

This project attempts to replicate results from Shimer & Smith (2000) and Smith (2006) in Python. The full references to the original articles are:

> Shimer, R., and Smith, L. (2000). Assortative matching and search. Econometrica, 68(2), 343–369. http://doi.org/10.1111/1468-0262.00112

> Smith, L. (2006). The Marriage Model with Search Frictions. J. Political Econ., 114(6), 1124–1144. https://doi.org/10.1086/510440

The reproduction was partially successful and has been submitted to [ReScience C](https://rescience.github.io/).




## Running the code: quick guide

Running the replication Python script only requires two common packages (Numpy and Matplotlib). The results presented in the articles can therefore probably be replicated with most versions of Python.

To run the replication script, in a terminal, and in the `code/` subfolder, type

```bash
$ python main.py
```

This creates all figures in the article, which should take ca. 30sec. The figures are saved in the `code/figures/` subfolder.




## Running the code: in detail

### Available files

**main.py** : this script creates all figures.
Usage: python main.py (ca. 30sec)

**run_TU.py** : is called by `main.py` to create figures with *transferable utility*. If run independently, a simulation with is be computed with parameters defined at the bottom of the script.
Usage: python run_TU.py (ca. 2sec)

**run_NTU.py** : is called by `main.py` to create figures with *non-transferable utility*. If run independently, a simulation with is be computed with parameters defined at the bottom of the script.
Usage: python run_NTU.py (ca. 2sec)




### Versioning

This implementation is written in Python 3 and requires Numpy and Matplotlib.

The packages required to run this implementation and the versions on which they were tested on are:

- python=3.7.4
- numpy=1.17.2
- matplotlib=3.1.1

For tractability, we provide a conda environment containing these package versions used for generating the figures in the article.

To create a new environment called RescienceGeoffroy with all necessary packages, in a terminal, and in the `code/` subfolder, type (this requires Anaconda, does not work with Miniconda)

```bash
$ conda update conda
$ conda env create -f environment.yml
```

Activate the environment with

```bash
$ conda activate RescienceGeoffroy
```

And run the replication script with

```bash
$ python main.py
```

The environment.yml file tries to load exactly these versions, but later versions will likely also work.

The source code was tested on Ubuntu 18.04.




## Article reproduction

The article uses the [ReScience C](https://rescience.github.io/) journal template. All elements are in the `article/` subfolder. All the figures in the article can also be found in the `article/figures/` subfolder. Instructions to reproduce the article are provided in the subfolder [README](article/README.md).




## Comparing the output of reproduction with the article figures
[@eddelbuettel](https://github.com/eddelbuettel), who reviewed this article, provided an R script for performing a visual comparison between the output of the Python script `main.py` and the article figures. This script makes use of the [visualTest](https://github.com/MangoTheCat/visualTest) package.

The output of the `main.py` script is saved in the `code/figures/` subfolder, and the article figures are located in the `article/figures/` subfolder. The R script checks if the images in the two folders have the same "image fingerprint", i.e. a 64-bit hexadecimal string generated via a Discrete Cosine Transform (see [visualTest](https://github.com/MangoTheCat/visualTest) for more information).

To run the visual comparison, in a terminal, and in the `code/` subfolder, type

```bash
$ Rscript compare_images.R
```

The packages required to run this implementation and the versions on which they were tested on are:

- R=4.0.3
- pdftools=2.3.1
- visualTest=1.0.0
