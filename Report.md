# Method description & parameter settings
- According to the comma in the dataset to extract data
- Use SVM tool to train model and do the prediction
- Do the 5-fold cross validation

        ./svm-train -v 5

- Training in probability estimates mode

        ./svm-train -b 1

- Do the prediction

        ./svm-predict -b 1

# Experimental results – accuracy
On OW2 PW1

    Cross Validation Accuracy = 92.56%

On OW8 PW2

    Cross Validation Accuracy = 91.8352%


# Discussion of difficulty or problem encountered
Even I tried different mode and different parameters, the prediction result are weird although the accuracy is about 90%. 

I think it is the limit of SVM on this dataset, I believe using deep learning method, like LSTM will strongly improve the result.