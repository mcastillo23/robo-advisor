# robo-advisor

An example financial planning application which helps customers make investment decisions. The system accepts a stock or cryptocurrency ticker as inputs and returns a recommendation as to whether the customer should buy the security or not. 

## Prerequisites

  + Anaconda 3.7+
  + Python 3.7+
  + Pip

## Installation
Fork this [remote repository](https://github.com/mcastillo23/robo-advisor) under your own control, then "clone" or download your remote copy onto your local computer.

Then navigate there from the command line (subsequent commands assume you are running them from the local repository's root directory):

```sh
cd robo-advisor 
```

Use Anaconda to create and activate a new virtual environment, perhaps called "shopping-env":

```sh
conda create -n stocks-env python=3.8 
conda activate stocks-env
```

From inside the virtual environment, install package dependencies:

```sh
pip install -r requirements.txt
```

> NOTE: if this command throws an error like "Could not open requirements file: [Errno 2] No such file or directory", make sure you are running it from the repository's root directory, where the requirements.txt file exists (see the initial `cd` step above)

## Setup

This program requires an API Key from AlphaVantage(https://www.alphavantage.co/). After requesting your free API Key, create a new file called ".env" in the root directory of your local repository. Then, update the contents of the ".env" file to match your personal API Key. Example ".env" contents:

    ALPHAVANTAGE_API_KEY="abc123"

> NOTE: the ".env" file is usually the place for passing configuration options and secret credentials, so as a best practice we don't upload this file to version control (which is accomplished via a corresponding entry in the [.gitignore](/.gitignore) file)

## Usage

Run the application script:

```py
python app/robo_advisor.py
```

> NOTE: if you see an error like "ModuleNotFoundError: No module named '...'", it's because the given package isn't installed, so run the `pip` command above to ensure that package has been installed into the virtual environment