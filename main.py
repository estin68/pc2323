import fastapi
import uvicorn

print("Hello, fastapi")
api = fastapi.FastAPI()


@api.get('/')  # decorator
def endpoint():  # endpoint function
    return {"msg": "Hello everyone",
            "list of ports": [9000, 8000, 6789],
            }


uvicorn.run(api, port=1987)
