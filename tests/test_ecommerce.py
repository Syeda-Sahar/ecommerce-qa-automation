import time
import pytest


def login_api(username, password):
    return {
        "status": 200,
        "user": username
    }


def payment_api(amount):

    return {
        "status": 500,
        "message": "Internal Server Error"
    }


def database_connection():

    raise TimeoutError(
        "Database took too long to respond"
    )


def inventory_service():

    return {
        "items": 24
    }


def order_service():

    return {
        "order_created": True
    }


# PASS
def test_login():

    response = login_api(
        "sahar",
        "abc123"
    )

    assert response["status"] == 200


# FAIL → Product Defect
def test_payment_gateway():

    response = payment_api(100)

    assert response["status"] == 200,\
        "Payment Gateway returned 500"


# FAIL → Environment
def test_database_connection():

    database_connection()


# PASS
def test_inventory_count():

    response = inventory_service()

    assert response["items"] > 0


# FAIL → Product Assertion
def test_order_creation():

    response = order_service()

    assert response["order_created"] is False,\
        "Expected order creation=False but got True"