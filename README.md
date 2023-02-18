# Task 2 - Semantic Similarity

This project applies SpaCy - a Python NLP library - to recommend the movie to watch next based on the film desciptions and desciption of Planet Hulk.

## Installation <a name="installation"/>

There is aa very easy way to run this program on your computer, i.e., Using my online Docker image.


### Using Docker image

- Download and install [Docker](https://www.docker.com/products/docker-desktop/). You may need to update your Linux as well, when the demand prompted.

- To confirm if you successfully install Docker, run this command in your CP:

```bash
docker run hello-world
```

- With the Docker app opened, run this code in your CP:

```bash
docker run andrewthien/semantic2
```

- When finished, you should see the out come of this program, similar to the picture in usage section.

### Note: please read the Usage section for more details


## Table of Contents
### 1. [Installation](#installation)
### 2. [Usage](#usage)
### 3. [Contributing](#contributing)
### 4. [Credits](#credits)


## Usage <a name="usage"/>

#### The program can be used to analyse and perform similarity checking between a film description (Planet Hulk) and 10 other movies, then point out which movie should be watched next after Planet Hulk.
#### After running the project, you should see the outcome as below. When the input is the description of Planet Hulk, Spacy recommends Movie C, which has the highest similarity with the input.


![screenshot](Screenshot.png "screenshot")


## Contributing <a name="contributing"/>

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Credits <a name="credits"/>

[Tri Thien Nguyen](https://www.linkedin.com/in/tri-thien-nguyen/)
