#!/bin/sh
uvicorn main:app --host 0.0.0.0 --port 7777 --workers 1
