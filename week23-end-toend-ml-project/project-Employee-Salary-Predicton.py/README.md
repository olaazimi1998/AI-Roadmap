# Employee Salary Prediction

## Problem

This project predicts employee salary based on employee characteristics.

## Features

- Age
- Experience
- Education
- Department

## Target

Salary

## Machine Learning

Random Forest Regressor

## Pipeline

Data
→ Preprocessing
→ Feature Engineering
→ Model
→ Evaluation
→ API

## API

FastAPI is used to serve the trained model.

## Run

```bash
uvicorn api.main:app --reload