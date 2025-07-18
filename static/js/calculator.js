// Calculator Web Interface JavaScript
class CalculatorApp {
    constructor() {
        this.currentExpression = '';
        this.result = '0';
        this.lastResult = 0;
        this.memory = 0;
        this.isScientificMode = false;
        this.sessionId = this.generateSessionId();
        
        this.initializeEventListeners();
        this.loadHistory();
        this.updateMemoryDisplay();
    }

    generateSessionId() {
        return 'session_' + Math.random().toString(36).substr(2, 9);
    }

    initializeEventListeners() {
        // Mode toggle
        document.getElementById('toggle-mode').addEventListener('click', () => {
            this.toggleMode();
        });

        // Keyboard support
        document.addEventListener('keydown', (event) => {
            this.handleKeypress(event);
        });

        // Expression input enter key
        document.getElementById('expression-input').addEventListener('keypress', (event) => {
            if (event.key === 'Enter') {
                this.evaluateExpression();
            }
        });
    }

    toggleMode() {
        this.isScientificMode = !this.isScientificMode;
        const basicMode = document.querySelector('.basic-mode');
        const scientificMode = document.querySelector('.scientific-mode');
        const modeText = document.getElementById('mode-text');

        if (this.isScientificMode) {
            basicMode.style.display = 'none';
            scientificMode.style.display = 'grid';
            modeText.textContent = 'Basic';
        } else {
            basicMode.style.display = 'grid';
            scientificMode.style.display = 'none';
            modeText.textContent = 'Scientific';
        }
    }

    handleKeypress(event) {
        const key = event.key;
        
        // Prevent default for calculator keys
        if ('0123456789+-*/=.()'.includes(key) || key === 'Enter' || key === 'Backspace') {
            event.preventDefault();
        }

        if ('0123456789'.includes(key)) {
            this.appendNumber(key);
        } else if ('+-*/'.includes(key)) {
            this.appendOperator(key);
        } else if (key === '.') {
            this.appendNumber('.');
        } else if (key === 'Enter' || key === '=') {
            this.calculate();
        } else if (key === 'Backspace') {
            this.backspace();
        } else if (key === 'Escape') {
            this.clearAll();
        } else if (key === 'Delete') {
            this.clearEntry();
        }
    }

    updateDisplay() {
        document.getElementById('expression').textContent = this.currentExpression;
        document.getElementById('result').textContent = this.result;
    }

    updateMemoryDisplay() {
        document.getElementById('memory-indicator').textContent = `Memory: ${this.memory}`;
    }

    appendNumber(number) {
        if (this.result !== '0' && this.currentExpression === '') {
            this.currentExpression = this.result;
        }
        
        if (this.currentExpression === '0' && number !== '.') {
            this.currentExpression = number;
        } else {
            this.currentExpression += number;
        }
        
        this.updateDisplay();
    }

    appendOperator(operator) {
        if (this.currentExpression === '' && this.result !== '0') {
            this.currentExpression = this.result;
        }
        
        if (this.currentExpression === '') {
            return;
        }

        // Replace * with × for display, but keep * for calculation
        const lastChar = this.currentExpression.slice(-1);
        if ('+-*/^'.includes(lastChar)) {
            this.currentExpression = this.currentExpression.slice(0, -1);
        }
        
        this.currentExpression += operator;
        this.updateDisplay();
    }

    appendFunction(func) {
        if (func === 'factorial') {
            if (this.currentExpression === '' && this.result !== '0') {
                this.currentExpression = this.result + '!';
            } else {
                this.currentExpression += '!';
            }
        } else {
            this.currentExpression += func + '(';
        }
        this.updateDisplay();
    }

    appendConstant(constant) {
        if (this.result !== '0' && this.currentExpression === '') {
            this.currentExpression = this.result;
        }
        this.currentExpression += constant;
        this.updateDisplay();
    }

    clearAll() {
        this.currentExpression = '';
        this.result = '0';
        this.updateDisplay();
    }

