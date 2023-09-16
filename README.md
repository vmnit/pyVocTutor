# pyVocTutor
Vocabulary Tutor is a Python script that helps in building Vocabulary. It is using the idea of VocTutor created by Mathew Isaac. 

For now, I've created a CLI based solution. Later, planning to add GUI version. 

## Features

- Supports multi user Vocabulary database.
- Simple text based config, data file.
- Multiple Vocab input files can be added so that user can jump from one category to another.
- Similar to original VocTutor, it removes word only if it has been answered multiple times correctly.

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
To generate a test template file, follow these steps:
1. Update the main.py script with your preferred ROOT_DIR
2. The tool will generate some config file and data file in that location.
3. Run the script with the following command:

```bash
python pyVocTutor.py --root_dir <Root directory where data files will be stored>
```


## Contributing
Contributions to the Test Template Generator are welcome! If you encounter any issues or have suggestions for improvements, please submit them in the [issue tracker](https://github.com/vmnit/pyVocTutor/issues).
Before making a contribution, kindly review the [contribution guidelines](CONTRIBUTING.md) for instructions on how to get started.

## License
This project is licensed under the [General Public License](License). Feel free to use, modify, and distribute the code within the terms of the license.
