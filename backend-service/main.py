from uvicorn import run
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    run("app.server:app", host="127.0.0.1", port=8004, reload=True)

    