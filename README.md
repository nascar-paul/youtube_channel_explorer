# YouTube Channel Video Fetcher
A simple Python script to fetch and list all videos from a specified YouTube channel using the YouTube Data API v3.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites
Before running this script, you need to have Python installed on your system. This script was developed with Python 3.x. 

### Setting Up a Virtual Environment (Highly Suggested)

Using a virtual environment is not mandatory, but it is highly recommended to avoid potential conflicts with other Python packages you may have installed.

1. Install `virtualenv` if you haven't:
  ```
pip install virtualenv
  ```

2. Create a virtual environment. While "Youtube" is the suggested name for the virtual environment, you can choose any name you prefer:
  ```
virtualenv Youtube
  ```

3. Activate the virtual environment:

- On Windows:
  ```
  .\Youtube\Scripts\activate
  ```

- On macOS and Linux:
  ```
  source Youtube/bin/activate
  ```

### Installing the Required Library

1. Install the `google-api-python-client` library:
  ```
pip install --upgrade google-api-python-client
  ```
2. Install the `google_api` client library: 
  ```
pip install youtube_transcript_api pytube
```

## Installation

1. Clone this repository:
  ```
git clone https://github.com/nascar-paul/youtube_channel_explorer.git
  ```
  If you do not have Python installed, you can download it from python.org.

Additionally, you will need the google-api-python-client package. You can install this package using pip:

bash
```Copy code
pip install --upgrade google-api-python-client
```

## Setting up the YouTube Data API
Go to the Google Developers Console.

Create a new project.
Once the project is created, select it and go to the "Library" section.
Search for "YouTube Data API v3" and enable it for your project.

Go to the "Credentials" section and create an API key.

## Running the Script
Clone this repository to your local machine or download the .py file.
Open a terminal/command prompt in the directory where the script is located.

Run the script using Python:

## bash

```Copy code
python YouTubeChannelVideoFetcher.py
```
When prompted, enter your API key and the YouTube channel ID you want to fetch videos from.

# Built With
Python - The programming language used.
Google API Python Client - The client library for accessing the Google APIs.

# Contributing
Please read CONTRIBUTING.md for details on my proposed code of conduct, and the process for submitting pull requests.

Pull requests are welcome, but for major changes, please open an issue first to discuss what you would like to change.

# License
This project is licensed under the MIT License - see the LICENSE.md file for details.

# Acknowledgments
Google Developers for providing the YouTube Data API v3.

Python Community for the invaluable resources and documentation.