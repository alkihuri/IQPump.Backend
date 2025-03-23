import fastapi 
import uvicorn
from services import matching
from routers import mockroutes, auth

app = fastapi.FastAPI()
app.include_router(mockroutes.router) 
app.include_router(auth.router)
app.include_router(matching.router)

if __name__ == "main":
    uvicorn.run(app, host="127.0.0.1", port=8000)







