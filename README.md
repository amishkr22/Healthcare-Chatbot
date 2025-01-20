# HealthCare ChatBot: Symptom Analysis and Diagnosis Tool

This repository contains a HealthCare ChatBot that uses machine learning to predict diseases based on user symptoms. It provides descriptions, suggests precautions, and analyzes symptom severity to recommend whether a doctor's consultation is necessary. The project includes an interactive chatbot with text-to-speech functionality.

## Features

- **Symptom Input:** Users can input symptoms interactively.
- **Disease Prediction:** Predicts potential diseases using a Decision Tree Classifier.
- **Interactive Chatbot:** Includes text-to-speech for better interaction.
- **Precautionary Measures:** Provides a list of precautions for predicted diseases.
- **Severity Analysis:** Suggests consultation based on symptom severity.
- **Data Visualization:** Includes exploratory data analysis (EDA) of the training dataset.

## Technologies Used

- Python (NumPy, pandas, matplotlib, seaborn, scikit-learn, pyttsx3)
- Machine Learning (Decision Tree Classifier, Label Encoding)
- Dataset Handling (CSV Parsing, Data Preprocessing)

## Datasets

The following datasets are used in this project (place them in a `Data/` directory in the project root):
1. **`Training.csv`** - Training dataset for disease prediction.
2. **`Testing.csv`** - Testing dataset for model validation.
3. **`Symptom_Description.csv`** - Descriptions of symptoms.
4. **`Symptom_Precaution.csv`** - Precautionary measures for diseases.
5. **`Symptom_Severity.csv`** - Severity levels of symptoms.

## Installation and Setup

1. **Clone the Repository**  
   Clone the repository to your local machine:
   ```bash
   git clone https://github.com/amishkr22/Healthcare-Chatbot.git
   cd healthcare-chatbot

2. **Install Dependencies**  
   Ensure you have Python 3.8 or higher installed. Use the provided `requirements.txt` file to install the necessary packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Add the Datasets**  
   Create a `Data/` directory in the project root and place the following files inside:
   - `Training.csv`
   - `Testing.csv`
   - `Symptom_Description.csv`
   - `Symptom_Precaution.csv`
   - `Symptom_Severity.csv`

4. **Run the Notebook**  
   Open the notebook `HealthCareChatBot.ipynb` in Jupyter Notebook or any compatible IDE and execute the cells to start the chatbot.

## Usage

1. **Launch the ChatBot**  
   Execute the notebook or the main script to start the chatbot.

2. **Interact with the ChatBot**  
   - Provide your name to initiate the session.
   - Enter symptoms as prompted.
   - Specify the duration of symptoms for severity analysis.

3. **Receive Output**  
   - View the predicted diseases, descriptions, and precautionary measures.
   - Get recommendations on whether a doctor's consultation is needed.

4. **Explore Data**  
   - Visualize data insights, including feature distributions and EDA outputs.

## Code Structure

- **Exploratory Data Analysis (EDA):** Insights into the training dataset.
- **Preprocessing:** Data preparation for training and testing.
- **Model Building:** Creation and evaluation of a Decision Tree Classifier.
- **Chatbot Functionality:** Symptom input, disease prediction, and response generation.
- **Utilities:**
  - `text_to_speech`: Converts text responses to speech.
  - `check_pattern`: Matches user input with known symptoms.
  - `sec_predict`: Provides secondary disease predictions.

## Future Enhancements

- Add advanced machine learning models (e.g., Random Forest, Neural Networks).
- Expand the dataset to include more symptoms and diseases.
- Integrate a web or mobile-based interface for broader accessibility.
- Support multilingual interactions.

## Acknowledgments

- **Data Source:** Provided datasets for symptoms, descriptions, and precautions.
- **Open-Source Libraries:** Special thanks to the Python libraries used in this project.