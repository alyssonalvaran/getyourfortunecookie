# Fortune Cookie Generator

This is a simple fortune cookie generator that displays a quote to the user and allows him/her to submit one.

Check out: [https://getyourfortunecookie.herokuapp.com/](https://getyourfortunecookie.herokuapp.com/)

## Getting Started

These instructions will get you a copy of the project up and running on your local Windows machine for development purposes.

### Prerequisites

Open your console and check if you have Python 3.x installed:

```
$ python --version
```

This should display the version installed on your machine. If you don't have it yet, check out their [official website](https://www.python.org/downloads/).

### Installing

These series of instructions will allow you to get this app running on a development environment.

1. Go to the directory where you want to store your files and clone this repository:

```
$ cd path/to/directory
$ git clone https://github.com/alyssonalvaran/getyourfortunecookie.git
```

2. Go inside the folder and create a virtual environment:

```
$ cd getyourfortunecookie
$ pip install virtualenv
$ virtualenv env
```

This will create a folder named `env` inside your directory.

3. Activate your virtual environment and install the packages inside `requirements.txt`:

```
$ .\env\Scripts\activate
$ pip install -r requirements.txt -y
```

4. Turn debug mode on (optional):

```
$ SET FLASK_DEBUG=1
```

5. Run the app:
```
flask run
```

You can stop the app by typing in `CTRL + C`.

## Running the tests

The tests are located in the `test_sayings.py` file. These tests check for the following:
* `test_get_sayings_list` tests if get_sayings_list returns a list of strings.
* `test_get_random_saying` tests if get_random_saying return a string saying and an integer index.
* `test_overwrite_saying` tests if overwrite_saying overwrites the previous value of the file.

To run the tests, just enter this in your console:
```
$ pytest
```

## Deployment

This application is deployed in [Heroku](https://heroku.com/) and automatically updates whenever there are changes pushed to the master branch of this repository.

## Built With

* [Flask](https://www.palletsprojects.com/p/flask/)
* [Bootstrap 4](https://getbootstrap.com/docs/4.0/getting-started/introduction/)

## Author

* [Alysson Alvaran](http://alyssonalvaran.com/)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details