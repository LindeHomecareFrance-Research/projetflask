from app import create_app
from config import DevConfiguration


app = create_app()
if __name__ == "__main__":
    
    app.run(debug=True)