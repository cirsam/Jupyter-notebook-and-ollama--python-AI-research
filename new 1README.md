**connect jupyter notebook to llama to access any AI model**
__setup steps__

1.go to python.org and download python3 and install it on your machine
open commandline application or terminal 

2. to ensure python is installed and working. run python--version and you should get somthing like python 3.x.x
3. check to see if pip is also installed and working. the latest python download comes with pip

4. to make sure pip is working run python -m ensurepip --upgrade in the terminal

5.before you create your virtual environment.create your working directory or folder. That is were you will install your virtual environment

6.nagate to your work folder in the terminal. like cd path\to\your\workfolder.
  create your virtual environment.  by runing python -m venv .venv
  
  7. now open your work folder you will see a dirctory called .venv. open it
  
  8. activate your environment by running .venv\Scripts\activate.bat in your terminal make sure you are in your path\to\your\workfolder
  
9. befor you activate your environment you will see C:\path\to\your\workfolder>

10. after you activate your environment. you will see

(.venv)C:\path\to\your\workfolder>
11. now install jupyter notebook.by running pip install jupyter notebook

12. start the jupyter notebook server by running jupyter notebook

13. you can install jupyter lab if you want by running pip install jupyterlab

14.you can lunch the lab by running jupyter lab as well.
now
**install ollama**

1.go to ollama .com and download the one for windows and insall it.

2. go to your searcharea next to the start icon and type ollama. click on the app. it will open the ollama terminal

3. start theollama server by runing ollama serve 

4. pull which ever model you want by running ollama pull modelName. where modelName is like claude code.

5. find more models here https://ollama.com/library?sort=newest  and pull which ever one you want .
  