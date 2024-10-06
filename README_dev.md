# Setting up a Development Environment

>[!WARNING]
>The client uses Python >=3.8 (as per setup.py), but the development dependencies will complain if you're not using at least Python 3.8. We use Python 3.10.

We welcome contributions to make this project even better! To get started, follow the steps below:

### 1. Fork the Repository
Navigate to the project repository.
Click the Fork button at the top-right corner of the page to create your own copy of the repository.

### 2. Clone the Repository
Once you've forked the repository, clone it to your local machine:
```
git clone https://github.com/your-username/nocodb-python-client.git
cd nocodb-python-client
```
Once you cloned the repo, create a virtual environment
```
python -m venv venv
source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
```

### 3. Install Dependencies
To set up the development environment, install the required dependencies:
```
pip install -r requirements.txt
```

### 4. Create a New Branch
Before making any changes, create a new branch for your work:
```
git checkout -b your-branch-name
```

### 5. Make Your Changes
Now you're ready to make changes. Be sure to:
- Write clean, readable code.
- Follow any code style guidelines (such as PEP 8).


### 7. Commit and Push Your Changes
Once you're happy with your changes, commit them with a meaningful message:
```
git add .
git commit -m "Describe your changes"
git push origin your-branch-name
```
### 8. Submit a Pull Request
Navigate to the original repository and create a pull request:

- Go to the Pull Requests tab.
- Click New Pull Request.
- Select your branch and provide a description of the changes you've made.
- Submit the pull request for review.

### 9. Code Review
Once you submit a pull request, it will be reviewed by the maintainers. Be open to feedback, and feel free to discuss any changes that need to be made.

