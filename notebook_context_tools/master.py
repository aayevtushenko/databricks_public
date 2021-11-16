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



def print_variable_from_dbfs(file_name):
  import os.path
  notebook_path = json.loads(dbutils.entry_point.getDbutils().notebook().getContext().toJson())['extraContext']['notebook_path']
  notebook_path = os.path.dirname(notebook_path)
  
  return dbutils.fs.head(f'{notebook_path}/{file_name}')