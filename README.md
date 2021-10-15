
# Music and Induced Emotion
## What factors are more likely to influence induced emotions while listening to music that is likely unfamiliar?

Music can be composed with the intent to express certain emotions. It may be straightforward enough to say that a song written with lyrics about love and happiness expresses happiness, or that a song written about loss expresses sadness, perhaps a song written in a minor key is meant to express sadness or grief.  What happens though when listening to the aforementioned pieces you experience agitation instead of happiness? Perhaps the saddest song (lyrics wise) brings you peaceful happy feelings.  A song that is meant to express anger may make you feel energized and happy. 

I am specifically interested in exploring what is it about music that makes us feel certain emotions, regardless of its intended expression.
***
## Executive Summary:

### Project Goal: What features of randomly played music will induce emotions of vitality (labeled "energized"?

### Key Findings: A Random Forest Classifier performed the best across the train, validate and test data sets. (Roughly 75% for all three, beating baseline accuracy by 12%) I discovered through EDA and a simple Logistic Regression model that the most important features for inducing energized emotions while listening to randomly played tracks, are: liking the song, having a fast tempo (108-156 BPM) and being classical in genre. 

### Summary/Future Iterations: 
Even though through the Logistic Regression model we found that there are features that do hold higher importance to others, it is clear there is still a blindspot in what combination of features actually will yield the greatest accuracy. Running a Logistic Regression model with only the most important features yielded a result about the same as baseline accuracy of 63%.  With more time, I'd like to explore more combinations of features. One thing that stands out to me by far is that classical music is the only genre where a song may be somewhat familiar to the listener. This is an aspect of data preparation I'd like to further investigate and model on. 
#### I plan to continue this project to predict influencers of other emotions as well. 

### It is my hope that this project will be useful in increasing human productivity, focus, mental well being, and improving various social, consumer and workplace experiences.

***

#### A few notes about the data: 
Data Sources: http://www2.projects.science.uu.nl/memotion/emotifydata/
Reference: A. Aljanaki, F. Wiering, R. C. Veltkamp. Studying emotion induced by music through a crowdsourcing game. Information Processing & Management, 2015.

The data set I'm using is collected from results of a gamified survey once available online and on facebook. In addition to the results being available at the above link, all of the songs are also available.

Some additional notes from the above reference:

    -747 females, 1031 males were surveyed and asked to give thier gender, age, initial mood.
    -The feature Mood is a Likert scale from 1(very bad) to 5(very good).
    -While the participant listened to the music, they would select emotions they experienced.
        The GEMS categories were explained to each participant:
        Emotional category	Explanation	Superfactor
        Amazement∗	Feeling of wonder and happiness	Sublimity
        Solemnity∗	Feeling of transcendence, inspiration. Thrills
        Tenderness	Sensuality, affect, feeling of love
        Nostalgia	Dreamy, melancholic, sentimental feelings
        Calmness∗	Relaxation, serenity, meditativeness
        Power	Feeling strong, heroic, triumphant, energetic	Vitality
        Joyful activation	Feels like dancing, bouncy feeling, animated, amused
        Tension	Nervous, impatient, irritated	Unease
        Sadness	Depressed, sorrowful

There are 400 songs, 4 genres and 100 songs per genre.  The music is all in the public domain and can be accessed on magnatune.com. From the creators of the referenced published study: "The resulting dataset contains music from 241 different albums by 140 performers. There were several reasons to choose music from Magnatune: it is of good quality and it is generally little known (familiar music might precondition induced emotion (Schubert, 2007))."(Aljanki, 2015)

Because this music is both published and public domain, I was able to upload each blinded sound clip into an online application to retreive more information about each piece.
From this application (audiokeychain.com) I was able to create and export a csv that contains Track number, Song Title, Artist, Key, and BPM. 
***
#### Using the available datasets of responses per listen, track_ids, and the acquired song info from audiokeychain.com, I was able to create a dataframe containing the following data:

#### Each observation represents one listen of a single track.  
#### The features used for each observation are: 

    track_id: numbered 1-400. 1-100 are all classical, 101-200 are all electronic, 201-300 are all pop, and 301 to 400 are all rock. 
    genre_x: classical, electronic, pop, and rock.  Genres were all assigned by the publisher, magnatune.com 
    mood: listener reported mood. 1-5 scale, 1 is bad, 5 is great. 
    age: listener reported numeric age.
    gender: listener reported gender. M/F not given and published reports do not specify. 0/1 values instead.
    key: from audiokeychain.com, C, G, D, A, E, B, F, Gb, Db, Ab, Eb, Bb, Cm, Gm, Dm, Am, Em, Bm, Fm, Gbm, Dbm, Abm, Ebm, Bbm
    minor_key: feature engineered by grouping minor keys together and major keys together. 0 for major, 1 for minor. 
    tempo: loosely using standard tempo categories with appropriate subsets of the data: 0-90 BPM as slow, 91-108 as moderate, 108-156 as fast, and over 156 as very fast. tempo derived from audiokeychain.com
    liked: listener reported. listener did not have to report whether they liked the song, but could do so if they wished. 1: listener reported liked, 0: listener did not report liked.
    disliked: listener reported. listener did not have to report whether they disliked the song, but could do so if they wished. 1: listener reported disliked, 0: listener did not report disliked.
    feel_sublime: listener reported induced emotions. 1 for any instance or instances of the following emotions: amazement, inspiration, tenderness, nostalgia, calmness. 0 for none reported. 
    agitated: listener reported induced emotions. 1 for any instance of tension, irritation, impatience, sadness or depression. 0 for none reported. 
    energized: listener reported induced emotions. 1 for any instance or instances of power, triumph, energy, joyful activation, animated, amused.   
***
#### To recreate this project, please upload the datasets available the above link. You may access the csv file I created using audiokeychain.com here:https://drive.google.com/file/d/1ZhQLEZHZ6Q4eElMZTXGN9CJnMuYEbWbX/view?usp=sharing
#### Be sure to clone the final_notebook, acquire.py and explore.py modules.
