import os, json
os.makedirs('data/cache', exist_ok=True)
for i in range(10):
    rec = {
        'tile_id': f'demo_{i}',
        'start_time': '2025-11-20T08:00:00Z',
        'end_time': '2025-11-20T08:10:00Z',
        'sat_image': 'samples/sample_sat_tile.png',
        'traffic_timeseries': {'sensor_ids':['s1','s2'],'speeds':[10+i,12+i]},
        'social_text': [{'id':f't{i}','text':'traffic jam','lang':'en'}],
        'economic':{'retail_index':0.9,'unemployment':0.05},
        'weather':{'temp':18,'precip':0.0},
        'label':{'congestion_risk_next_6h':0.5}
    }
    with open(f'data/cache/rec_{i}.json','w') as f:
        json.dump(rec,f)
print('Wrote sample records to data/cache')
