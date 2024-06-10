
# Local LaMini Model

## Prerequisites

1. **Code Editor:** [Visual Studio Code](https://code.visualstudio.com/)
2. **Virtual Environment:** [Anaconda](https://www.anaconda.com/)
3. **Git and Git LFS:** [Git](https://www.git-scm.com/) and [Git LFS](https://git-lfs.com/)
4. **Hugging Face Account:** [Hugging Face](https://huggingface.co/)

## Step 1: Clone Repository or Install Python Files

### Clone Repository
Once you have installed Git, you can clone the repository to get all the files:
\`\`\`bash
git clone https://github.com/Geet-choudhari/Local-Lamini-Model
\`\`\`

### Manual Installation
Alternatively, create a project directory on your local machine, install the three Python files manually, and create two folders named \`db\` and \`docs\` in the same directory.
- \`db\`: This folder will store your embeddings.
- \`docs\`: This folder will store your PDF files.

## Step 2: Create a Virtual Environment

Create a virtual environment using Conda or Venv and install all the dependencies:
\`\`\`bash
pip install -r requirements.txt
\`\`\`

## Step 3: Install the LLM Model Locally

We will use the LaMini-T5-738M model.

### Prerequisites
1. **Hugging Face Account:** [Sign up on Hugging Face](https://huggingface.co/)
2. **Git LFS:** [Install Git LFS](https://git-lfs.com/)

### Install the Model
Run the following commands to install the model locally in the same repository:
\`\`\`bash
git lfs install
git clone https://huggingface.co/MBZUAI/LaMini-T5-738M
\`\`\`

## Step 4: Prepare the Data

Place your PDF files in the \`docs\` folder. To create embeddings for the files, run the following script:
\`\`\`bash
python ingest.py
\`\`\`
This will create embeddings and a vector database file in the \`db\` folder.

## Step 5: Run the Model

To activate the model and start the application, run:
\`\`\`bash
streamlit run app.py
\`\`\`
"""


