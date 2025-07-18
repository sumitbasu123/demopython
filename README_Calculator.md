# Python Calculator

A comprehensive calculator application with both command-line and graphical user interfaces. Supports basic arithmetic operations, scientific functions, expression evaluation, and memory operations.

## Features

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
- Expression evaluation with mathematical functions
- Memory operations (store, recall, clear, add)
- Calculation history
- Error handling for invalid operations
- Both GUI and CLI interfaces

## Usage

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

### Expression Evaluator

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

## Memory Operations

The calculator includes memory functionality:
- **MS**: Store current value in memory
- **MR**: Recall value from memory
- **MC**: Clear memory
- **M+**: Add current value to memory

## Error Handling

The calculator handles common errors gracefully:
- Division by zero
- Square root of negative numbers
- Logarithm of non-positive numbers
- Invalid expressions
- Factorial of negative numbers

## Testing

Run the test script to verify functionality:
```bash
python3 test_calculator.py
```

This will test all calculator functions and display the results.

## Requirements

- Python 3.x
- `tkinter` (optional, for GUI mode)
- Standard library modules: `math`, `sys`, `re`

## Code Structure

The calculator is organized into several classes:

- **Calculator**: Core calculation engine with all mathematical operations
- **CalculatorGUI**: Graphical user interface using tkinter
- **CalculatorCLI**: Command-line interface for terminal use

## Examples

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

## License

This calculator is provided as-is for educational and practical use.

---

**Author**: AI Assistant  
**Version**: 1.0  
**Last Updated**: 2024