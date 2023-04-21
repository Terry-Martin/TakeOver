# TakeOver
(Developer: Terry Martin)


[Live webpage](https://takeover-terry-martin.herokuapp.com/)

## Table Of Contents

1. [Project Goals](#project-goals)
    1. [Creator Goals](#creator-goals)
    2. [Player Goals](#player-goals)
2. [Game Info](#game-info)
    1. [Game Story](#game-story)
    2. [Game Basics](#game-basics)
    3. [Flow Chart](#flow-chart)
3. [User Experience](#user-experience)
    1. [Target Audience](#target-audience)
    2. [User Requrements and Expectations](#user-requirements-and-expectations)
    3. [User Stories](#user-stories)
4. [Design](#design)
    1. [Design Choices](#design-choices)
    2. [Colour](#colour)
5. [Technologies Used](#technologies-used)
    1. [Languages](#languages)
    2. [Frameworks and Tools](#frameworks-and-tools)
6. [Features](#features)
7. [Testing](#validation)
    1. [HTML Validation](#HTML-validation)
    2. [CSS Validation](#CSS-validation)
    3. [Accessibility](#accessibility)
    4. [Performance](#performance)
    5. [Device testing](#performing-tests-on-various-devices)
    6. [Browser compatibility](#browser-compatability)
8. [Bugs](#Bugs)
9. [Deployment](#deplyment)
10. [Credits](#credits)
11. [Acknowledgements](#acknowledgements)

## Project Goals

### Creator Goals
- Build a python project
- Create a game about taking over a town
- Allow user to input name and make selections based on story questions
- Give user a chance to complete game under certain conditions
- Display relevant info to user at correct time
- Two main battle types - Auto and Reaction time
- Final battle with change to Reaction time battle


### Player Goals
- Read story and options
- Enter name
- Virew foe info
- Make selections
- View current health
- Respond to reaction time battles
- CHance to defeat final boss
- Retry game after defeat

## Game Info

### Game story
- You are a born survivor and a seasoned warrior. Weary of seeing the corrupt politians and greedy landowners thrive on he back of your blood and sweat.
- No longer willing to take orders for pitiful payouts
- Its time to put your skills and charisma to the test and seat yourself at the top of the table.
- Determined to crush anyone that dares to stand in your way

### Game Basics
- User will see the intro screen with game name and then read short story intro
- User will then be giving a choice of two options (Decision Branch 1)
- One option will lead to an automatic battle against 3 foes
- The other option will lead to a reaction time battle. In this case, the user will need to press the Enter key when the word GO appears and hope their reaction time is faster than that set for foe
- User will lose health for each hit they take
- If health goes below zero at any stage of game, it will be game over. 
- User will then be giving a choice of two options (Decision Branch 2)
- This will run similar to options in first decision branch
- User will then be giving a choice of two options (Decision Branch 3)
- This will run similar to options in first decision branch except there is no reaction time battle
- User will then face a final battle. 
- This final battle is based on reaction time battle but user will have to count to seven seconds in their head after the trigger word and only then press enter. 
- If they press the Enter key between 6.5 to 7.5 seconds after trigger word, they win the battle and complete the game.
- Game will auto restart after it ends

### Flow Chart
![flow chart image](images/flowchart.jpg)

## User Experience

### Target Audience
The website is designed with the following target audience in mind:
- Project assessor
- Student peers
- People with an interest in python
- People who enjoy games
- People with a interest in adventure games
- People fed up with landlords

### User Requirements and Expectations
- Straight forward, easy to use interface
- Time to read and make selections
- Clear target to complete the game
- Retry game

### User Stories

#### Player
1. As a player, I want to start the game
2. As a player, I want to understand what the game is about
3. As a player, I want to be able to enter my name
4. As a player, i want to know how much health I have left
7. As a player, I want to receive acknowledment if i complete the game
8. As a player, I want to be able to play the game without any bugs

#### Creator
13. As the creator, I want showcase my abilities with python
14. As the creator, I want users to enjoy the game and have a interest in completing it
15. As the creator, I want users to be surprised by some of the game features
16. As the creator, I want the game to be bug free and capture/handle any likely user input errors

## Design

### Design Choices
The website was designed to be displayed with a custom/CI made python enviroemt that mimics a website.
pyfiglet and colorama were used to style and format the text

### Colour
Basic colours were chosen from those available through https://pypi.org/project/colorama/

## Technologies Used

### Languages
The following languages were used to develop the website:
- Python

### Frameworks and Tools
The following frameworks and tools were used to develop the website:
- Heroku
- Gitpod
- Google Sheets
- Colorama
- Pyfiglet
- Miro

## Features
The app is onone webpage

### Question, Answer and Submit for Missing Song Lyric Game

![balsamiq image](assets/images/readme_images/feature1.jpg)
- Displays 4 lines of a song. Each song has Dream theme to it
- It takes 8 songs to complete game. They are selected randomly from a bank of 25 question/answers.
- Questions/Answers are stored in an array. Songs sourced from Google. Questions are custom made
- Text of first question asked flashes on screen to draw user attention and direct their focus
- User is told how many letters there are in missing lyric word
- Answers can be typed in Input Box
- Answers will be accepted in lower and upper case

### Player Info

![balsamiq image](assets/images/readme_images/feature2.jpg)
- Displays users 4 stats with current score - Dreaminess, Comfort, Luck and Sleep Depth
- Dreaminess, Comfort and Luck are generated at the start of each game. Each stat score will start at a number between 70 to 90 (randomly decided)
- These 3 stats are combined to give an overall Sleep Depth score.
- User stats will increase/decrease depnding on answers given to Missing Song Lyric questions

### Sleep Info

![balsamiq image](assets/images/readme_images/feature3.jpg)
- Displays a progress bar (circle) that highlights the numer of hours sleep the user has achived so far
- This increments by one hour each question answered, regardless if the answer given was correct or incorrect
- Each hours sleep costs the user 10 points of each stat
- Target of 8 hours is shown. If user reaches this target they complete the game
- Sleep Depth stat score shows in green when it is high, changes to yellow when in mid range and red when score is low

### Player Items

![balsamiq image](assets/images/readme_images/feature4.jpg)
- This area starts the game blank as user has zero items 
- Items can be found randomly when users answer a question. The chances of finding an item are 1 in 8
- There are 3 types of items - Jumper, Pillow and Comforter
- There are 3 subtypes of each item. Finding any of these items will give a positive or negative influence on user stats. 
- USers can only find one of each item type per game but can possible find 3 items per game (eg, user can find 1 Jumper, 1 Pillow and 1 Comforter per game but not 2 Jumpers)
- Items are displayed as an image after they are found
- These images were generated using Dream by Womba AI imaging, so are custome made


## Validation

### HTML Validation

- Passed through https://validator.w3.org/


### CSS Validation

- Passed through https://jigsaw.w3.org/css-validator/


### JaveScript Validation

- Passed through https://jshint.com/


### Performance

Checked and edited after Google Lighthouse


### Performance tests on various devices

Throughout development and testing, I used the following devices to ensure that the site was responsive, and worked as intended.

- Laptop running Windows 11
- Samsung S20


### Browser Compatibility

The website was tested on several web browsers to ensure consistency. The browsers used are as follows:

- Microsoft Edge
- Google Chrome
- Firefox

## Bugs

 - Bug from validator: Bad value for attribute src on element img: Must be non-empty.
 - Fix: Set the image src attribute to #:

- Bug from validator: Element hr not allowed as child of element ul in this context.
- Fix: Move HR tag outside of ul/ol

- Bug: Game not restarting when fuction called
- Fix: No fix added yet

#### Deployment
* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.
-


#### Images

- https://www.pexels.com/
- https://dream.ai/create


### Code

- Progress Bar code adapted from: https://codepen.io/Asadabbas/pen/ZEGLBoJ 
- Text flashing from: https://stackoverflow.com/questions/9620594/removing-ul-indentation-with-css

## Acknowledgements

Thanks to all the below:
- Classmates who are also giving a helping hand
- Slack community
- Course facilitator (Paul Thomas)
- My Creative Director Nason (7 year old god son) Thanks for Dream Jumper idea