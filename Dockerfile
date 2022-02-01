FROM plantiga/pandoc-base


COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN sudo apt-get install pandoc


# Run the app
CMD python app.py
