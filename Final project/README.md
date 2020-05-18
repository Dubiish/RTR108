# Circuit Simulator

- This is a final project for computer studies course
- Task is to build simple web circuit simulator using python as back-end and ngspice as simulator

## Solution

- I decided to use React as the main framework for front-end since I am already used to work in JavaScript fullstack
- For back-end I used Flask as the framework for simple API

### How it works

- User types input data in front-end form for voltage divider (or any other circuit)
- After submitting data are sent to python back-end where are processed and ran by NGSPICE simulator (Native on system, no python library was used for it)
- NGSPICE will spill some results and these are processed by server and sent in JSON format back to front-end where are displayed in results form

![Home_page](./Final project/pictures/home_page.PNG)

## Summary

- Front-end: React (Javascript) + Bootstrap CSS Framework (React integration)
- Back-end: Flask (Python)
- NgSpice simulator ran natively on linux ubuntu
