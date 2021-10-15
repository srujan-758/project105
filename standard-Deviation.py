import csv
import math

with open("data.csv",newline='') as f:
 reader=csv.reader(f)
 file_data=list(reader)

data=file_data[0]  

def mean(data):
 with open('data.csv', newline='') as f:
  reader= csv.reader(f) 
  file_data=list(reader)

  new_data=[] 
  for i in range(len(file_data)): 
   n_num= file_data[i][1] 
   new_data.append(float(n_num))

  n=len(new_data)   
  total=0
  for x in new_data:
   total=total+x 

  mean=total/n
  return(mean)  
  
  
 
#squaring & getting the values 
squared_list=[]
for number in data: 
  a= int(number)-mean(data)
  a=a**2
  squared_list.append(a)

# getting the sum
sum=0
for i in squared_list:
  sum=sum+i   

#dividing the sum by total values
result=sum/len(data)-1

#getting the daviation by taking square root
std_deviation=math.sqrt(result)


print("The standard deviation is:-" +str(std_deviation))

