<div align="center">
<img width="30%" src="https://user-images.githubusercontent.com/72341453/134747028-7e2d90cc-a92f-4f66-815e-54a0d50cca54.PNG">

# StudyBuddy
</div>

### Using Docker
--> Pull the docker image
```bash
docker pull ayushmodi/studybud:latest
```

--> Build the image
```bash
docker build --build-arg GIT_REPO_URL=https://github.com/AyushModi123/StudyBud.git --build-arg GIT_BRANCH=main -t my_django_app . 
```

--> Run the container
```bash
docker run -p 8000:8000 my_django_app
```
#

### Cloning the repository

--> Clone the repository using the command below :
```bash
git clone https://github.com/AyushModi123/StudyBud.git

```

--> Move into the directory where we have the project files : 
```bash
cd StudyBud

```

--> Create a virtual environment :
```bash
# Let's install virtualenv first
pip install virtualenv

# Then we create our virtual environment
virtualenv envname

```

--> Activate the virtual environment :
```bash
envname\scripts\activate

```

--> Install the requirements :
```bash
pip install -r requirements.txt

```

#

### Running the App

--> To run the App, we use :
```bash
python manage.py runserver

```

> ⚠ Then, the development server will be started at http://127.0.0.1:8000/

#

### App Preview :

<table width="100%"> 
<tr>
<td width="50%">      
&nbsp; 
<br>
<p align="center">
  Feed Home
</p>
<img src="https://github.com/AyushModi123/StudyBud/assets/99743679/6de00a06-e9e5-48cd-88d7-5b8e27461490">
</td> 
<td width="50%">
<br>
<p align="center">
  Room Conversation Preview
</p>
<img src="https://user-images.githubusercontent.com/72341453/134747155-3ca5b55f-b064-4741-aeae-abe90bddf41e.PNG">  
</td>
</table>


