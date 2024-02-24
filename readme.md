# London Prayer Times Project

This project provides a Python script to retrieve and display prayer times for London from two sources: London Aziziye Mosque and the Turkish Directorate of Religious Affairs.

The script also includes functionality to play the Azan (call to prayer) from a specified Spotify device, as configured in the .env file.

## Table of Contents

- Introduction
- Folder Structure
- Dependencies
- Installation
- Usage
- Configuration
- Contributing
- License

## Introduction

London Prayer Times Project is a Python script designed to fetch and display accurate prayer times for London. It utilizes data from London Aziziye Mosque and the Turkish Directorate of Religious Affairs.


## Dependencies

The project relies on the following Python packages:

- `selenium`: For web automation.
- `requests`: For making HTTP requests.
- Other standard Python libraries.

It was tested and built with Python `3.11.7` and pip `24.0`
## Installation

1. Clone the repository:

```
git clone https://github.com/yourusername/london-prayer-times.git
cd london-prayer-times
```

2. Install the required dependencies:

```
pip install -r requirements.txt
```


## Usage

To run the script, execute the following command in the terminal:

```
python src/main.py
```


The script will fetch prayer times and make decisions on playing specific playlists based on the current time.

## Configuration

Configure the script by modifying the `.env` file. Add your Spotify username, password and device names.

## Test

You can run tests with

```
python -m unittest discover tests
```

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the project.

## License

This project is licensed under the MIT License.