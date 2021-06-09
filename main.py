import csv
import plotly.figure_factory as ff
import statistics
import random
import pandas as pd
import plotly.graph_objects as go

df =  pd.read_csv("medium_data.csv")


def random_set(counter):
  dataset = []
  
  for i in range(0,counter):
    randonIndex = random.randint(0,len(data)-1)
    val = data[randonIndex]
    dataset.append(val)
    
  mean  =  statistics.mean(dataset)
  return mean 

def showfig(mean_list):
  df =  mean_list
  mean = statistics.mean(df)
  fig = ff.create_distplot([df],["reading_time"], show_hist=False)

  fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.4],mode = 'lines', name = 'mean'))
  fig.show()

def setup():
  mean_list =[]

  for i in range(0,100):
    setofmeans = random_set(10)
    mean_list.append(setofmeans)

  mean = statistics.mean(mean_list) 
  showfig(mean_list)

  print(mean,":mean sample")

def standardDev():
  mean_list =[]

  for i in range(0,100):
    setofmeans = random_set(10)
    mean_list.append(setofmeans)

  standarddev = statistics.stdev(mean_list) 
  

  print(standarddev,":standard dev")



setup()
standardDev()
