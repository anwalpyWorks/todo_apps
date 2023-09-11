from fastapi import FastAPI
import routes
import sys
app= FastAPI()

sys.path.append("routes/create.py")
sys.path.append("routes/delete.py")
sys.path.append("routes/update.py")
sys.path.append("routes/gel_all_value.py")
sys.path.append("routes/search.py")
