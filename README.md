# Dashboard : Analysis of the INA Thematic Barometer for French News Bulletins (2005 - 2020)

## Project description

This dashboard hosts a complete collection of both linear, detailed insight and interactive visualizations on the subject of news coverage between 2005 and 2020.

Given the size of the data and the many details and information hidden inside the dataset, we wish here to not only to provide an in-depth analysis of the data, but also give an opportunity for the users to test their own analysis skills.

## Data

The data was extracted from the French government's official [data.gouv.fr](https://www.data.gouv.fr) website and can be found [right here](https://www.data.gouv.fr/fr/datasets/classement-thematique-des-sujets-de-journaux-televises-janvier-2005-septembre-2020).
The samples are categorized by two features : the thematic, which can take 14 values, and the channel, which can take 6. The analysis we will provide in this dashboard will focus on those two features,
investigating their tendencies and variations over the timespan, both separately and jointly.

## Setup

#### -- Open the terminal for your coding environment

#### -- Install streamlit
- (`pip install streamlit`)
  
Optional : Validate the installation by running the Hello app
- (`streamlit hello`)
#### -- Access the folder storing the source code of the app
- (`cd [PATH]`)
#### -- Run the Hello.py file using streamlit
- (`streamlit run Hello.py`)
#### -- Following a short loading period, the Streamlit app should open on your browser

## Warnings (to read before usage) :

```diff
Due to defaults in the construction of the original .CSV file rendering it unusable (header split between the 1st and 2nd rows),
the actual data used by the dataframe comes from a manually cleaned .CSV file, which can be found in the 'data' folder
of the source code.
```

## Credits
Coding/Data Cleaning/Data Analysis : **Romain Ferigo** 
