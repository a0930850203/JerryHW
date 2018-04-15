
# coding: utf-8

# practice1

# In[51]:


class work():
    def look(self):
        print("hello")


# In[52]:


self_name = work()
self_name.look()


# In[26]:


class Car():
    def saying(self):
        print("I'm a Car")


# In[27]:


class Book(Car):
    pass


# In[28]:


x_car = Car()
Y_book = Book()


# In[29]:


x_car.saying()


# In[30]:


class Book(Car):
    def saying(self):
        print("I'm a book")
    def need_a_push(self):
        print("may i help you?")


# In[31]:


x_car = Car()
y_book = Book()
y_book.saying()


# In[32]:


y_book.need_a_push()


# exercise1

# In[21]:


class Restaurant():
    def look(self):
        print("義大利麵,好吃的")


# In[40]:


class IceCreamStand(Restaurant):
    def look(self):
        print("白醬",a)


# In[41]:


describe_restaurant = Restaurant()
show_flavors = IceCreamStand()
describe_restaurant.look()
show_flavors.look()


# In[35]:


a = ["紅醬","白醬","青醬"]


# In[39]:


a

