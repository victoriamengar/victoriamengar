# Developing Data Products - Week 4 Course Project
## Victoria Menendez Garcia

This shiny app enables the user to change the cutpoint of a Kaplan-meier analysis of TCPTP pathway level in 25 Hodgkin's Lymphoma patients.
As it is a dataset with numeric values, it must be dichotomized in high and low following a cut point.
This cut point is chosen by the user with a slicer.

The .Rmd and the .html files are a presentation with all the instructions and an example of the output.

## Instructions:

1. Open RStudio.
2. Set the folder which contains ui.R and server.R files as your working directory (you can do it with the setwd("filepath") function).
3. Make sure that shiny is loaded with library(shiny). If you don't have this package,install it with install.packages("shiny").
4. Execute in the console with the function runApp(). It is recommended to be opened in the browser.
