FROM python:3


COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN sudo apt-get install pandoc


# Run the app
CMD python app.py
