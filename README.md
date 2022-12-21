# L03T12 - Compulsory Task 1

# Welcome:

Welcome to my program 'semantic.py' for L03T12 - Compulsory Task 1.

## **Contents:**

* Description.
* Installation.
* Usage.
* Credits.


## **Description:**
This is a simple program that uses spacy's en_core_web_md language model to run through examples and compare words.

## **Installation:**
To install download the files from the git Repo to your local machine.

**If you are using MacOS**

Use the following *commands* in terminal/bash:

1. Install virtualenvwrapper

$ *pip3 install virtualenvwrapper*

2. Create the "virtualenvs" folder

$ *mkdir ~/.virtualenvs*

3. Before you export this, make sure you are doing it in your project folder, because that's where you will activate the virtualenv

Export:

$ *export WORKON_HOME=$HOME/.virtualenvs*

next, write down in terminal which python3, to find the path and add it after the "=" sign

$ *export VIRTUALENVWRAPPER_PYTHON=*

in my case:

$ *export VIRTUALENVWRAPPER_PYTHON=/Library/Frameworks/Python.framework/Versions/3.10/bin/python3*

to find the virtualenv path write in the terminal *which virtualenv*

add the path after the "=" sign

$ *export VIRTUALENVWRAPPER_VIRTUALENV=*

in my case:

$ *export VIRTUALENVWRAPPER_VIRTUALENV=/Library/Frameworks/Python.framework/Versions/3.10/bin/virtualenv*


4. Last step is to add the source in the terminal

almost the same as the path you got when writing which virtualenv

The difference is the "wrapper.sh" in the end.

in my case

$ *source /Library/Frameworks/Python.framework/Versions/3.10/bin/virtualenvwrapper.sh*

5. Now you can create the virtualenv name by doing the following:

$ *mkvirtualenv nameOfTheVirtualEnviroment*

in my case

$ *mkvirtualenv L03T10*

Now you have your virtual enviroment setup.

Use the below function to install all of the required modules:

$ *pip install -r requirements.txt*

Your virtual enviroment should now be set up.

**DOCKER:**

You can download the docker files at: https://hub.docker.com/r/haydenbp/l03t12.1

Use terminal / bash to 'cd' to the root directory of the downloaded files.

Then use the following commands to create the container and run the program:

$ *docker build -t python-app ./*
$ *docker run python-app*


## **Usage**:

To use run the app. cd to to the root directory with terminal.

run the command:

$ *python3 garden.py run*


## **Credits**:

The site and all of its contents were created by myself *Hayden Poulter* . You can contact me at haydenbp@protonmail.com.

Thanks for reading.