'''
virtualenv env helps to create isolated Python environments. It allows you to manage dependencies for different projects separately, preventing conflicts between them. When you create a virtual environment, it includes its own Python interpreter and can have its own set of installed packages. This is particularly useful when working on multiple projects that require different versions of libraries or when you want to avoid installing packages globally on your system. By activating the virtual environment, you can ensure that your project
'''

'''
python -m venv env is a command used to create a virtual environment named "env" using the built-in venv module in Python. This command sets up a new directory called "env" that contains a copy of the Python interpreter and a separate location for installing packages. After running this command, you can activate the virtual environment and install project-specific dependencies without affecting the global Python installation on your system.

.\env\Scripts\activate is the command used to activate the virtual environment created with python -m venv env. When you run this command, it modifies your shell's environment variables to point to the Python interpreter and installed packages within the "env" directory. This allows you to work within the isolated environment, ensuring that any packages you install or use are specific to that environment and do not interfere with other projects or the global Python installation on your system.

if you 
    + CategoryInfo          : SecurityError: (:) [], PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess

this error we use this Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

deactivate is the command used to exit or deactivate the currently active virtual environment. When you run this command, it restores your shell's environment variables to their original state, allowing you to return to the global Python environment or switch to another virtual environment if needed. This is useful when you have finished working on a project within a virtual environment and want to return to your default Python setup.


pip freeze requirements.txt is a command used to generate a list of all the installed packages and their versions in the current Python environment and save it to a file named requirements.txt. This file can then be used to recreate the same environment on another machine or share it with others. By running pip freeze > requirements.txt, you can capture the exact dependencies of your 
project, making it easier to manage and reproduce the environment in the future.
i have to be inside the virtual environment to run this command otherwise it will capture the global packages which may not be relevant to the project.

pip install -r requirements.txt is a command used to install all the packages listed in the requirements.txt file. This file typically contains a list of package names and their specific versions that are required for a project. By running pip install -r requirements.txt, you can quickly set up the necessary dependencies for your project in your current Python environment, ensuring that you have the correct versions of the packages installed as specified in the requirements file.







'''
