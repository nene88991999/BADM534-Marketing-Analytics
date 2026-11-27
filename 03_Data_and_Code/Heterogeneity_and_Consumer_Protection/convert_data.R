args <- commandArgs(trailingOnly=TRUE)
root <- if(length(args)) args[1] else "03_Data_and_Code/Heterogeneity_and_Consumer_Protection"
load(file.path(root, "upstream", "cheese.rda"))
stopifnot(nrow(cheese)==5555, ncol(cheese)==4, nlevels(cheese$RETAILER)==88)
write.csv(cheese, file.path(root, "data", "cheese.csv"), row.names=FALSE)
