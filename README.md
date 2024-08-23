# Quizzler App

## Project Overview

Quizzler is a quiz application built using Python's Tkinter library for the graphical user interface and the Open Trivia Database (OpenTDB) API for fetching trivia questions. The app presents a series of true/false questions to the user and keeps track of the score. The quiz ends when the user has answered all the questions.


## App Preview
<p align="center">
  <img src="https://github.com/Eyimofe28/Images/blob/main/Screenshot%202024-08-23%20173914.png?raw=true" width="200" height="350" />
  <img src="https://github.com/Eyimofe28/Images/blob/main/Screenshot%202024-08-23%20173953.png?raw=true" width="200" height="350" />
  <img src="https://github.com/Eyimofe28/Images/blob/main/Screenshot%202024-08-23%20174019.png?raw=true" width="200" height="350" />
</p>

## Features

- **Randomized Questions**: Questions are fetched randomly from the OpenTDB API.
- **Score Tracking**: The app tracks the user's score and displays it in real time.
- **Interactive GUI**: Users interact with the quiz through a simple and intuitive graphical interface built with Tkinter.
- **Feedback Mechanism**: The app provides immediate feedback on whether the user's answer was correct or incorrect.
- **End-of-Quiz Notification**: The app notifies the user when they have completed all the questions.

## Dependencies

- Python 3.x
- Tkinter (comes pre-installed with Python)
- Requests library (install via `pip install requests`)

## File Descriptions

### `quizzler_main.py`

This is the main entry point of the application. It initializes the question bank, sets up the quiz brain, and launches the user interface.

### `quizzler_ui.py`

This file defines the `QuizInterface` class, which manages the graphical user interface. It handles displaying questions, updating the score, and providing feedback to the user.

### `quiz_data.py`

This file handles fetching the trivia questions from the Open Trivia Database API. It sends a request to the API and stores the returned data in a `question_data` list.

### `quiz_brain.py`

This file defines the `QuizBrain` class, which manages the quiz logic, such as keeping track of the score, progressing through questions, and checking the user's answers.

### `question_model.py`

This file defines the `Question` class, which represents each question in the quiz. Each question has a text and an answer.

## Getting Started

1. **Clone the Repository**: Clone the project repository to your local machine.
   ```bash
   git clone <repository-url>
   ```

2. **Install Dependencies**: Install the required Python packages.
   ```bash
   pip install requests
   ```

3. **Run the Application**: Execute the `quizzler_main.py` file to start the quiz.
   ```bash
   python quizzler_main.py
   ```

## Contributing

If you would like to contribute to this project, feel free to fork the repository and submit a pull request with your changes. Ensure that your code is clean and well-documented.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

This readme should provide you with a good understanding of the Quizzler app and its components. If you have any questions or need further assistance, feel free to reach out!
