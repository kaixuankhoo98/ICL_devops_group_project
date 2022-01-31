from flask import Flask
from literature_searcher import create_app
import os
port = int(os.environ.get("PORT", 5000))
app = create_app()
app.run(host='0.0.0.0',port=port)
