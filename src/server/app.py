from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
app = FastAPI()

class Query(BaseModel):
    bbox: list = None
    start_time: str = None
    horizon_hours: int = 6

@app.get('/health')
def health():
    return {'status':'ok'}

@app.post('/query/congestion')
def congestion(q: Query):
    import random
    tiles = []
    for i in range(6):
        tiles.append({'tile_id':f'demo_{i}','risk':round(random.random(),3),'expected_delay_mins':round(random.random()*30,2)})
    return {'status':'ok','tiles':tiles}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8080)
