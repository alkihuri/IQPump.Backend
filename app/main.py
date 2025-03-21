import fastapi 
from routers import mockroutes

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

app = fastapi.FastAPI()
app.include_router(mockroutes.router) 

import uvicorn





