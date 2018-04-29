library("pracma")
setwd("/Volumes/Workgroup_Shares/Keller\ Lab/Binfs/Data/Thyroiditis-k9TRB-OH/Output/Matrixes/HdSum39/HD-nCount")
files <- list.files(path="wt-HD-0", pattern="*.csv", full.names=T, recursive=FALSE)
datalist <- list()
par(mfrow=c(4,4))
Cr1in=NULL
Cr1out=NULL
Cr2in=NULL
Cr2out=NULL
Cr3in=NULL
Cr3out=NULL
Cr4in=NULL
Cr4out1=NULL
Cr4out2=NULL
out=NULL
for (i in 1:length(files)) {
  test <- read.csv(files[i],header=T)
  Cr1<-diff(test$HD)
  if(all(Cr1==1)){
    test<-test[-1,]
    h<-(test$HD)
    r<-(test$RATIO)
    c<-(test$COUNT)
    df<-data.frame(h,r)
    colnames(df)<-c("HD","ratio")
    #plot(df,main=paste0(basename(files[i]),"-39"),type="l", col="navy")
    #grid()
    sampleID_Cr1_in<-basename((files[i]))
    sample.ID.in<-sub("^([^.]*).*", "\\1",sampleID_Cr1_in)
    Cr1df.in<-data.frame(sample.ID.in)
    Cr1df.in<-rbind(Cr1df.in)
    Cr1in=rbind(Cr1in,Cr1df.in)
    groupcount <- findpeaks(c)
    gpcount<-groupcount[,1]
    gpcount.sorted.re<-sort(gpcount,decreasing = F)
    lengpcount<-length(gpcount)
    count.max<-gpcount.sorted.re[lengpcount]
    if (count.max >= 500) {
      #plot(df,main=paste0(basename(files[i]),"-42"),type="l", col="navy")
      #grid()
      sampleID_Cr2_in<-basename((files[i]))
      sample.ID.in<-sub("^([^.]*).*", "\\1",sampleID_Cr2_in)
      Cr2df.in<-data.frame(sample.ID.in)
      Cr2df.in<-rbind(Cr2df.in)
      Cr2in=rbind(Cr2in,Cr2df.in)
      if (count.max >= 1000) {
        #plot(df,main=paste0(basename(files[i]),"-48"),type="l", col="navy")
        #grid()
        sampleID_Cr3_in<-basename((files[i]))
        sample.ID.in<-sub("^([^.]*).*", "\\1",sampleID_Cr3_in)
        Cr3df.in<-data.frame(sample.ID.in)
        Cr3df.in<-rbind(Cr3df.in)
        Cr3in=rbind(Cr3in,Cr3df.in)
        groupratio <- findpeaks(r)
        gpratio<-groupratio[,1]
        if (length(gpratio)==2 | length(gpratio)==3) {
          gpratio.sorted<-sort(gpratio,decreasing = T)
          gpratio.sorted.re<-sort(gpratio,decreasing = F)
          lengpratio<-length(gpratio)
          ratio.min<-gpratio.sorted[lengpratio]
          ratio.max<-gpratio.sorted.re[lengpratio]
          ratio.max<-rbind(ratio.max)
          #ratio.min<-rbind(ratio.min)
          gpcount.sorted<-sort(gpcount,decreasing = T)
          count.min<-gpcount.sorted[lengpcount]
          sampleID<-basename((files[i]))
          sample.ID<-sub("^([^.]*).*", "\\1",sampleID)
          count.ratio<-count.min/count.max
          dafr<-data.frame(sample.ID,ratio.min,ratio.max,count.min,count.max,count.ratio)
          p<-data.frame(dafr$sample.ID,dafr$ratio.min,dafr$ratio.max,dafr$count.min,dafr$count.max,dafr$count.ratio)
          colnames(p)<-c("sample.ID","ratio.min(nh1)","ratio.max(nh2)","count.min(h1)","count.max(h2)","h1/h2")
          #plot(df,main=paste0(basename(files[i]),"-39"),type="l", col="navy")
          #grid()
          Cr4in=rbind(Cr4in,p)
        } else if (length(gpratio)==1) {
          sampleID_Cr4_out<-basename((files[i]))
          sample.ID.out<-sub("^([^.]*).*", "\\1",sampleID_Cr4_out)
          Cr4_out<-paste0(sample.ID.out,"")
          Cr4df.out<-data.frame(Cr4_out)
          Cr4df.out<-rbind(Cr4df.out)
          Cr4out1=rbind(Cr4out1,Cr4df.out)
        } else if (length(gpratio) > 3) {
          sampleID_Cr4_out<-basename((files[i]))
          sample.ID.out<-sub("^([^.]*).*", "\\1",sampleID_Cr4_out)
          Cr4_out<-paste0(sample.ID.out,"")
          Cr4df.out<-data.frame(Cr4_out)
          Cr4df.out<-rbind(Cr4df.out)
          Cr4out2=rbind(Cr4out2,Cr4df.out)
        }
      }else if (count.max < 1000) {
        sampleID_Cr3_out<-basename((files[i]))
        sample.ID.out<-sub("^([^.]*).*", "\\1",sampleID_Cr3_out)
        Cr3_out<-paste0(sample.ID.out,"")
        Cr3df.out<-data.frame(Cr3_out)
        Cr3df.out<-rbind(Cr3df.out)
        Cr3out=rbind(Cr3out,Cr3df.out)
      }
    } else if (count.max < 500) {
      sampleID_Cr2_out<-basename((files[i]))
      sample.ID.out<-sub("^([^.]*).*", "\\1",sampleID_Cr2_out)
      Cr2_out<-paste0(sample.ID.out,"")
      Cr2df.out<-data.frame(Cr2_out)
      Cr2df.out<-rbind(Cr2df.out)
      Cr2out=rbind(Cr2out,Cr2df.out)
    }
  } else if (all(Cr1!=1) ) {
    sampleID_Cr1_out<-basename((files[i]))
    sample.ID.out<-sub("^([^.]*).*", "\\1",sampleID_Cr1_out)
    Cr1_out<-paste0(sample.ID.out,"")
    Cr1df.out<-data.frame(Cr1_out)
    Cr1df.out<-rbind(Cr1df.out)
    Cr1out=rbind(Cr1out,Cr1df.out)
  }
}
write.csv(Cr4in,paste0("../../Tables/Cdr3s39/","4CriterionsofTRB39.csv"))

