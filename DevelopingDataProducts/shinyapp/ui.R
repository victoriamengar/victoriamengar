
library(shiny)
shinyUI(pageWithSidebar(
    headerPanel("Kaplan-Meier analysis of TCPTP pathway in Hodgkin's Lymphoma patients"),
    sidebarPanel(
        h4("Choose a percentage of patients to consider HIGH. The rest are considered LOW"),
        sliderInput("cut", "cut", value = 50, min = 25, max = 75, step = 1)
    ),
    mainPanel(
        h3("Plot of Kaplan-Meier with the selected cut"),
        plotOutput("KMplot")
    )
))