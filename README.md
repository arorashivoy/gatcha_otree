# Gacha Game Experiment

An [oTree](https://www.otree.org) experiment testing **loss aversion** and the
**sunk cost effect** in gacha games — the lottery mechanic behind titles like
Genshin Impact, where players spend currency on randomised rewards.

Behavioural economics course project at IIIT-Delhi, January 2025, by
**Aditya Padmagirwar**, **Aditi Saxena** and **Shivoy Arora**.

> A screenshot or GIF of the slot-machine page belongs here.

## What it tests

Participants get 200 tokens, each pull costs 10, and rewards run Common through
Legendary. They may quit after any pull; once tokens run out they can request 100
more. The design crosses two manipulations:

| | |
|---|---|
| **Pity-system disclosure** | whether participants are told that the odds of a high-value reward rise after a run of failures |
| **Outcome framing** | *"if you quit now, you risk losing what you've invested"* versus *"if you continue, you could win big"* |

It measures pulls made, tokens spent, the point at which a participant stops,
their perceived odds, and self-reported regret, frustration and satisfaction.

The central hypothesis is that **disclosing the pity system increases spending**
rather than reducing it — because it reframes a run of bad pulls as progress
toward a guaranteed reward, which is exactly the reasoning a sunk cost produces.

**The report sets out the design and its hypotheses; it does not report results.**
Analysis was planned as ANOVA and regression across the two factors, with a target
of 100–120 participants. Treat this repository as the instrument, not the finding.

## Overview

Participants start with an initial amount of in-game currency and can spend it to make pulls in the Gacha game. Each pull costs a certain amount of in-game currency and yields a random reward. The experiment aims to observe participants' behavior in managing their currency and making decisions based on their previous investments and outcomes.

## How to Run the Experiment

1. **Install Dependencies**: Ensure you have Python installed. Install the required dependencies using the 

requirements.txt

 file:
    ```sh
    pip install -r requirements.txt
    ```

2. **Set Up Environment Variables**: Set the `OTREE_ADMIN_PASSWORD` environment variable for admin access:
    ```sh
    export OTREE_ADMIN_PASSWORD='your_password'
    ```

3. **Run the Server**: Start the oTree server using the Procfile:
    ```sh
    otree devserver
    ```

4. **Access the Experiment**: Open your web browser and navigate to `http://localhost:8000` to access the experiment.

5. **Admin Interface**: To access the admin interface, navigate to `http://localhost:8000/admin` and log in with the username `admin` and the password you set in the environment variable.

## Report and presentation

- [Detailed report](https://drive.google.com/file/d/1XMUSN9nVYqjYyuuwgIJxwmWtUdqjuKVw/view?usp=sharing)
- [Presentation](https://drive.google.com/file/d/19r7tAt6S73aLs11k1PlxLn_f3NVJBeXT/view?usp=sharing)

Both are hosted on Google Drive and owned by a co-author, so a reader without
access will hit a sign-in wall.

## Credits

Reward tier artwork lives in `slot_machine/static/image/`. Its provenance is not
recorded in this repository and should be credited before anyone relies on it.
