# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
    - Developed in part by: Bennett Woods, WGU
    - 06/2025
    - v1.0
    - Questions/Comments: bwoo175@wgu.edu

    The model was built using a Random Forest Classifier with Pyton and sciki-learn. The model is deployed using FastAPI and is tested with GitHub Actions that have been automated with unit testing and style enforcement parameters. 

## Intended Use
    The model is intended to be used to predict whether an individual earns more, or less, than $50,000 in a calendar year based on demographic and occupation-related attributes within the census.csv dataset. 

## Training Data
    The model was trained using the census.csv dataset, or 'Adult Census Income dataset'. It includes features like: work class, education, marital status, occupation, relationship, race, sex and native country. 'Salary', the label column, is made up of two values: <=50K and >=50K. 

    The 80/20 train-test split was applied and categorical vairables were encoded using HotEncoder and the label was made by LabelBinarizer. 

## Evaluation Data
    The evaluation dataset, the 20% of the split, was preprocessed identically as the 80% to remain consistent with encoding and transformation of labels.

## Metrics
_Please include the metrics used and your model's performance on those metrics._
Precision: 0.7391 | Recall: 0.6384 | F1: 0.6851

The results are saved in slice_output.txt for logging.

## Ethical Considerations
    The dataset used has demographic features that are sensitive in nature, such as race and sex. There does exist a potential for bias along these two features by overfitting or or education levels in relation to certain races. 

    There will be necessary changes required of the datset to be implemented for important purposes outside of this project.

## Caveats and Recommendations
    The model only captures data from 1994-1995 US census data. Therefore, it may mot be applied generally to other populations due to societal differences. 

    Other features that will need to be considered to provide accurate data would be years of occupational experience, education years of experience, economic background and others. 

    It is recommended to apply changes to sensitive data features and monitor potential for biases based on the information above.