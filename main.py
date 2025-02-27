from fastapi import FastAPI


app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'Hello World'}


@app.get('/healthz')
async def root():
    return {'result': 'healthy'}
