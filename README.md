# FlaskApi
FastAPI Notes API

A simple FastAPI server that accepts POST requests with subject and description fields, and returns a 201 Created response.

Features

Built using FastAPI (high-performance Python web framework).

Provides a /notes/ endpoint to create notes.

Returns 201 Created status with the submitted note.

Includes interactive API docs via Swagger (/docs) and ReDoc (/redoc).

Installation & Setup

2. Create Virtual Environment
python -m venv venv


# On Windows
venv\Scripts\activate

3. Install Dependencies
pip install fastapi uvicorn

Running the Server

Start the FastAPI server:

uvicorn main:app --reload


Server will run at:

http://127.0.0.1:8000

API Usage
Endpoint: POST /notes/

Request Body (JSON):

{
  "subject": "Meeting Notes",
  "description": "Discussed project roadmap and deadlines"
}




API Documentation

Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

