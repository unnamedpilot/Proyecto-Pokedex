#!/bin/bash

# Execute the Python script
python /app/module/id_container_provider.py

exec flask run --host=0.0.0.0 --port=80

