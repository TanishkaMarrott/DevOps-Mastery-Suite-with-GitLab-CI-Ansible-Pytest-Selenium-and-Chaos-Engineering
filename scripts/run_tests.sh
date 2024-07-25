#!/bin/bash

echo \"Running unit tests...\"
pytest tests/unit/

echo \"Running Selenium tests...\"
python selenium/test_login.py
