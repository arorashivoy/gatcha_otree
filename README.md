# Gacha Game Experiment

Please check out the detailed project report and the presentation in the links below.

This Repository contains the code for Behavioural Economics experiment designed to test Loss Aversion and the Sunk Costs effect in Gacha games. The experiment simulates a Gacha-style game where participants use in-game currency to receive random rewards.
- [Presentation](https://drive.google.com/file/d/19r7tAt6S73aLs11k1PlxLn_f3NVJBeXT/view?usp=sharing)
- [Detailed Report](https://drive.google.com/file/d/1XMUSN9nVYqjYyuuwgIJxwmWtUdqjuKVw/view?usp=sharing)

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
