# Python Calculator

A comprehensive calculator application with **web interface**, command-line, and graphical user interfaces. Supports basic arithmetic operations, scientific functions, expression evaluation, and memory operations.

## 🌟 Features

### Basic Operations
- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)
- Power (^)

### Scientific Functions
- Square root (sqrt)
- Trigonometric functions (sin, cos, tan)
- Logarithms (log base 10, natural log)
- Factorial (!)

### Additional Features
- **Web interface** with modern, responsive design
- Expression evaluation with mathematical functions
- Memory operations (store, recall, clear, add)
- Calculation history with session management
- Error handling for invalid operations
- Multi-interface support (Web, GUI, CLI)
- Keyboard shortcuts and accessibility features

## 🚀 Usage

### Web Interface (Recommended)

The calculator now includes a beautiful web interface that works in any modern browser!

**Start the web application:**
```bash
# Method 1: Using the startup script
./start_web.sh

# Method 2: Manual start
pip3 install --break-system-packages -r requirements.txt
python3 app.py
```

Then open your browser and navigate to: **http://localhost:5000**

#### Web Features:
- **Modern Design**: Beautiful, responsive interface with gradient backgrounds
- **Dual Modes**: Switch between Basic and Scientific calculator modes
- **Real-time History**: See your calculations appear instantly in the history panel
- **Memory Operations**: Full memory functionality with visual feedback
- **Expression Evaluator**: Dedicated input for complex mathematical expressions
- **Keyboard Support**: Use your keyboard for quick calculations
- **Touch Friendly**: Works great on mobile devices and tablets
- **Error Handling**: Elegant error messages with toast notifications
- **Session Management**: Each browser session maintains its own calculation history

#### Keyboard Shortcuts:
- **Numbers & Operators**: Direct input via keyboard
- **Enter** or **=**: Calculate result
- **Escape**: Clear all
- **Backspace**: Remove last character
- **Delete**: Clear current entry

### Command Line Interface (CLI)

Run the calculator in CLI mode:
```bash
python3 calculator.py --cli
```

The CLI provides a menu-driven interface with the following options:
1. **Basic Operations** - Perform arithmetic calculations
2. **Scientific Functions** - Access advanced mathematical functions
3. **Expression Evaluator** - Evaluate complex mathematical expressions
4. **Memory Operations** - Store and recall values
5. **View History** - See previous calculations
6. **Clear History** - Clear calculation history
7. **Exit** - Close the calculator

### Graphical User Interface (GUI)

Run the calculator in GUI mode:
```bash
python3 calculator.py --gui
```

Or simply run without arguments (defaults to GUI):
```bash
python3 calculator.py
```

**Note**: GUI mode requires `tkinter`. If not available, the calculator automatically falls back to CLI mode.

### GUI Features
- Calculator-style button interface
- Memory display showing current memory value
- Keyboard support for number input
- Function buttons for scientific operations
- Error handling with popup dialogs

## 🧮 Expression Evaluator

The calculator can evaluate complex mathematical expressions. Supported functions and constants:

- **Operators**: `+`, `-`, `*`, `/`, `^` (power)
- **Functions**: `sin()`, `cos()`, `tan()`, `sqrt()`, `log()`, `ln()`
- **Constants**: `pi`, `e`

#### Examples:
```
2 + 3 * 4           # Result: 14
sqrt(16) + 2^3      # Result: 12.0
sin(pi/2)           # Result: 1.0
log(100) + ln(e)    # Result: 3.0
```

## 💾 Memory Operations

The calculator includes memory functionality:
- **MS**: Store current value in memory
- **MR**: Recall value from memory
- **MC**: Clear memory
- **M+**: Add current value to memory

## ⚠️ Error Handling

The calculator handles common errors gracefully:
- Division by zero
- Square root of negative numbers
- Logarithm of non-positive numbers
- Invalid expressions
- Factorial of negative numbers

## 🧪 Testing

