import os
import sys

## add module to syspath
# get the current working directory
cwd = os.path.abspath(os.path.dirname(__file__))
# isolate the last folder (the folder we are currently in)
project = os.path.basename(cwd)
# remove the last folder from the cwd
new_path = cwd.strip(project)
# create a new path pointing to where our Flask object is defined
full_path = os.path.join(new_path,'flaskr')
print("cwd: ", cwd)
print("project: ", project)
print("new path: ", new_path)
print("full path: ", full_path)
try:
    from flaskr import app
except ImportError:
    sys.path.append(full_path)
    from flaskr import app


def before_feature(context, feature):
    context.client = app.test_client()
