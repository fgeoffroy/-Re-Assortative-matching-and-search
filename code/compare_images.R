## This R script allows to compare two sets of pdf files: the output of the reproduction python script main.py
## and the figures of the article (See the README file for more information).
## This script was written by Dirk Eddelbuettel, the first reviewer of the article.

## Dirk Eddelbuettel, Feb 2021, released under GPL 2 or later


library(pdftools)		# on CRAN: to convert pdf to png
library(visualTest)		# at github.com/MangoTheCat/visualTest: to assess figure similarity


dirA <- paste(getwd(), "/../article/figures", sep="")     # soft link into the article figures
dirB <- paste(getwd(), "/figures", sep="")                # soft link into the output of reproduction

pdffiles <- list.files(dirA, pattern="*.pdf")

for (f in pdffiles) {
  ## construct filenames in original and reproduced directories
  fileA <- file.path(dirA, f)
  fileB <- file.path(dirB, f)
  stopifnot(`no reproduced file found` = file.exists(fileB))
  
  ## create two tempfiles and produces png variants
  tfA <- tempfile(fileext=".png")
  tfB <- tempfile(fileext=".png")
  pdf_convert(fileA, format="png", filenames=tfA, verbose=FALSE)
  pdf_convert(fileB, format="png", filenames=tfB, verbose=FALSE)
  
  ## compare these png variants based on their "image fingerprint" (a 64-bit hexadecimal string generated via a Discrete Cosine Transform)
  stopifnot(`disparity found` = isSimilar(tfA, tfB, exact=TRUE))
  
  ## report progress
  cat("Processed and compared", f, "without issues.\n")
}

cat("Done. No issues.\n")
