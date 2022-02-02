FROM python:3


COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN curl -sSL https://get.haskellstack.org/ 
RUN wget https://hackage.haskell.org/package/pandoc-1.17.0.3/pandoc-1.17.0.3.tar.gz
RUN tar xvzf pandoc-1.17.0.3.tar.gz

RUN curl --proto '=https' --tlsv1.2 -sSf https://get-ghcup.haskell.org
RUN cabal update
RUN cabal --version

RUN cabal install pandoc




# un the app
CMD python app.py


