library(readr)
X281 <- read_csv("C:/Users/apb38/Desktop/DR/enernoc-comm/enernoc-comm/enernoc-comm/csv/281.csv")
View(X281)
attach(X281)

#clean data a little
df <-data.frame(X281)
df$Date <- as.Date(dttm_utc)
df$Time <- format(dttm_utc,"%H:%M:%S")
data <-data.frame(df$Date,df$Time,value)
data1 <- data.frame(df$Time,value)

load.libraries <- function (needed.packs, quietly = T) 
{
  installed.packs <- installed.packages()
  for (pack in needed.packs) {
    if (!pack %in% installed.packs) {
      install.packages(pack, repos = "http://cran.cnr.Berkeley.edu")
    }
    if (quietly) {
      suppressPackageStartupMessages(library(pack, character.only = T, 
                                             quietly = quietly))
    }
    else {
      library(pack, character.only = T)
    }
  }
}
load.libraries(c('data.table','lubridate','stringr')
dailyload <- DT[,.(Value.mean = mean(value)),by=V2]
dailyload

plot(dailyload$Value.mean, axes=F, ylim=c(0,20), typ='l', ann=F)
par(tcl= -0.2)
axis(1, at=seq(1, 288, by=10), lwd=1, lwd.ticks=1)
par(tcl= -0.5)
axis(2)
title(main="Average daily load of Grocery Store 281", xlab = "interval", ylab="kWh")
linear.model <- lm(dailyload$Value.mean ~ row(dailyload)[,1])


###### original
plot(d$index, axes=F, ylim=c(0,150), typ='l', ann=F)
par(tcl= -0.2)
axis(1, at=seq(1, 445, by=12), labels=F, lwd=1, lwd.ticks=1)
par(tcl= -0.5)
axis(1, at=seq(1 + 12*2, 450, by=60), labels=seq(1975,2010,5), lwd=0, lwd.ticks=2)
par(tcl= -0.5)
axis(2)
abline(v=(12*(seq(2,32,by=5)))+1, col="lightgray", lty="dotted")
abline(h=(seq(0,150,25)), col="lightgray", lty="dotted")
title(main="Nominal Major Currencies Dollar Index", sub="Mar 1973 = 100.00", ylab="US$ vs major currencies")
linear.model = lm(d$index ~ row(d)[,1])
abline(linear.model, col="blue")


#####################
attempt 1
data<-data.table(data)
d3<-data[,df.Date:=NULL]
d4<-d3[,.(time=unique(df.Time),energy=ave(value,na.rm=TRUE)),by=df.Time]
#idk why its is not condensing down the df.Time to the "unique(df.Time)", I am guessing this has to do with it being a time value.


######### attempt 2
setkey(data,df.Time)
data["00:00:00"]

