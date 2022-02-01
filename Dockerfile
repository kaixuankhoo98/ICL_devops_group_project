FROM python:3


COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
RUN brew install pandoc

# Run the app
CMD python app.py
