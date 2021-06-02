# sort-me-out

# Installation

1. Install necessary packages in your python environment (a virtual env is recommended)
   `pip install -r requirements.txt`

# Execution
### Local Setup
`
uvicorn main:app --reload
`

### DETA deployment

1. Login to DETA 
   ```
   deta login
   ```
   You will be prompted to authenticate via the browser.


2. Deta relies on having `main.py` and `requirements.tx`t in the same directory from where app is being deployed
   ```cd sort-me-out
   ```
3. For the very first time create instance and deploy the code
```angular2html
deta new
```
4. And any susequent changes can be deployed by running

```angular2html
deta deploy
```