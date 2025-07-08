# Animal Image Classification Project

## Overview
This project is an animal image classification system that uses a machine learning model to recognize and classify images of various animals. The project includes a user interface for easy interaction and testing of the model.

## Features
- Classifies images of animals such as bears, cats, dogs, elephants, giraffes, horses, and pandas
- Pre-trained machine learning model for image recognition
- User-friendly interface for uploading and testing images
- Organized dataset for training and evaluation

## Dataset
The dataset is organized in the `data/` directory, with subfolders for each animal class:
- `bear/`
- `cat/`
- `dog/`
- `elephant/`
- `giraffe/`
- `horse/`
- `panda/`

Each subfolder contains images of the respective animal.

## Model
The trained model is saved in the `saved_model/my_model/` directory. It is used by the UI to classify new images.

## Usage
1. **Install Requirements**
   - Make sure you have Python 3.x installed.
   - Install required packages (see Requirements section).
2. **Run the UI**
   - Execute the `ui.py` script to launch the user interface:
     ```bash
     python ui.py
     ```
3. **Test the Model**
   - Use the UI to upload images and view classification results.

## Requirements
- Python 3.x
- TensorFlow or Keras (for loading the model)
- Additional packages as required by `ui.py` (e.g., tkinter, PIL, etc.)

Install dependencies using pip:
```bash
pip install tensorflow pillow
```
Add any other dependencies as needed.

## Project Structure
```
project/
├── data/                # Animal image dataset
├── saved_model/         # Trained model directory
├── testing/             # Test images
├── ui.py                # User interface script
├── README.md            # Project documentation
└── ...                  # Other files
```

## License
Specify your license here.

## Acknowledgements
- Dataset sources
- Libraries and frameworks used 