"""
Author: Ryan
Description: REST API for Item randomizer
"""

from api import app

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
