## Objective

The purpose of this project is to break down and interpret soccer teams' performance data, giving users clear insights into a team's strengths and weaknesses. 

We aim to build an analysis tool that provides a comprehensive view of how good a team is and how it compares to others. By evaluating key metrics like **goals**, **dangerous attacks**, **shots**, and **shots on target**, we can identify a team's strengths. Additionally, by analyzing defensive stats, we can uncover their weaknesses—based on how effectively or poorly they respond to an opponent's attacks.

Our tool will allow users to analyze these performances over custom time frames. Furthermore, we plan to train a model that ranks teams based on these metrics, providing valuable insights into their overall performance.


## Dataset

Here are a couple of datasets that we are utilizing in this project. Some of the data are used for visualization purposes, while others are crucial for building an accurate prediction model.

- **[matches.csv](https://github.com/dataquestio/project-walkthroughs/blob/master/football_matches/matches.csv):**  
  This dataset contains over 1,390 rows of data from recent soccer games in the Premier League, starting from 2021. It provides key metrics such as **xG**, **xGA**, **possession**, and many more essential statistics.

- **pl_data_dt.json:**  
  This is a custom dataset created for this project, where we scraped detailed soccer performance data from various online websites.

## Prerequisites

Before running this project, ensure that the required tools are installed on your system.

### Check if Python is Installed

To check if Python is installed on your system, open a terminal or command prompt and run:

```bash
python --version
```

### Setting Up

Follow these steps to set up and run the application:


### Navigate to the directory where you want to clone/run/save the application
```bash
cd your_selected_directory
```
### Clone this repository
```bash
git clone https://github.com/mao-99/scorecast.git
```
### Navigate to the cloned repository
```bash
cd scorecast
```
### Install the dependencies listed in the requirements.txt file
```bash
pip install -r requirements.txt
```
### Run the application using Streamlit
```bash
streamlit run streamlit_app.py
```

## Application Graphical User Interface
<img width="727" alt="Screenshot 2024-12-05 at 10 04 08 PM" src="https://github.com/user-attachments/assets/33c42664-cf80-4753-b01e-f4c264cc0240">

## Report

You can find the detailed report for this project [here](https://docs.google.com/document/d/15nuv61q-cU3QHNOqI



