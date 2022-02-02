FROM python:3


COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN (curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)
Run export brew=/home/linuxbrew/.linuxbrew/bin
RUN brew install pandoc



# un the app
CMD python app.py


