# disco
<p align="center"><img src="https://github.com/felipeserna/disco/blob/main/Images/robot_at_piano.jpg" /></p>
<br>

Machine Learning Portfolio Project by Javier Charria, Andrew Kalil, Felipe Serna, and Diego Vivius. Project developed for Holberton School.

The user will experience the joy of listening to songs created by a machine and not by humans. The idea is that the user can listen to classical music that actually sounds like music: a coherent sequence of notes similar to a sequence played by professional musicians.

MIDI files have a lot of events such as note-on, note-off, time shift, bar, track, and so on. We will only focus on two main events, note-on and note-off. The MIDI format captures 16 channels (numbered 0 to 15), 128 notes, and 128 loudness settings (also called velocity).

## Libraries, frameworks and APIs
* music21<br>

Music21 is a Python-based toolkit for computer-aided musicology. It is used for loading and processing MIDI files in Python.<br>

People use music21 to answer questions from musicology using computers, to study large datasets of music, to generate musical examples, to teach fundamentals of music theory, to edit musical notation, study music and the brain, and to compose music (both algorithmically and directly). Many MIDI files have multiple instruments in their music. In our dataset, the MIDI files only contains one instrument, which is Piano. We will extract the notes from the piano instruments.<br>

* Keras<br>

API from TensorFlow for building and training Machine Learning models.

## Generative Models
Unique challenges of generative models:
A more subtle problem that comes from having complex data, and the fact that we are trying to generate data rather than a numerical label or value, is that our notion of model **accuracy** is much more complicated: we cannot simply calculate the distance to a single label or scores.

## Installation and Usage
Using Colab:
By default all the libraries that we use are already installed in Colab.

Go to [Models](https://github.com/linkjavier/disco/tree/main/models) and copy the Jupyter Notebook in Colab.

Go to [Datasets](https://github.com/linkjavier/disco/tree/main/Datasets) and download the dataset you want to use.

Upload your dataset to [Google Drive](https://drive.google.com/)

To connect Colab to Google Drive this [link](https://www.marktechpost.com/2019/06/07/how-to-connect-google-colab-with-google-drive/) may help.

In the line
```
!unzip '/content/drive/MyDrive/your_dataset.zip'
```
copy the dataset you uploaded to Google Drive.

In the line
```
data_dir = 'your_dataset'
```
do the same as above but without the *.zip extension.

Run the Colab notebook.

A MIDI file will be generated.

## Authors:
Felipe Serna <1509@holbertonschool.com>

[LinkedIn profile](https://www.linkedin.com/in/felipesernabarbosa/)

Diego Vivius <vandeldiegoc@gmail.com>

[LinkedIn profile](https://www.linkedin.com/in/diego-vivius)

Javier Charria <javiercharria@gmail.com>

[LinkedIn profile](https://www.linkedin.com/in/javier-charria-76760764/)

Andrew Kalil <andrew_kalil@hotmail.com>

[LinkedIn profile](https://www.linkedin.com/in/andrewkalil/)
