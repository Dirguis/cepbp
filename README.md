# cepbp
General repos with examples on how to build a project: classes definition, set up tests set up. Allows me to quickly access a working example.

The code generates dimension metrics (perimeter, area), for different shapes (circle, rectangle). It is quite a simple problem and it can be used to illustrate a ton best practices and tricks.
Note that even best practices can vary from one team to the other. This example repo is more intended to illustrate the various packages and the most common features that developers use when they build packages. Everything is not perfect. Feel free to experiment and criticize!

Most of the code assume a Linux/Mac environment/machine. However, all the steps can be done in Windows as well.

# Virtual Environment

## Set up a virtual environment

While developing, it is highly recommended to work in a virtual environment. Install virtualenv and virtualenvwrapper:
```
pip install virtualenv virtualenvwrapper --user
```
In order to use virtualenvwrapper, you must source the executable. To do so automatically, locate **virtualenvwrapper.sh** (usually in */usr/local/bin/virtualenvwrapper.sh* or */home/<your_directory_name>/.local/bin/*) and update your **.bashrc** file by adding this line at the end:
```
source <path_to_virtualenvwrapper.sh>
```
Note, if you cannot find it, execute this in your terminal (if installed in your home directory. Update the root path otherwise):
```
find ~/ -type f -name "virtualenvwrapper.sh"
```
Exit and source your **.bashrc** `source ~/.bashrc` or close re-open your terminal.

Now we can create our own virtual environment! Move into your local repo, for which you want to create an environment and execute:
```
mkvirtualenv cepbp
```
You should have a brand new virtual environment. You can see that you are in the virtual environment by looking at the path in your terminal. You should see *(cepbp)*. All python libraries that we will install will be defined only within this environment and will not be accessible from outside.

Note, to exit the environment, type:
```
deactivate
```
To start an exisiting environment:
```
workon <environment name>
```

Copy the repo into an appropriate location:
```
git clone ssh://git@adlm.nielsen.com:7999/~foda8001/cepbp.git
```

More information: [https://docs.python-guide.org/dev/virtualenvs/]

## Installing packages in your virtual environment

### Regular pip install

In order to let other developers know what packages are need for your project, a requirement file is needed. Pip can install all of the packages referenced in *requirements.txt* by executing:
```
pip install -r requirements.txt
```
Note that if you want to install packages/repos directly from bitbucket, you can do it by using the same url given to clone the repo and you can specify a given branch, like so:
```
pip install git+https://github.com/Dirguis/cepbp@master
```
However, this is intended if you are not actively developing the package.

### Makefiles

One can write a Makefile as well, in order to streamline some of the most important operations to help developers get started. For example, the Makefile could contain a section to automatically run pip on the requirements.txt file. That specific command could be called *init* and be activated by running in the terminal:
```
make init
```
*make* will run any file named *Makefile* in the directory. Makefiles are general files that can run all sorts of command. It can be particularly useful to clean up a directory from compiled files, or execute tests.

# Running the code

To execute the script in python run:
```
from cepbp.dimension_calculator import DimensionCalculator
dc = DimensionCalculator('data_science', submitted_by='tester')
dc.output_dimension_value((3.0, 12.0), 'rectangle', 'perimeter')
```
You should see printed text and the perimeter value returned:
```
Request submitted by tester
Request submitted by group data_science
rectangle perimeter: 30.000
Out[5]: 30.0
```

# Code organization

## Architecture

```bash
.
├── cepbp
│   ├── areas
│   │   ├── areas.py
│   │   └── __init__.py
│   ├── common
│   │   ├── custom_error_handler.py
│   │   ├── __init__.py
│   │   ├── input_testing.py
│   │   ├── logs.py
│   │   └── pick_dimension.py
│   ├── dimension_calculator.py
│   ├── __init__.py
│   └── perimeters
│       ├── __init__.py
│       └── perimeters.py
├── LICENSE
├── Makefile
├── README.md
├── requirements.txt
├── setup.py
└── tests
    ├── context.py
    ├── test_data.json
    └── tests.py

```
The code is organized into a distribution package, in which you will find all the necessary information to distribute your code and the project itself which would be *cepbp* in our case.

## Distribution files

- *LICENCE*: To legally protect your code ([https://docs.python-guide.org/writing/license/])
- *Makefile*: Automate some basic tasks like installing all the requirements, cleaning the folder from execution files, or start a test on your code
- *README.md*: Empowers people to decrypt your intentions without, hopefully, guessing too much
- *requirements.txt*: List all the other packages that your code needs in order to run. That list is referenced at installation time, to install the needed packages along with yours
- *setup.py*: Master module to distribute and allow others to install our package
- *tests*: package with standard testing code
- *cepbp*: This is where your code is being developed

For more information about the structure of a distributed package, please refer to [https://docs.python-guide.org/writing/structure/]

## Modules and packages

The code should be organized into modules (python files), themselves organized into packages (folders with python modules and a *__init__.py* file). When a package is called, the *__init__.py* is called and executed. Typically, the *__init__.py* can be left empty (and it is even good practice in general). One can make use of it to simplify the calls to these functions or classes directly from the parent directory. For example, when I call **perimeters**, the *__init__.py* automatically loads the class **Perimeters**: `from perimeters import Perimeters`. Therefore, I can now call that class from the master module like so:
```
from perimeters import Perimeters
# instead of:
# from perimeters.perimeters import Perimeters
```
This should be done only if it does not add any confusion to the code. If so, default to explicitly reference the class by its full path.

# Logging

In order to monitor the execution of your code and record interesting results, or errors to identify issues, it is important to log information in an automatic way. Python provides the package **logging** [https://docs.python.org/3/library/logging.html].

## Customize your loggers

When you define a logger, however, the package creates a singleton. That means that only one version of an instance can exist and be created. That has the annoying property of printing your logged message n times if you tried to define your logger n times, if you develop in a notebook for example. In order to do that, I typically wrap the logging package into a custom class in which I can define the logs format, to make sure that I will not re-instantiate the log object if it already exists. I can as well make sure that the messages will print both in the terminal and in a file. The code is located at *cepbp/common/logs.py*.

## Customize your error messages

Another useful way of making code robust, is to properly catch errors and create a meaningful error message. It can be really useful to add to the error message the data that caused the error. To do that, one can create a customized error handler that will print the error and selected data in the log file for example. The code in *cebpb/common/custom_error_handler.py* does just that. It simply allows to pass a message and data through an Exception raised.

# Testing

Testing is typically overlooked when data scientists develop. However, it is an essential part of building robust packaging, ensuring that the code meets some standards at every step of the development process. Python provides a nice package for that task: pytest [https://docs.pytest.org/en/latest/]. The test code should live in a separate folder, at the top level. As long as the tests are defined in functions starting with *test_*, pytest will automatically find them and will call the functions. The functions can be successions of assertions.
Note that in *tests/tests.py*, the package *cepbp* is called using an extra file *context.py*. This is just an interface to make sure that the package is loaded successfully in all situations.
The tests can be initiated by executing the Makefile like so:
```
make tests
```

# General recommendation

## Use standard when you code

- It generally appreciated that people default to the same code formatting. One great way to do that is to use pycodestyle (`pip install pycodestyle`) with any python IDE such as pycharm or Atom. You can generally install packages on your IDE, that will check your code and make sure you conform to the best practices. In Atom, you can use **linter-pycodestyle** for example (I personally suppressed these warnings though: E501, W503 (see [http://pycodestyle.pycqa.org/en/latest/intro.html] for more information))
- Keep packages and modules names short, lowercase and possibly without underscore unless it improves readability. Class names follow the CapWords convention. More information here: [https://www.python.org/dev/peps/pep-0008/#package-and-module-names]
- Document all your functions and classes. One nice way to do that is to follow the numpy docstring conventions: [https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html]
- Be as explicit as you can when you name variables
- Do not reuse name variables, especially if the data changes its nature (string -> dataframe for example)
- when you import packages/modules, always use the explicit path, referenced from the top folder of your project (ex: **from cepbp.common.logs import Logs**). That will save you a lot of headaches with improper references modules and packages.
- When you import packages/modules, never blindly import everything (**from numpy import \***) because it will potentially interfere with other functions. Instead, always import the package/module and use its name or an alias (**import numpy as np**)
