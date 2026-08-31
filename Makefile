install:
	python -m pip install -r requirements.txt

test:
	pytest -q

run:
	streamlit run app.py
