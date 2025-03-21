import fastapi 
import uvicorn
from routers import mockroutes


app = fastapi.FastAPI()
app.include_router(mockroutes.router) 

if __name__ == "main":
    uvicorn.run(app, host="127.0.0.1", port=8000)







