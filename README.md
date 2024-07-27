# Orders Analysis

## Description
This project reads order data from a CSV file and computes various metrics such as total revenue per month, total revenue per product, and total revenue per customer. It also identifies the top 10 customers by revenue.

## Requirements
- Docker
- Python 3.12

## Setup

### Build Docker Images

```bash
docker build -t orders-analysis -f Dockerfile .
docker build -t orders-analysis-test -f Dockerfile.test .