
from gpiozero import Button
from subprocess import Popen
from time import sleep

player = None
#Each of these correspond to one button on my saxophone. The number inside of Button() is what GPIO the data from the button goes into
button1 = Button(2)
button2 = Button(3)
button3 = Button(4)
button4 = Button(5)
button5 = Button(6)
button6 = Button(7)
button7 = Button(8)
button8 = Button(9)
button9 = Button(10)
button10 = Button(11)
button11 = Button(12)
button12 = Button(13)
button13 = Button(14)
button14 = Button(18)
octave = Button(16)
current_note = None

while True:

        if (not button1.is_pressed and not button2.is_pressed and not button3.is_pressed and not button4.is_pressed and
        not button5.is_pressed and not button6.is_pressed and not button7.is_pressed and not button8.is_pressed and
        button9.is_pressed and button10.is_pressed and not button11.is_pressed and not button12.is_pressed and
        not button13.is_pressed and not button14.is_pressed and octave.is_pressed):
                note = "/home/pi/DE_Project_Audio/358403-mtg-sax-alto-d5#_x0TBG9IW.wav"
                #play high d sharp
        elif (not button1.is_pressed and not button2.is_pressed and not button3.is_pressed and not button4.is_pressed
        and not button5.is_pressed and not button6.is_pressed and not button7.is_pressed and not button8.is_pressed
        and not button9.is_pressed and button10.is_pressed and not button11.is_pressed and not button12.is_pressed and
        not button13.is_pressed and not button14.is_pressed and octave.is_pressed):
                note = "/home/pi/DE_Project_Audio/358402-mtg-sax-alto-d5_pTOlFqru.wav"
                #play high d 
#       elif (not button1.is_pressed and not button2.is_pressed and not button3.is_pressed and not button4.is_pressed
#       and not button5.is_pressed and not button6.is_pressed and not button7.is_pressed and not button8.is_pressed
#       and not button9.is_pressed and not button10.is_pressed and not button11.is_pressed and not button12.is_pressed
#       and not button13.is_pressed and not button14.is_pressed and octave.is_pressed):
#               note = "/home/pi/DE_Project_Audio/358401-mtg-sax-alto-c5#_Zie35Gk0.wav"
                #play high c sharp
        elif (not button1.is_pressed and button2.is_pressed and not button3.is_pressed and not button4.is_pressed
        and not button5.is_pressed and not button6.is_pressed and not button7.is_pressed and not button8.is_pressed
        and not button9.is_pressed and not button10.is_pressed and not button11.is_pressed and not button12.is_pressed
        and not button13.is_pressed and not button14.is_pressed and octave.is_pressed):
                note = "/home/pi/DE_Project_Audio/358400-mtg-sax-alto-c5_4cQrVbaI.wav"
                #play high c
        elif (button1.is_pressed and not button2.is_pressed and not button3.is_pressed and not button4.is_pressed and
        not button5.is_pressed and not button6.is_pressed and not button7.is_pressed and not button8.is_pressed and
        not button9.is_pressed and not button10.is_pressed and not button11.is_pressed and not button12.is_pressed and
        not button13.is_pressed and not button14.is_pressed and octave.is_pressed):
                note = "/home/pi/DE_Project_Audio/358399-mtg-sax-alto-b4_a15xLMt3.wav"
                #play high b
      elif (button1.is_pressed and button2.is_pressed and not button3.is_pressed and not button4.is_pressed and
        not button5.is_pressed and not button6.is_pressed and not button7.is_pressed and not button8.is_pressed and
        not button9.is_pressed and not button10.is_pressed and not button11.is_pressed and not button12.is_pressed and
        not button13.is_pressed and not button14.is_pressed and octave.is_pressed):
                note = "/home/pi/DE_Project_Audio/358397-mtg-sax-alto-a4_e1DKhJZV.wav"
                #play high a
        elif (button1.is_pressed and button2.is_pressed and button3.is_pressed and not button4.is_pressed and not
        button5.is_pressed and not button6.is_pressed and not button7.is_pressed and not button8.is_pressed and not
        button9.is_pressed and not button10.is_pressed and not button11.is_pressed and button12.is_pressed and not
        button13.is_pressed and not button14.is_pressed and octave.is_pressed):
                note = "/home/pi/DE_Project_Audio/358396-mtg-sax-alto-g4#_BPyCxexH.wav"
                #play high g sharp
        elif (button1.is_pressed and button2.is_pressed and button3.is_pressed and not button4.is_pressed and
        not button5.is_pressed and not button6.is_pressed and not button7.is_pressed and not button8.is_pressed and not
        button9.is_pressed and not button10.is_pressed and not button11.is_pressed and not button12.is_pressed and
        not button13.is_pressed and not button14.is_pressed and octave.is_pressed):
                note = "/home/pi/DE_Project_Audio/358395-mtg-sax-alto-g4_yd5ZnfLe.wav"
                #play high g

        elif (button1.is_pressed and button2.is_pressed and button3.is_pressed and not button4.is_pressed and
        button5.is_pressed and not button6.is_pressed and not button7.is_pressed and not button8.is_pressed and not
        button9.is_pressed and not button10.is_pressed and not button11.is_pressed and not button12.is_pressed and not
        button13.is_pressed and not button14.is_pressed and octave.is_pressed):
                note = "/home/pi/DE_Project_Audio/358394-mtg-sax-alto-f4#_A6kSAW4a.wav"
                #play f sharp
        elif (button1.is_pressed and button2.is_pressed and button3.is_pressed and button4.is_pressed and not
        button5.is_pressed and not button6.is_pressed and not button7.is_pressed and not button8.is_pressed and not
        button9.is_pressed and not button10.is_pressed and not button11.is_pressed and not button12.is_pressed and not
        button13.is_pressed and not button14.is_pressed and octave.is_pressed):
                note = "/home/pi/DE_Project_Audio/358393-mtg-sax-alto-f4_FmPFEpWn.wav"
                #play f
        elif (button1.is_pressed and button2.is_pressed and button3.is_pressed and button4.is_pressed and button5.is_pressed
        and not button6.is_pressed and not button7.is_pressed and not button8.is_pressed and not button9.is_pressed and
        not button10.is_pressed and not button11.is_pressed and not button12.is_pressed and not button13.is_pressed and
        not button14.is_pressed and octave.is_pressed):
                note = "/home/pi/DE_Project_Audio/358392-mtg-sax-alto-e4_UouVpUPe.wav"
                #play e
        elif (button1.is_pressed and button2.is_pressed and button3.is_pressed and button4.is_pressed and button5.is_pressed
        and button6.is_pressed and button7.is_pressed and not button8.is_pressed and not button9.is_pressed and not
        button10.is_pressed and not button11.is_pressed and not button12.is_pressed and not button13.is_pressed and not
        button14.is_pressed and octave.is_pressed):
                note = "/home/pi/DE_Project_Audio/358391-mtg-sax-alto-d4#_22Uk8s9D.wav"
                #play d sharp
        elif (button1.is_pressed and button2.is_pressed and button3.is_pressed and button4.is_pressed and button5.is_pressed
        and button6.is_pressed and not button7.is_pressed and not button8.is_pressed and not button9.is_pressed and not
        button10.is_pressed and not button11.is_pressed and not button12.is_pressed and not button13.is_pressed and not
        button14.is_pressed and octave.is_pressed):
                note = "/home/pi/DE_Project_Audio/358390-mtg-sax-alto-d4_fJULps1p.wav"
                #play d
