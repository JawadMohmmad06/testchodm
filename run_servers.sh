#!/bin/bash

uvicorn twoprojecttest:app --host 0.0.0.0 --port 8000 --reload &
uvicorn twoprojecttest2:app --host 0.0.0.0 --port 8001 --reload
