import uvicorn

from twoprojecttest import app as app1
from twoprojecttest2 import app as app2

if __name__ == "__main__":
    uvicorn.run(app1, host="0.0.0.0", port=8000)
    uvicorn.run(app2, host="0.0.0.0", port=8001)