#       elif (not button1.is_pressed and not button2.is_pressed and not button3.is_pressed and not button4.is_pressed and
#       not button5.is_pressed and not button6.is_pressed and not button7.is_pressed and not button8.is_pressed and not
#       button9.is_pressed and not button10.is_pressed and not button11.is_pressed and not button12.is_pressed and not
#       button13.is_pressed and not button14.is_pressed and not octave.is_pressed):
#               note = "/home/pi/DE_Project_Audio/358389-mtg-sax-alto-c4#_q73ubJBp.wav"
                #play c sharp
        elif (not button1.is_pressed and button2.is_pressed and not button3.is_pressed and not button4.is_pressed and
        not button5.is_pressed and not button6.is_pressed and not button7.is_pressed and not button8.is_pressed and not
        button9.is_pressed and not button10.is_pressed and not button11.is_pressed and not button12.is_pressed and not
        button13.is_pressed and not button14.is_pressed and not octave.is_pressed):
                note = "/home/pi/DE_Project_Audio/358388-mtg-sax-alto-c4_vFER2BH4.wav"
                #play c
   
        elif (button1.is_pressed and not button2.is_pressed and not button3.is_pressed and not button4.is_pressed and
        not button5.is_pressed and not button6.is_pressed and not button7.is_pressed and not button8.is_pressed and not
        button9.is_pressed and not button10.is_pressed and not button11.is_pressed and not button12.is_pressed and not
        button13.is_pressed and not button14.is_pressed and not octave.is_pressed):
                note = "/home/pi/DE_Project_Audio/358387-mtg-sax-alto-b3_S66Ojgvd.wav"
                #play b
        elif (button1.is_pressed and button2.is_pressed and not button3.is_pressed and not button4.is_pressed and
        not button5.is_pressed and not button6.is_pressed and not button7.is_pressed and not button8.is_pressed and not
        button9.is_pressed and not button10.is_pressed and not button11.is_pressed and not button12.is_pressed and not
        button13.is_pressed and not button14.is_pressed and not octave.is_pressed):
                note = "/home/pi/DE_Project_Audio/358385-mtg-sax-alto-a3_i1rHvoT0.wav"
                #play a
        elif (button1.is_pressed and button2.is_pressed and button3.is_pressed and not button4.is_pressed and
        not button5.is_pressed and not button6.is_pressed and not button7.is_pressed and not button8.is_pressed and not
        button9.is_pressed and not button10.is_pressed and not button11.is_pressed and button12.is_pressed and not
        button13.is_pressed and not button14.is_pressed and not octave.is_pressed):
                note = "/home/pi/DE_Project_Audio/358384-mtg-sax-alto-g3#_WXODsdIb.wav"
                #play g sharp
        elif (button1.is_pressed and button2.is_pressed and button3.is_pressed and not button4.is_pressed and
        not button5.is_pressed and not button6.is_pressed and not button7.is_pressed and not button8.is_pressed and not
        button9.is_pressed and not button10.is_pressed and not button11.is_pressed and not button12.is_pressed and not
        button13.is_pressed and not button14.is_pressed and not octave.is_pressed):
                note = "/home/pi/DE_Project_Audio/358383-mtg-sax-alto-g3_zm3yWkAE.wav"
                #play g
        elif (button1.is_pressed and button2.is_pressed and button3.is_pressed and not button4.is_pressed and
        button5.is_pressed and not button6.is_pressed and not button7.is_pressed and not button8.is_pressed and not
        button9.is_pressed and not button10.is_pressed and not button11.is_pressed and not button12.is_pressed and not
        button13.is_pressed and not button14.is_pressed and not octave.is_pressed):
                note = "/home/pi/DE_Project_Audio/358382-mtg-sax-alto-f3#_ksCzpstd.wav"
                #play low f sharp
        elif (button1.is_pressed and button2.is_pressed and button3.is_pressed and button4.is_pressed and
        not button5.is_pressed and not button6.is_pressed and not button7.is_pressed and not button8.is_pressed and not
        button9.is_pressed and not button10.is_pressed and not button11.is_pressed and not button12.is_pressed and not
        button13.is_pressed and not button14.is_pressed and not octave.is_pressed):
                note = "/home/pi/DE_Project_Audio/358381-mtg-sax-alto-f3_nJ5BS97z.wav"
                #play low f

        elif (button1.is_pressed and button2.is_pressed and button3.is_pressed and button4.is_pressed and
        button5.is_pressed and button6.is_pressed and button7.is_pressed and not button8.is_pressed and not
        button9.is_pressed and not button10.is_pressed and not button11.is_pressed and not button12.is_pressed and not
        button13.is_pressed and not button14.is_pressed and not octave.is_pressed):
                note = "/home/pi/DE_Project_Audio/358379-mtg-sax-alto-d3#_EuCeDEWj.wav"
                #play low d sharp
        elif (button1.is_pressed and button2.is_pressed and button3.is_pressed and button4.is_pressed and
        button5.is_pressed and button6.is_pressed and not button7.is_pressed and not button8.is_pressed and not
        button9.is_pressed and not button10.is_pressed and not button11.is_pressed and not button12.is_pressed and not
        button13.is_pressed and not button14.is_pressed and not octave.is_pressed):
                note = "/home/pi/DE_Project_Audio/358378-mtg-sax-alto-d3_IobP6hiC.wav"
                #play low d
        elif (button1.is_pressed and button2.is_pressed and button3.is_pressed and button4.is_pressed and
        button5.is_pressed and button6.is_pressed and not button7.is_pressed and button8.is_pressed and not
        button9.is_pressed and not button10.is_pressed and not button11.is_pressed and not button12.is_pressed and
        button13.is_pressed and not button14.is_pressed and not octave.is_pressed):
                note = "/home/pi/DE_Project_Audio/358377-mtg-sax-alto-c3#_lDEQIu8h.wav"
                #play low c sharp
        #Else statement makes it so when no note is being played, we change note to none so that we can tell the pi to stop playing any noise
        else:
                note = None
        #This if statement basically checks to see if we switched a note. If we did, it stops whatever audio we were playing if it was on and play a note
        if note is not current_note:
                if player is not None:
                        player.kill()
                        player = None
                if note is not None:
                        player = Popen(["aplay", "--duration=2", note])
                current_note = note
        #This if statement makes it so that if we keep holding on one button, it'll make sure to keep on repeating everytime the audio is finished
        if note is not None and note is current_note:
                if player is None and player.poll() is not None:
                        player = Popen(["aplay", "--duration=2", note])
        sleep(0.01)
