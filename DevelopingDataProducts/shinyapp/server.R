
library(shiny)
suppressPackageStartupMessages(library(survival))				
#Kaplan-Meier analysis needs these two packages.
suppressPackageStartupMessages(library(survminer))
suppressPackageStartupMessages(library(magrittr))                               
#To do piping
suppressPackageStartupMessages(library(ggplot2))                        
#To do plots in general
data <- data.frame(patient = c("HL10",
                               "HL12",
                               "HL13",
                               "HL14",
                               "HL15",
                               "HL17",
                               "HL19",
                               "HL2",
                               "HL20",
                               "HL21",
                               "HL22",
                               "HL23",
                               "HL24",
                               "HL25",
                               "HL28",
                               "HL29",
                               "HL3",
                               "HL4",
                               "HL40",
                               "HL41",
                               "HL47",
                               "HL5",
                               "HL6",
                               "HL8",
                               "HL9"
), TCPTP = c(1.516,
                                            1.7221,
                                            1.6037,
                                            0.8147,
                                            2.1933,
                                            1.6638,
                                            1.637,
                                            0.9114,
                                            1.6598,
                                            1.5298,
                                            1.3616,
                                            1.781,
                                            1.7064,
                                            1.7424,
                                            2.3032,
                                            1.5731,
                                            0.5897,
                                            0.7895,
                                            1.0795,
                                            1.209,
                                            0.9352,
                                            1.422,
                                            1.1651,
                                            0.841,
                                            1.196
), FFS = c(140.93,
           5.10,
           5.73,
           34.40,
           10.10,
           4.07,
           37.33,
           49.23,
           5.03,
           6.13,
           4.07,
           6.07,
           18.20,
           37.33,
           16.83,
           16.27,
           126.23,
           59.30,
           106.70,
           82.90,
           72.67,
           10.00,
           51.93,
           6.10,
           7.10
), fustat = c(0,
              1,
              1,
              1,
              1,
              1,
              1,
              1,
              1,
              1,
              1,
              1,
              1,
              0,
              1,
              1,
              0,
              0,
              0,
              0,
              1,
              1,
              0,
              1,
              1
))

dataprep <- function(data, cut) {
    cut <- as.numeric(cut)
    numHIGH <- round(cut*0.01*nrow(data))			        
    #Number of HIGH value patients that it should be with this cut point.
    
    columnorder <- sort(data[,2], decreasing = TRUE)            
    #From higher to lower, we order the column values after converting it to a vector with the pull() function.
    
    cuteach <- columnorder[numHIGH]					#Se coge el valor de cutoff. Los menores seran LOW.
    
    survdich <- data    
    #Copy of the dataset.
    
    newcolumn <- ifelse(survdich[,2] >= cuteach, "HIGH","LOW")
    
    #Testing if there are more than one point per level.
    
    freqmat <- table(newcolumn)				        
    #Frequency matrix
    
    No0 <- length(freqmat[freqmat != 0])		                
    #Elements not 0
    No1 <- length(freqmat[freqmat == 1])				
    #Elements not 1
    Elem <- No0 - No1					        
    #Elements that are not 0 nor 1
    if (Elem <= 1) {							
        #If there are less than 2 elements different from 0 or 1
        plot <- NULL
    }
    
    survdich[,2] <- newcolumn
    
    #Ensuring that both fustat and ffs are numeric and unlisted:
    
    FUSTAT <- as.numeric(unlist(survdich[,4]))
    
    FFS <- as.numeric(unlist(survdich[,3]))
    
    survobj <- Surv(time = FFS, event = FUSTAT, type = "right")
    #It uses FFS and FUSTAT data.
    
    #KM plotting:
    levels <- unlist(survdich[,2])
    fit1 <- surv_fit(survobj ~ levels, data = survdich)
    npatients = nrow(survdich)
    pvalueKM <- surv_pvalue(fit1)[2]
    return(fit1)
}

shinyServer(
    function(input, output) {
        output$KMplot <- renderPlot({
            fit <- dataprep(data, input$cut)
            print(ggsurvplot(fit,
                                                     pval = TRUE,
                                                     pval.method=TRUE,
                                                     risk.table = "abs_pct",
                                                     fontsize = 4,
                                                     font.tickslab = c(12),
                                                     legend.title = "",
                                                     font.title = c(16, "bold", "darkblue"),
                                                     font.subtitle = c(13, "plain", "darkblue"),
                                                     font.legend = c(11, "plain"),
                                                     tables.y.text = FALSE,
                                                     xlab = "FFS in months",
                                                     title = "Dichotomization and Kaplan-Meier analysis",
                                                     ))
        })
    }
)