FROM python:3


COPY . .
RUN pip install --no-cache-dir -r requirements.txt

# Run the app
CMD python app.py