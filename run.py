# is going to import from __init__ as we are importing from a package (herd is a package)
from herd import app


if __name__ == '__main__':
    app.run(debug=True)