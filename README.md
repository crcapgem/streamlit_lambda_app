## Transformer health :blue[knowledge base, and search]

This repo contains the code for our genAI hackathon submission for Transformer health :blue[knowledge base, and search]

Execute the following commands to activate env:

```bash
python3 -m venv appenv
source appenv/bin/activate
pip install -r requirements.txt
```
or in windows:

```bash
python3 -m appenv
.\appenv\Scripts\Activate.ps1 
pip install -r requirements.txt
 ```

To run the application locally, execute the following command:

```bash
streamlit run app.py \
  --browser.serverAddress=localhost \
  --server.enableCORS=false \
  --server.enableXsrfProtection=false \
  --server.port 8080
 ```


### How to run
To test the app locally run,

```bash
streamlit run app.py
```
Open [http://localhost:8501](http://localhost:8501) with your browser to see the result.
