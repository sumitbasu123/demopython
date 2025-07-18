#!/usr/bin/env python3
"""
Test script for the Calculator Web API
Tests all API endpoints to ensure functionality.
"""

import requests
import json
import time
import sys

BASE_URL = "http://localhost:5000"
SESSION_ID = "test_session"

def test_api_endpoint(endpoint, method="GET", data=None):
    """Test an API endpoint and return the response."""
    url = f"{BASE_URL}{endpoint}"
    
    try:
        if method == "GET":
            response = requests.get(url, timeout=5)
        elif method == "POST":
            response = requests.post(url, json=data, timeout=5)
        elif method == "DELETE":
            response = requests.delete(url, json=data, timeout=5)
        
        return response
    except requests.exceptions.RequestException as e:
        print(f"❌ Error connecting to {url}: {e}")
        return None

def test_expression_evaluation():
    """Test expression evaluation endpoint."""
    print("\n🧮 Testing Expression Evaluation:")
    
    test_cases = [
        "2 + 3",
        "10 * 5",
        "sqrt(16)",
        "sin(pi/2)",
        "2^3"
    ]
    
    for expression in test_cases:
        data = {
            "expression": expression,
            "session_id": SESSION_ID
        }
        
        response = test_api_endpoint("/api/evaluate", "POST", data)
        if response and response.status_code == 200:
            result = response.json()
            if result.get("success"):
                print(f"  ✅ {expression} = {result['result']}")
            else:
                print(f"  ❌ {expression} - Error: {result.get('error')}")
        else:
            print(f"  ❌ {expression} - Request failed")

def test_memory_operations():
    """Test memory operations endpoint."""
    print("\n💾 Testing Memory Operations:")
    
    # Store value in memory
    data = {
        "operation": "store",
        "value": 42,
        "session_id": SESSION_ID
    }
    
    response = test_api_endpoint("/api/memory", "POST", data)
    if response and response.status_code == 200:
        result = response.json()
        if result.get("success"):
            print(f"  ✅ Stored 42 in memory")
        else:
            print(f"  ❌ Failed to store: {result.get('error')}")
    
    # Recall value from memory
    data = {
        "operation": "recall",
        "session_id": SESSION_ID
    }
    
    response = test_api_endpoint("/api/memory", "POST", data)
    if response and response.status_code == 200:
        result = response.json()
        if result.get("success"):
            print(f"  ✅ Recalled from memory: {result['result']}")
        else:
            print(f"  ❌ Failed to recall: {result.get('error')}")

def test_history_operations():
    """Test history operations."""
    print("\n📜 Testing History Operations:")
    
    # Get history
    response = test_api_endpoint(f"/api/history?session_id={SESSION_ID}")
    if response and response.status_code == 200:
        result = response.json()
        if result.get("success"):
            history = result.get("history", [])
            print(f"  ✅ Retrieved history: {len(history)} items")
            if history:
                print(f"  📝 Latest: {history[-1]}")
        else:
            print(f"  ❌ Failed to get history: {result.get('error')}")
    
    # Clear history
    data = {"session_id": SESSION_ID}
    response = test_api_endpoint("/api/history", "DELETE", data)
    if response and response.status_code == 200:
        result = response.json()
        if result.get("success"):
            print(f"  ✅ History cleared successfully")
        else:
            print(f"  ❌ Failed to clear history: {result.get('error')}")

def test_main_page():
    """Test that the main page loads."""
    print("\n🌐 Testing Main Page:")
    
    response = test_api_endpoint("/")
    if response and response.status_code == 200:
        if "Python Calculator" in response.text:
            print("  ✅ Main page loads successfully")
            return True
        else:
            print("  ❌ Main page content incorrect")
            return False
    else:
        print("  ❌ Main page failed to load")
        return False

def main():
    """Main test function."""
    print("🧪 Testing Calculator Web API")
    print("=" * 40)
    
    # Check if server is running
    print("🔍 Checking if server is running...")
    if not test_main_page():
        print("\n❌ Server is not running or not accessible.")
        print("💡 Please start the server with: python3 app.py")
        sys.exit(1)
    
    # Run all tests
    test_expression_evaluation()
    test_memory_operations()
    test_history_operations()
    
    print("\n" + "=" * 40)
    print("✅ All tests completed!")
    print("🌐 Web calculator is ready to use at: http://localhost:5000")

if __name__ == "__main__":
    main()