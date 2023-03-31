# The purpose of this repository is to accomplish the following:

- [x] Learn more about FastAPI by spinning up a simple demo app.
    - [ ] Created a starter app, but the next step is to spin up an interactive demo app.
         - Create an endpoint that allows the user to perform the basic CRUD operations
            - [ ] **C**reate (post)
            - [ ] **R**ead   (get)
            - [ ] **U**pdate (put)
            - [ ] **D**elete (delete) 
- [ ] Instrument the demo app with the New Relic platform.
- [ ] Explain the purpose of the FastAPI demo app .
- [ ] Explain the meaning of instrumenting one app with another app.
- [ ] Describe how the demo app was successfully instrumented with the New Relic platform.
- [ ] What was learned throughout the process.



## Tools used
- MacBook.
- Visual Studio Code (VSCode).
- Installed the latest version of python3 from https://www.python.org/downloads/.
- Installed pip in the Terminal via `curl -o get-pip.py https://bootstrap.pypa.io/get-pip.py`, followed by `python3 get-pip.py`.
- Installed fastapi in the Terminal via `pip3 install fastapi`.


## Issues encountered and a resolution
- **Issue 1:** fastapi not being recognized in the editor. 
    - **Resolve:**
        1. Opening the command palette via the (`Ctrl` + `Shift` + `P`) command
        2. Typing and selecting **Python: Select Interpreter** w/the path pointing to my project folder
- The uvicorn command not being recognized when trying to run the python demo app due to its binaries not being in the Terminal PATH for it to be picked up. Instead, I was able to launch the app via `python3 -m uvicorn starter:app --reload`
~~- After exiting the uvicorn web server and closing the app in the browser, I changed the contents of the file and tried to reload the server. Unfortunately, I ran into the `No Module named uvicorn found` which could possibly be due to a deeper installation issue (initial speculation). I discovered this by running the `pip3 list` command in the terminal and didn't see either **fastapi** or **uvicorn** modules installed. *Will need to be resolved later.*~~
- **Issue 2:** When trying to `import png` into the the `steganography.py` file, the `Import "png" could not be resolve Pylance(reportMissingImports)` warning message was returned
    - **Resolve:**
        1. Searched for the error message and found a resolve on [stackOverflow](https://stackoverflow.com/questions/31142919/how-to-install-the-png-module-in-python) which instructed to do the following:
            a. Run `pip3 install pypng`
            b. The `import png` line of code should work

