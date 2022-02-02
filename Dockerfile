FROM ashwinvis/latex-pandoc-python


COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN apt install -y lmodern





# Run the app
CMD python app.py