Run the test script to verify functionality:
```bash
python3 test_calculator.py
```

This will test all calculator functions and display the results.

## 📋 Requirements

### Web Interface
- Python 3.x
- Flask 2.3.3
- Flask-CORS 4.0.0
- Modern web browser (Chrome, Firefox, Safari, Edge)

### Desktop Applications
- Python 3.x
- `tkinter` (optional, for GUI mode)
- Standard library modules: `math`, `sys`, `re`

## 🏗️ Code Structure

The calculator is organized into several components:

### Backend (Python)
- **Calculator**: Core calculation engine with all mathematical operations
- **CalculatorGUI**: Graphical user interface using tkinter
- **CalculatorCLI**: Command-line interface for terminal use
- **Flask App**: Web server providing REST API and serving the frontend

### Frontend (Web)
- **HTML**: Modern, semantic structure with accessibility features
- **CSS**: Responsive design with animations and modern styling
- **JavaScript**: Interactive functionality and API communication

### API Endpoints
- `GET /` - Serve the main calculator page
- `POST /api/evaluate` - Evaluate mathematical expressions
- `POST /api/memory` - Memory operations (store, recall, clear, add)
- `GET /api/history` - Retrieve calculation history
- `DELETE /api/history` - Clear calculation history

## 📱 Responsive Design

The web interface is fully responsive and works on:
- **Desktop computers** (Windows, macOS, Linux)
- **Tablets** (iPad, Android tablets)
- **Mobile phones** (iOS, Android)
- **Any device with a modern web browser**

## 🎨 Screenshots

The web interface features:
- **Beautiful gradient background** with glass-morphism effects
- **Intuitive button layout** with hover animations
- **Live calculation history** with clickable results
- **Memory indicator** showing current stored value
- **Toast notifications** for feedback and errors
- **Smooth transitions** and micro-interactions

## 📖 Examples

### Web Interface Usage
1. Open http://localhost:5000 in your browser
2. Click numbers and operators to build expressions
3. Press "=" or Enter to calculate
4. Use the mode toggle to switch between Basic/Scientific
5. View your calculation history in the side panel
6. Use memory buttons (MC, MR, MS, M+) for memory operations

### Basic Usage (CLI)
```bash
$ python3 calculator.py --cli
Welcome to Python Calculator!

==================================================
         PYTHON CALCULATOR
==================================================
1. Basic Operations
2. Scientific Functions
3. Expression Evaluator
4. Memory Operations
5. View History
6. Clear History
7. Exit
--------------------------------------------------
Enter your choice (1-7): 1

Basic Operations:
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Power (^)

Select operation (1-5): 1
Enter first number: 10
Enter second number: 5

Result: 15.0
```

### Expression Evaluation
```bash
Enter your choice (1-7): 3

Expression Evaluator
Supported: +, -, *, /, ^, sin, cos, tan, sqrt, log, ln, pi, e
Example: sin(pi/2) + sqrt(16) * 2

Enter expression: 2^3 + sqrt(9)
Result: 11.0
```

## 🔧 Installation & Setup

1. **Clone or download** the calculator files
2. **Install dependencies** (for web interface):
   ```bash
   pip3 install --break-system-packages -r requirements.txt
   ```
3. **Choose your interface**:
   - Web: `./start_web.sh` or `python3 app.py`
   - GUI: `python3 calculator.py`
   - CLI: `python3 calculator.py --cli`

## 🌐 Deployment

The web application can be deployed to:
- **Local development**: `python3 app.py`
- **Production servers**: Use gunicorn or similar WSGI server
- **Cloud platforms**: Heroku, AWS, Google Cloud, etc.
- **Docker containers**: Create Dockerfile based on Python image

## 📄 License

This calculator is provided as-is for educational and practical use.

---

**Author**: AI Assistant  
**Version**: 2.0 (Web Interface Added)  
**Last Updated**: 2024  
**Technologies**: Python, Flask, HTML5, CSS3, JavaScript, tkinter