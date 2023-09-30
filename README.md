# pyVocTutor
Vocabulary Tutor is a Python script that helps in building Vocabulary.
It is using the idea of VocTutor created by Mathew Isaac. 

For now, I've created a CLI based solution. Later, planning to add GUI version. 

## Features

- Supports multi user Vocabulary database.
- Simple text based config, data file.
- Multiple Vocab input files can be added so that user can jump from one category to another.
- Similar to original VocTutor, it removes word only if it has been answered multiple times correctly (i.e. the number of trials specified by user).

## Getting Started

### Prerequisites

To run the pyVocTutor, you need to have Python installed on your system. Ensure you have a compatible version of Python installed.

### Installation

1. Clone this repository to your local machine:

```bash
git clone https://github.com/vmnit/pyVocTutor.git
```

2. Navigate to the project directory:
```bash
cd pyVocTutor
```

### Usage
To run the tool:
1. Default ROOT_DIR is D:\pyVocTutor, but one can pass your own directory with --root_dir option.
2. Run the tool with the following command:
```bash
python pyVocTutor.py --root_dir <Root directory where data files will be stored>
```
3. The tool will generate some config file and data file in that location.
4. Tool will ask for user to create user profile in config file. If already existing, user needs to select the option.
5. Then, the tool will ask for vocab data file, which will be used to create questionare. 
To create the questionare, the tool will create a data file in user's directory in the root directory.
6. The tool will ask for number of correct answers to be required to not ask this word again.
7. Once everything is done, it will start asking question.
   1. It will respond in CORRECT or WRONG answer and will share number of trials remaining.
   2. The number of trials will reduce only if the answer is correct.

Enjoy learning !!!

## Contributing
Contributions to the the project are welcome! If you encounter any issues or have suggestions for improvements, please submit them in the [issue tracker](https://github.com/vmnit/pyVocTutor/issues).
Before making a contribution, kindly review the [contribution guidelines](CONTRIBUTING.md) for instructions on how to get started.

## License
This project is licensed under the [General Public License](License). Feel free to use, modify, and distribute the code within the terms of the license.
