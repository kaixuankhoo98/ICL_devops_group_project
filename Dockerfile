FROM pandoc/core

RUN echo "Got Pandocs"

FROM python:3


COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN (curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)



# un the app
CMD python app.py


