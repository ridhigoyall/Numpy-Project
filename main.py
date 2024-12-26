import numpy as np
from operationclass import IntArray

def productivity_of_company(order,
data_frame):
  '''
  num_product=0
  for element in data_frame[order]:
    num_product += element

  return num_product
  '''
  return np.sum(data_frame[order])  

def max_productivity(data_frame):
  i=0
  best_company=i+1
  num_of_products=0

  for i in range(len(data_frame)):
    result=productivity_of_company(i,data_frame)
    if result >num_of_products:
      num_of_products=result
      best_company=i+1

  print(f"The best company is the {best_company}. company with {num_of_products} products made")

def min_productivity(data_frame):
  i=0
  worst_company=i+1
  num_of_products=productivity_of_company(0,data_frame)

  for i in range(len(data_frame)):
    result=productivity_of_company(i,data_frame)
    if result < num_of_products:
      num_of_products=result
      worst_company=i+1

  print(f"The worst company is the {worst_company}. company with {num_of_products} products made")

def mean_product(data_frame):
  for i in range(len(data_frame)):
    avg=np.mean(data_frame[i])
    print(f'On average , one employee from {i + 1}.Company produced {avg} products')

  '''for element in np.nditer(data_frame):
    print(element)'''
  sum_products =0
  num_employee=0

  for row in data_frame:
    for employee in row:
      num_employee += 1

  for row in range(len(data_frame)):
    row_sum =np.sum(data_frame[row])
    sum_products += row_sum

  total_mean=sum_products / num_employee

  print(f'Total mean of entity monopoly is {total_mean} per employee')      
  

def file_handling():
  lines=[]

  with open('company.txt','r')as file:
    for line in file:
      value=line.strip().split(',')
      int_value=[int(val) for val in value]
      lines.append(int_value)

    data_frame=np.array([np.array(row) for row in lines],dtype='object')

    return data_frame 


def main():
  data_frame=file_handling()

  print(data_frame)

  first_brach=IntArray(data_frame[0])
  first_brach.display()
  first_brach.salary( )
  first_brach.show_data()

  max_productivity(data_frame)
  min_productivity(data_frame)
  mean_product(data_frame)

main()  