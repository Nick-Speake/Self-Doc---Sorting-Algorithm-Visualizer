from app import create_app

app = create_app() # instantiates Flask object
    
if __name__ == "__main__":
    app.run(debug=True) # debug=True enables live reloads for dynamic web application
    
