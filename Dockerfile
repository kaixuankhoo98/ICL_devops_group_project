FROM pandoc/core

RUN echo "Got Pandocs"

FROM python:3


COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN brew install pandoc



# un the app
CMD python app.py


