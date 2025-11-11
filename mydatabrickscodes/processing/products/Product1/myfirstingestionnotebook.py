# Databricks notebook source
#yui
calendar = spark.read.option("header", "true").csv("/Volumes/myfirstcatalog/myfirstproduct/myfirstvolume/calendar.csv")

calendar.write.format("delta").saveAsTable("myfirstcatalog.myfirstproduct.calendar",mode="overwrite")

# COMMAND ----------

data_dictionary = spark.read.option("header", "true").csv("/Volumes/myfirstcatalog/myfirstproduct/myfirstvolume/data_dictionary.csv")

data_dictionary.write.format("delta").saveAsTable("myfirstcatalog.myfirstproduct.data_dictionary",mode="overwrite")

# COMMAND ----------

inventory = spark.read.option("header", "true").csv("/Volumes/myfirstcatalog/myfirstproduct/myfirstvolume/inventory.csv")

inventory.write.format("delta").saveAsTable("myfirstcatalog.myfirstproduct.inventory",mode="overwrite")

# COMMAND ----------

products = spark.read.option("header", "true").csv("/Volumes/myfirstcatalog/myfirstproduct/myfirstvolume/products.csv")

products.write.format("delta").saveAsTable("myfirstcatalog.myfirstproduct.products",mode="overwrite")

# COMMAND ----------

sales = spark.read.option("header", "true").csv("/Volumes/myfirstcatalog/myfirstproduct/myfirstvolume/sales.csv")

sales.write.format("delta").saveAsTable("myfirstcatalog.myfirstproduct.sales",mode="overwrite")

# COMMAND ----------

stores = spark.read.option("header", "true").csv("/Volumes/myfirstcatalog/myfirstproduct/myfirstvolume/stores.csv")

stores.write.format("delta").saveAsTable("myfirstcatalog.myfirstproduct.stores",mode="overwrite")

# COMMAND ----------

print("Print me !!!")

# COMMAND ----------

stores.write.format("delta").saveAsTable("myfirstcatalog.myfirstproduct.stores",mode="overwrite")

# COMMAND ----------

selct ahahahak 

# COMMAND ----------

def very_bad_function(a, b, c, d, e, f):
    pass  # too many parameters

# COMMAND ----------

x = 10
print(y) 

# COMMAND ----------

def hello1():
    print("Hello world")

def hello2():
    print("Hello world")

# COMMAND ----------

DB_PASSWORD = "supersecret123"

# COMMAND ----------

def do_nothing():
    pass

# COMMAND ----------

# def old_function():
#     print("this is old")

# COMMAND ----------

Test this

# COMMAND ----------

pip install

# COMMAND ----------

a<>b
