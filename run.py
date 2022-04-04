# is going to import from __init__ as we are importing from a package (herd is a package)
from herd import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)