    clearEntry() {
        this.currentExpression = '';
        this.updateDisplay();
    }

    backspace() {
        if (this.currentExpression.length > 0) {
            this.currentExpression = this.currentExpression.slice(0, -1);
            if (this.currentExpression === '') {
                this.result = '0';
            }
            this.updateDisplay();
        }
    }

    toggleSign() {
        if (this.currentExpression === '' && this.result !== '0') {
            this.result = (parseFloat(this.result) * -1).toString();
        } else if (this.currentExpression !== '') {
            if (this.currentExpression.startsWith('-')) {
                this.currentExpression = this.currentExpression.slice(1);
            } else {
                this.currentExpression = '-' + this.currentExpression;
            }
        }
        this.updateDisplay();
    }

    async calculate() {
        if (this.currentExpression === '') {
            return;
        }

        try {
            const response = await fetch('/api/evaluate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    expression: this.currentExpression,
                    session_id: this.sessionId
                })
            });

            const data = await response.json();

            if (data.success) {
                this.result = data.result.toString();
                this.lastResult = data.result;
                this.currentExpression = '';
                this.updateDisplay();
                this.loadHistory();
                this.showSuccessToast('Calculation completed');
            } else {
                this.showErrorToast(data.error);
                this.shakeCalculator();
            }
        } catch (error) {
            this.showErrorToast('Network error occurred');
            this.shakeCalculator();
        }
    }

    async evaluateExpression() {
        const expression = document.getElementById('expression-input').value.trim();
        
        if (expression === '') {
            this.showErrorToast('Please enter an expression');
            return;
        }

        try {
            const response = await fetch('/api/evaluate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    expression: expression,
                    session_id: this.sessionId
                })
            });

            const data = await response.json();

            if (data.success) {
                this.result = data.result.toString();
                this.lastResult = data.result;
                this.currentExpression = '';
                this.updateDisplay();
                this.loadHistory();
                this.showSuccessToast(`Result: ${data.result}`);
                document.getElementById('expression-input').value = '';
            } else {
                this.showErrorToast(data.error);
            }
        } catch (error) {
            this.showErrorToast('Network error occurred');
        }
    }

    async memoryClear() {
        try {
            const response = await fetch('/api/memory', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    operation: 'clear',
                    session_id: this.sessionId
                })
            });

            const data = await response.json();

            if (data.success) {
                this.memory = data.memory_value;
                this.updateMemoryDisplay();
                this.showSuccessToast('Memory cleared');
            } else {
                this.showErrorToast(data.error);
            }
        } catch (error) {
            this.showErrorToast('Network error occurred');
        }
    }

    async memoryRecall() {
        try {
            const response = await fetch('/api/memory', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    operation: 'recall',
                    session_id: this.sessionId
                })
            });

            const data = await response.json();

            if (data.success) {
                this.result = data.result.toString();
                this.currentExpression = '';
                this.updateDisplay();
                this.showSuccessToast(`Recalled: ${data.result}`);
            } else {
                this.showErrorToast(data.error);
            }
        } catch (error) {
            this.showErrorToast('Network error occurred');
        }
    }

    async memoryStore() {
        const value = this.currentExpression !== '' ? 
            parseFloat(this.currentExpression) : 
            parseFloat(this.result);

        if (isNaN(value)) {
            this.showErrorToast('Invalid value to store');
            return;
        }

        try {
            const response = await fetch('/api/memory', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    operation: 'store',
                    value: value,
                    session_id: this.sessionId
                })
            });

            const data = await response.json();

            if (data.success) {
                this.memory = data.memory_value;
                this.updateMemoryDisplay();
                this.showSuccessToast(`Stored: ${value}`);
            } else {
                this.showErrorToast(data.error);
            }
        } catch (error) {
            this.showErrorToast('Network error occurred');
        }
    }

    async memoryAdd() {
        const value = this.currentExpression !== '' ? 
            parseFloat(this.currentExpression) : 
            parseFloat(this.result);

        if (isNaN(value)) {
            this.showErrorToast('Invalid value to add');
            return;
        }

        try {
            const response = await fetch('/api/memory', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    operation: 'add',
                    value: value,
                    session_id: this.sessionId
                })
            });

            const data = await response.json();

            if (data.success) {
                this.memory = data.memory_value;
                this.updateMemoryDisplay();
                this.showSuccessToast(`Added ${value} to memory`);
            } else {
                this.showErrorToast(data.error);
            }
        } catch (error) {
            this.showErrorToast('Network error occurred');
        }
    }

    async loadHistory() {
        try {
            const response = await fetch(`/api/history?session_id=${this.sessionId}`);
            const data = await response.json();

            if (data.success) {
                this.displayHistory(data.history);
            }
        } catch (error) {
            console.error('Failed to load history:', error);
        }
    }

    displayHistory(history) {
        const historyList = document.getElementById('history-list');
        
        if (history.length === 0) {
            historyList.innerHTML = '<p class="no-history">No calculations yet</p>';
            return;
        }

        historyList.innerHTML = '';
        
        // Show last 10 calculations
        const recentHistory = history.slice(-10).reverse();
        
        recentHistory.forEach(item => {
            const historyItem = document.createElement('div');
            historyItem.className = 'history-item fade-in';
            historyItem.textContent = item;
            historyItem.addEventListener('click', () => {
                const result = item.split(' = ')[1];
                if (result) {
                    this.result = result;
                    this.currentExpression = '';
                    this.updateDisplay();
                }
            });
            historyList.appendChild(historyItem);
        });
    }

    async clearHistory() {
        try {
            const response = await fetch('/api/history', {
                method: 'DELETE',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    session_id: this.sessionId
                })
            });

            const data = await response.json();

            if (data.success) {
                this.loadHistory();
                this.showSuccessToast('History cleared');
            } else {
                this.showErrorToast(data.error);
            }
        } catch (error) {
            this.showErrorToast('Network error occurred');
        }
    }

    showErrorToast(message) {
        const toast = document.getElementById('error-toast');
        const messageElement = document.getElementById('error-message');
        
        messageElement.textContent = message;
        toast.classList.add('show');
        
        setTimeout(() => {
            toast.classList.remove('show');
        }, 3000);
    }

    showSuccessToast(message) {
        const toast = document.getElementById('success-toast');
        const messageElement = document.getElementById('success-message');
        
        messageElement.textContent = message;
        toast.classList.add('show');
        
        setTimeout(() => {
            toast.classList.remove('show');
        }, 2000);
    }

    shakeCalculator() {
        const calculator = document.querySelector('.calculator');
        calculator.classList.add('shake');
        
        setTimeout(() => {
            calculator.classList.remove('shake');
        }, 500);
    }
}

// Global functions for HTML onclick events
let calculatorApp;

function appendNumber(number) {
    calculatorApp.appendNumber(number);
}

function appendOperator(operator) {
    calculatorApp.appendOperator(operator);
}

function appendFunction(func) {
    calculatorApp.appendFunction(func);
}

function appendConstant(constant) {
    calculatorApp.appendConstant(constant);
}

function clearAll() {
    calculatorApp.clearAll();
}

function clearEntry() {
    calculatorApp.clearEntry();
}

function backspace() {
    calculatorApp.backspace();
}

function toggleSign() {
    calculatorApp.toggleSign();
}

function calculate() {
    calculatorApp.calculate();
}

function evaluateExpression() {
    calculatorApp.evaluateExpression();
}

function memoryClear() {
    calculatorApp.memoryClear();
}

function memoryRecall() {
    calculatorApp.memoryRecall();
}

function memoryStore() {
    calculatorApp.memoryStore();
}

function memoryAdd() {
    calculatorApp.memoryAdd();
}

function clearHistory() {
    calculatorApp.clearHistory();
}

// Initialize the calculator when the page loads
document.addEventListener('DOMContentLoaded', () => {
    calculatorApp = new CalculatorApp();
});