# Text-Improvement-Engine
This is a text improvement engine that analyses a given text and suggests improvements based on the similarity to a list of "standardised" phrases. These standardised phrases represent the ideal way certain concepts should be articulated, and the tool should recommend changes to align the input text closer to these standards.

# Setup Process
Clone this repository to your local machine.<br>
Install the required dependencies with pip install -r requirements.txt.<br>
Run the script with python text_improvement.py.<br>

# Usage
When you run the script, you will be prompted to choose an option for inputting your text. You can either enter the text directly or provide a path to a text file.

# Technologies Used
Python: The script is written in Python.<br>
Transformers: This library provides the pre-trained DistilBERT model used for text analysis.<br>
NLTK: The Natural Language Toolkit is used for tokenizing the input text and removing stop words.<br>
Scikit-learn: This library’s cosine_similarity function is used to calculate semantic similarity.<br>

# Design Decisions
The DistilBERT model was chosen for its balance between performance and efficiency. It’s capable of understanding the semantic meaning of text, which is crucial for this tool. The cosine similarity measure was used because it effectively captures the angle between two vectors, which in this case represent our phrases.

# Results
Here are some example results from the tool:<br><br>

Suggestion: Replace 'consensus need' with 'Demonstrate leadership' (Similarity: 0.8544626235961914)<br>
Suggestion: Replace 'good use' with 'Optimal performance' (Similarity: 0.8528397083282471)<br>
Suggestion: Replace 'aim efficient' with 'Execute strategies' (Similarity: 0.89717036485672)<br>
Suggestion: Replace 'efficient look' with 'Optimal performance' (Similarity: 0.8553969860076904)<br>
Suggestion: Replace 'ways creative' with 'Foster innovation' (Similarity: 0.8611928224563599)<br>
Suggestion: Replace 'Growth essential' with 'Drive growth' (Similarity: 0.897219181060791)<br>
Suggestion: Replace 'building strong' with 'Demonstrate leadership' (Similarity: 0.8578121662139893)<br>
Suggestion: Replace 'relationships team' with 'Demonstrate leadership' (Similarity: 0.8545510172843933)<br>
