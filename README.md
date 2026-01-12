# DE-Final-Project-Alto-Saxophone-
This is the GitHub repository for all the code that is needed for my Alto Saxophone final project

**About My Project**

The goal of my project is to essentially replicate an actual saxophone for the fraction of the price. Since normal saxophones can cost over $3000, I wanted to make one myself to use. With this project, people will be able to make demo saxophones that is a lot cheaper than actual saxophones.

**Libraries Used For Project**
- GPIOZero 
- Subprocess
- Time

**Code Flow Chart**
<img width="1422" height="1033" alt="Screenshot 2026-01-12 115935" src="https://github.com/user-attachments/assets/210f1af7-ae53-47a5-828e-faf88a5d6390" />
This is my code in a flow chart form. This flow chart is only when a button is being pressed. It first gets the combination of buttons that are being pressed and not being pressed and turns that into a note. Before it plays the note, it first checks if there is already another note playing. If there is, it checks if that note is the same note as the one we got from our combination. If they're the same, it does nothing and just let the note keep playing. If they're not the same, it stops the current audio from playing and starts playing the new note. If there is no note being played, it just plays the audio for the new note. 
