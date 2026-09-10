# Building

# poetry
https://www.twilio.com/en-us/blog/introduction-python-dependency-management-poetry-package#:~:text=are%20available%20here%20.-,Create%20a%20new%20project%20with%20Poetry,your%20project's%20configuration%20file%20(pyproject.


run server:
`poetry run python crud`
or
`poetry run python crud/__main__.py`

Maintainers should see [MAINTAINERS.md](MAINTAINERS.md).

Build and run:
```
docker build -t api . 
docker run -d -p 8088:3000 --name api api
```
Open `http://localhost:8088` in your browser.
