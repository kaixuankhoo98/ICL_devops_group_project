FROM plantiga/pandoc-base


COPY . .
RUN pip install --no-cache-dir -r requirements.txt






# Run the app
CMD python app.py


