# Frequency of PWM

## 1 Context
Certain digital output pins can be configured to produce a pulse width modulated (PWM) signal. 
That is a periodic signal where a digital number is translated to some fraction of the time where the signal is high.

Both types of IoT devices have serial light sensors and LEDs. The LEDs can be driven by PWM.

Your light sensors are not wast enough to capture a PWM signal. 
In this exercise we imagine that they are.

## 2 Exercise
What is the real frequency of a PWM signal?

Subquestions:
 - How would you construct an experimental setup for measuring this?
 - What are the stumbling blocks?
 - What would you expect to see?


## 3 Recipe
1. Find the documentation of your PWM engine (it is a part of your microcontroller).
2. Find the documentation of your UART (this is the serial port which is part of your microcontroller).
3. Evaluate potential for capturing the PWM signal with the light sensor.
4. Find a solution to the limitation(s).
5. Design an experimental setup for answering the questions.