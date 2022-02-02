FROM ashwinvis/latex-pandoc-python


COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN apt install pandoc texlive -y





# Run the app
CMD python app.py


