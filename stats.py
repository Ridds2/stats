import pandas as pd
df=pd.read_csv('C:\\Users\\Dell\\Downloads\\Autism-G1.csv')
import statistics
b=df.Coloured_inside_object
a=[]

for i in range(len(b)):
    a.append(b[i])

print(a)
def describe(a):
    print(len(df))
    print((min(a),max(a)))
    mean=statistics.mean(a)
    print(mean)
    print(statistics.variance(a))
    print(statistics.median(a))
    mo=statistics.mode(a)               #238
    sd=statistics.variance(a)**0.5      #standard deviation
    skewness=(mean-mo)/sd
    print(skewness)
    sum=0
    for i in range(len(a)):
        sum=sum+(a[i]-mean)**4
    kurtosis=(sum/len(a))/sd**4
    print(kurtosis)


describe(a)     #(b)

