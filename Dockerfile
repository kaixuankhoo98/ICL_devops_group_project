FROM python:3

WORKDIR ./

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY * /
# Run the app
CMD flask run --host=0.0.0.0 --port=$PORT

