# Console-Based To-Do List Application

A robust, terminal-based To-Do List application built in Python that allows users to manage daily tasks seamlessly. This project features strong exception handling to prevent program crashes during invalid user interactions.

## Features

- **Add Multiple Tasks:** Prompt the user to enter a specific number of tasks and capture them sequentially.
- **Delete Tasks Safely:** Remove completed or unwanted tasks by their listing index.
- **View Tasks:** A clean interface showing all active tasks with standard numbered formatting.
- **Robust Exception Handling:** 
  - Prevents crashes when strings/letters are entered into numerical inputs (`ValueError`).
  - Safeguards against selecting numbers out of range when deleting (`IndexError`).
  - Automatically identifies empty list states gracefully.

## Technologies Used

- **Python 3.x** (Standard built-in libraries only; zero external dependencies)

## Project Structure

```text
├── to-do-list.py  # The application entry point (handles loop & user menu)
├── operation.py   # Core backend functions (Add, Delete, View logic)
└── README.md      # Project documentation
```
 ## Getting Started
 ### Prerequisites
 Make sure you have Python installed on your machine. check your Python version by running:
 
 ```bash
python --version
 ```

## Installation & Execution
- Clone the repository to your local machine:
```bash
git clone https://github.com/Harshu-052006/to-do-list.git
cd to-do-list
```

- Run the application:
```bash
python to-do-list.py
```

## How it Works
1. Main Loop: to-do-list.py contains the main loop that continuously prompts the user for actions until they choose to exit.
2. Moduler Architecture: operation.py contains the core functions for adding, deleting, and viewing tasks, keeping the code organized and maintainable.
3. Input Verification: 
   - When adding tasks, the program ensures that the user inputs a valid number of tasks.
   - When deleting tasks, it checks if the input index is valid and within range.
   - The application handles empty task lists gracefully, informing the user when there are no tasks to display or delete.


## Future Improvements

- **Persistent Storage:** Add functionality to save the To-Do list to a local `tasks.txt` or `tasks.json` file so tasks aren't lost when the program closes.
- **Due Dates:** Allow users to assign deadlines and sorting options for their tasks.
- **GUI Version:** Build a graphical user interface using Python's `tkinter` library.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page or submit a pull request if you want to improve the logic or add features.

## License

This project is open-source and available under the [MIT License](LICENSE) file for more details.