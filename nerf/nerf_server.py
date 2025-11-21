from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
class RenderRequest(BaseModel):
    pose: list
    w: int = 800
    h: int = 600
@app.post('/render')
def render(req: RenderRequest):
    # Implement call to instant-ngp or nerfstudio here
    return {'status':'queued','note':'render not implemented in stub'}
