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
<br/><br/>

**Fingering Diagram**
<img width="868" height="1157" alt="Screenshot 2026-01-12 120631" src="https://github.com/user-attachments/assets/e133d027-2dbf-4157-8930-bda101d7620b" />

This is a fingering chart for how to play each note on the alto saxophone. I referenced this image to use for my own saxophone. When a certain combination of buttons on this chart was hit, the note that corresponds to it would be played.

**How Playing Notes Work**

I can play the notes for my saxophone project depending on the buttons that are pressed. I have corresponded my 15 buttons on my project to 15 buttons on an actual saxophone. Then I have an if/elif statement for every note that I want added and have 15 different conditions inside each if/elif statement. Each condition refers to each of my 15 buttons and checks if they are on and off. I need to reference all 15 buttons as there are many notes where a certain combination of buttons overlap. It doesn't directly play the notes in each if statement, but sets a value of a variable called note to the audio file I want played. After it goes through all the if statements, then it goes through the logic I talked about in the code flow chart.

# Important Components to Saxophone
**Pressure Transducer**

<img width="855" height="512" alt="Screenshot 2026-01-12 12 46 07 PM" src="https://github.com/user-attachments/assets/f6d1ac8f-3558-4eb6-86c8-1ffb0f9e4709" />

Detects the amount of pressure that is being put onto it. This was meant to be used to detect the pressure of the air you are blowing into it, which would change the volume of the saxophone.

**Buttons**

<img width="396" height="394" alt="Screenshot 2026-01-12 12 56 01 PM" src="https://github.com/user-attachments/assets/773b182f-fc2b-4d99-8977-4ee4ffb4cf63" />

Detects when it is being pressed or not. This is used to act as a button on the saxophone. With a certain combination of buttons that are on and off, we can find what note that corresponds to on the actual saxophone and tell the code to play it.

# CAD Models

**Saxophone**
<img width="1419" height="1014" alt="Screenshot 2025-12-21 023828" src="https://github.com/user-attachments/assets/4e0f7da1-0fa3-4f73-99b1-bd48d5eeeac4" />

<br/><br/>
**Buttons**

<img width="869" height="557" alt="Screenshot 2026-01-12 171616" src="https://github.com/user-attachments/assets/80f89e27-b885-4ee1-ac0c-c79741ed2d3b" />

