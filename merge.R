install.packages("plyr")
library(plyr)
install.packages("dplyr")
library(dplyr)
show.way<-par(mfrow=c(2,2))
setwd("/Volumes/Workgroup_Shares/Keller\ Lab/Binfs/Data/Thyroiditis-k9TRB-OH/Output/Matrixes/HdSum48/HD-nCount")
filenames <- list.files(path="wt-HD-0", pattern="*.csv", full.names=T, recursive=FALSE)
import.list <- llply(filenames, read.csv)
dataall <- Reduce(function(x, y) merge(x, y, all=T, 
                                       by=c("HD")), import.list, accumulate=F)
dataall[is.na(dataall)]<-0
cols1 <- names(dataall) == 'COUNT.x'
cols2 <- names(dataall) == 'COUNT.y'
cols3 <- names(dataall) == 'RATIO.x'
cols4 <- names(dataall) == 'RATIO.y'
names(dataall)[cols1] <- paste0('COUNT')
names(dataall)[cols2] <- paste0('COUNT')
names(dataall)[cols3] <- paste0('RATIO')
names(dataall)[cols4] <- paste0('RATIO')
dataall
colsc <- names(dataall) == 'COUNT'
names(dataall)[colsc] <- paste0('COUNT', seq_along(colsc))
colsr <- names(dataall) == 'RATIO'
names(dataall)[colsr] <- paste0('RATIO', seq_along(colsr))
head(dataall)
HD_ratio <- dataall %>% select(-starts_with("COUNT"))
HD_count <- dataall %>% select(-starts_with("RATIO"))
write.csv(HD_count,paste0("all-csv/","countall.csv"))
write.csv(HD_ratio,paste0("all-csv/","ratioall.csv"))
HD_ratio
HD_count
sum(HD_ratio)
HD_ratio$sum<- rowSums(HD_ratio[,2:59])
HD_count$sum<- rowSums(HD_count[,2:59])
write.csv(HD_count,paste0("all-csv/","count_all_sum.csv"))
write.csv(HD_ratio,paste0("all-csv/","ratio_all_sum.csv"))
hdrs<-data.frame(HD_ratio$HD,HD_ratio$sum)
colnames(hdrs)<-c("HD","ratio_sum")
ylim<-range(c(0:6))
hdrs
plot(hdrs,ylim=ylim,type="l", col="red",xlab="HD",
     ylab="Accumulated HD ratio",main="Distribution of HD VS SUM of ratio for Cdr3s-48")
