# web_api - A web api to mqtt gateway

## Instructions
1) Copy the file .sample_env to a new file named .env and update the information inside to meet your broaker configuration.
2) Run `pip install -r requirements.txt`
3) Run `bash run_gunicorn` or `bash run_flask_server` for debugging.
4) The api will be available on `http://your_ip:8050`.
5) Type `http://your_ip:8050/your_message` to see `your_message` being transmitted to the broker.

**Tested on Python3**
