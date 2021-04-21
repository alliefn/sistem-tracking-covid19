pip install mysql-connector-python
pip install pytest
mysql -u root -p < trackingCovid.sql
pytest -v
py src/main.py
