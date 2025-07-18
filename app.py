#!/usr/bin/env python3
"""
Flask Web Application for Python Calculator
Provides a web interface and REST API for calculator operations.
"""

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import json
import traceback
from calculator import Calculator

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Global calculator instance with session storage
calculators = {}

def get_calculator(session_id='default'):
    """Get or create a calculator instance for a session."""
    if session_id not in calculators:
        calculators[session_id] = Calculator()
    return calculators[session_id]

@app.route('/')
def index():
    """Serve the main calculator page."""
    return render_template('index.html')

@app.route('/api/calculate', methods=['POST'])
def api_calculate():
    """API endpoint for basic calculations."""
    try:
        data = request.get_json()
        session_id = data.get('session_id', 'default')
        operation = data.get('operation')
        operands = data.get('operands', [])
        
        calc = get_calculator(session_id)
        
        if operation == 'add':
            result = calc.add(operands[0], operands[1])
        elif operation == 'subtract':
            result = calc.subtract(operands[0], operands[1])
        elif operation == 'multiply':
            result = calc.multiply(operands[0], operands[1])
        elif operation == 'divide':
            result = calc.divide(operands[0], operands[1])
        elif operation == 'power':
            result = calc.power(operands[0], operands[1])
        elif operation == 'sqrt':
            result = calc.sqrt(operands[0])
        elif operation == 'sin':
            result = calc.sin(operands[0])
        elif operation == 'cos':
            result = calc.cos(operands[0])
        elif operation == 'tan':
            result = calc.tan(operands[0])
        elif operation == 'log':
            result = calc.log(operands[0])
        elif operation == 'ln':
            result = calc.ln(operands[0])
        elif operation == 'factorial':
            result = calc.factorial(int(operands[0]))
        else:
            return jsonify({'error': 'Invalid operation'}), 400
            
        return jsonify({
            'result': result,
            'success': True
        })
        
    except Exception as e:
        return jsonify({
            'error': str(e),
            'success': False
        }), 400

@app.route('/api/evaluate', methods=['POST'])
def api_evaluate():
    """API endpoint for expression evaluation."""
    try:
        data = request.get_json()
        session_id = data.get('session_id', 'default')
        expression = data.get('expression')
        
        calc = get_calculator(session_id)
        result = calc.evaluate_expression(expression)
        
        return jsonify({
            'result': result,
            'success': True
        })
        
    except Exception as e:
        return jsonify({
            'error': str(e),
            'success': False
        }), 400

@app.route('/api/memory', methods=['POST'])
def api_memory():
    """API endpoint for memory operations."""
    try:
        data = request.get_json()
        session_id = data.get('session_id', 'default')
        operation = data.get('operation')
        value = data.get('value', 0)
        
        calc = get_calculator(session_id)
        
        if operation == 'store':
            calc.store_memory(value)
            result = calc.recall_memory()
        elif operation == 'recall':
            result = calc.recall_memory()
        elif operation == 'clear':
            calc.clear_memory()
            result = 0
        elif operation == 'add':
            calc.store_memory(calc.recall_memory() + value)
            result = calc.recall_memory()
        else:
            return jsonify({'error': 'Invalid memory operation'}), 400
            
        return jsonify({
            'result': result,
            'memory_value': calc.recall_memory(),
            'success': True
        })
        
    except Exception as e:
        return jsonify({
            'error': str(e),
            'success': False
        }), 400

@app.route('/api/history', methods=['GET'])
def api_history():
    """API endpoint to get calculation history."""
    try:
        session_id = request.args.get('session_id', 'default')
        calc = get_calculator(session_id)
        
        return jsonify({
            'history': calc.get_history(),
            'success': True
        })
        
    except Exception as e:
        return jsonify({
            'error': str(e),
            'success': False
        }), 400

@app.route('/api/history', methods=['DELETE'])
def api_clear_history():
    """API endpoint to clear calculation history."""
    try:
        data = request.get_json() or {}
        session_id = data.get('session_id', 'default')
        calc = get_calculator(session_id)
        
        calc.clear_history()
        
        return jsonify({
            'message': 'History cleared',
            'success': True
        })
        
    except Exception as e:
        return jsonify({
            'error': str(e),
            'success': False
        }), 400

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    print("Starting Calculator Web Application...")
    print("Access the calculator at: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)