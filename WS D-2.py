#!/usr/bin/env python
# coding: utf-8

# In[1]:


def calculate_carbon_footprint(energy_consumption,emission_factor):
    return energy_consumption * emission_factor
energy_consumption = 1000
emission_factor = 0.475
footprint =calculate_carbon_footprint(energy_consumption,emission_factor)
print("carbon Footprint:",footprint,"kg CO2")


# In[2]:


cities=[
    {"name":"city A","carbon_footprint":500},
    {"name":"city B","carbon_footprint":350},
    {"name":"city C","carbon_footprint":600},
    {"name":"city D","carbon_footprint":200}
]
sustainability_threshold=400
sustainable_cities=list(filter(lambda city: city["carbon_footprint"]< sustainability_threshold,cities))
print("Sustainable cities:")
for city in sustainable_cities:
    print("-",city["name"])


# In[5]:


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age


# In[6]:


person=Person("Bharat",10000)


# In[7]:


person.name


# In[9]:


class Car:
    wheels=4
    def __init__(self,make,year):
        self.make=make
        self.year=year
        
    def start_engine(self):
        print("Engine started")
    
    @classmethod # class Method
    def get_wheels(cls):
        return cls.wheels
    
    @staticmethod
    def is_motor_vehicle():
        return True


# In[11]:


car= Car("Toyota",2022)
print(car.make)
print(car.year)


# In[12]:


car.start_engine()


# In[15]:


car.get_wheels()


# In[16]:


car.is_motor_vehicle()


# In[24]:


class Person:
    def __init__(self,name,age):
        self._name=name
        self._age=age
        
    def get_name(self):
        return self._name
        


# In[25]:


person = Person("MIT",15)


# In[26]:


person._name


# In[27]:


person._age


# In[29]:


person=Person("raghu",21)
person.get_name()


# In[54]:


# inheritence
class vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        
    def display_info(self):
        return f"{self.brand},{self.model}"
    
class Car(vehicle):
    def __init__(self,brand,model, doors):
        super().__init__(brand,model)
        self.doors=doors
        
    def display_info(self):
        return f"{self.brand} {self.model}{self.doors}"
        
    


# In[55]:


my_car=Car('Maruthi','suzuki',7)


# In[56]:


my_car.display_info()


# In[57]:


class Animal:
    def make_sound(self):
        print("Animal make sound!")
        
class Dog(Animal):
    def make_sound(self):
        print("bark!!")


# In[58]:


dog1=Dog()


# In[59]:


dog1.make_sound()


# In[61]:


class Examples:
    def sum(self, *args):
        return sum(args)


# In[63]:


e=Examples()


# In[64]:


e.sum(1,2,4,9)


# In[68]:


import pandas as pd
a=pd.Series([0,1,2,3,4])


# In[70]:


a


# In[71]:


z=pd.DataFrame({'S':[5,6,7],'B':[4,5,6]})


# In[72]:


z


# In[73]:


import numpy as np
thd_array=np.array([[3,4,5],[7,8,9],[10,11,12]])
print(thd_array)


# In[1]:


import pandas as pd
renewable_sources=['solar','wind','hydro','geothermal','tidal']
rs=pd.Series(renewable_sources)
rs


# In[6]:


#dataFrame
data={
    'Project':['solar Farm','wind turbine','hydro plant','geothermal station','tidal plant'],
    'Technology':['solar','Wind','hydro','Geothermal','Tidal'],
    'Capacity[%]':[150,300,200,600,700],
    'Cost (million)':[200,400,600,900,250],
    'Location':['North America','Europe','Asia','china','Russia'],
    'YOC':[2023,2022,2021,2010,2009]
                  
}


# In[7]:


df=pd.DataFrame(data)
df


# In[9]:


df['Technology']


# In[19]:


high_capacity=df['Capacity[%]']>150
print(f"high capacity projects are: \n {df[high_capacity]}")


# In[20]:


high_cost=df['Cost (million)']>200
print(f"high cost projects are: \n {df[high_cost]}")


# In[28]:


df['cost per MW']=df['Cost (million)']/df['Capacity[%]']
df


# In[29]:


total_cost=df['Cost (million)'].sum()
total_capacity=df['Capacity[%]'].sum()
print(f'Total Cost of Projects:{total_cost} million') 
print(f'Total Capacity of Projects:{total_capacity} %') 


# In[32]:


grouped_data =df.groupby('Technology')['Capacity[%]'].sum()
grouped_data                                       


# In[33]:


import numpy as np
a=np.array([1,2])
a


# In[35]:


a.ndim


# In[39]:


b=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
b


# In[41]:


z=np.random.rand(2,3)
z


# In[43]:


z=np.random.rand(4,4)
z


# In[ ]:




