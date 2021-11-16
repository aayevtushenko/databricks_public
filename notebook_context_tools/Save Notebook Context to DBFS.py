# Databricks notebook source
# Setup a widget with parameter
# dbutils.widgets.dropdown("skip", "true", ['true', 'false'])

# Show the files in the current notebook's directory
import os.path
notebook_path = json.loads(dbutils.entry_point.getDbutils().notebook().getContext().toJson())['extraContext']['notebook_path']
notebook_path = os.path.dirname(notebook_path)
display(dbutils.fs.ls(notebook_path))

# COMMAND ----------

def save_variable_dbfs(var, file_name='saved_out.txt'):
  """
  dbutils.fs.put("/FileStore/my-stuff/my-file.txt", "Contents of my file")
  """
  
  import json
  import os.path
  
  context = json.loads(dbutils.entry_point.getDbutils().notebook().getContext().toJson())
  path = context['extraContext']['notebook_path']
  path = os.path.dirname(path)
  
  var = str(var)
  full_path = f'{path}/{file_name}'
  dbutils.fs.put(full_path, var, overwrite=True)
  
  print(f'file was saved to {full_path}')

# COMMAND ----------

def print_variable_from_dbfs(file_name):
  import os.path
  notebook_path = json.loads(dbutils.entry_point.getDbutils().notebook().getContext().toJson())['extraContext']['notebook_path']
  notebook_path = os.path.dirname(notebook_path)
  
  return dbutils.fs.head(f'{notebook_path}/{file_name}')

# COMMAND ----------

#edit this value
value = 10

if dbutils.widgets.get("skip") == 'false':
  print(f'setting the value to {value}')
  save_variable_dbfs(value, 'a_value_for_measuring_a_thing.txt')
else:
  print(f"the old value is: {print_variable_from_dbfs('a_value_for_measuring_a_thing.txt')}")

# COMMAND ----------


