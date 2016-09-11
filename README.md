Check out: http://devpost.com/software/aaa-67fakr for more details

For a brief demo: https://www.youtube.com/watch?v=1vnHadw-2k8

I, Trainer is a robotic personal trainer capable of offering encouragement, and keeping track of your exercises.

## Inspiration
Rocky, and I, Robot.

## What it does
I, Trainer, is a highly functional personal trainer. Designed to encourage users, I, Trainer also keeps track of the user's data (exercises completed, date, etc.).

## How we built it
**Interacting with I, Trainer**
You interact with I, Trainer by having a conversation. You tell pepper you want to exercise, what exercise you want to do, and how difficult you want the exercise to be. This dialogue is handled in the Choregraphe studio. The user also has the option of directly interacting with the tablet. Displayed on the tablet are webpages. To perform a rep, the user taps one of I, Trainer's sensors upon completion. I, Trainer displays your performance on the exercises you've done so far, as well as the current exercise. Chart.js, and jQuery were used to display the cool visuals and navigation between pages.

**Keeping track of data **
We setup a flask server with endpoints to keep track of the user data. This server was then deployed on Heroku. Whenever the user turns on I, Trainer the data is fetched, and when an exercise is completed I, Trainer posts the relevant data.

## Challenges we ran into
Integrating webpage navigation/updates with I, Trainer controls.
Making I, Trainer dance.

## Accomplishments that we're proud of
Building a fully functional, not hard-coded application in under 24 hours while sleep-deprived.

## What we learned
How to build an interactive application using Pepper`s SDK, and integrating that with a backend.
To use version control next time.

## What's next for I, Trainer
More exercises, more data, more personalized exercise dashboard.