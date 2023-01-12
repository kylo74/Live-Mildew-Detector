## Dataset Content
* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). We created then a fictitious user story where predictive analytics can be applied in a real project in the workplace.
* The dataset contains +4 thousand images taken from client's crop fields. The images show cherry leaves that are healthy and cherry leaves that contain powdery mildew, which is a fungal disease that affects a wide range of plants. The cherry plantation crop is one of their finest products in the portfolio and the company is concerned about supplying the market with a product of compromised quality.



## Business Requirements
The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is to manually verify if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If it has powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute.  The company has thousands of cherry trees located in multiple farms across the country. As a result, this manual process is not scalable due to time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that is capable of detecting instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project to all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.


* 1 - The client is interested in conducting a study to visually differentiate a cherry leaf that is healthy and that contains powdery mildew.
* 2 - The client is interested to predict if a cherry leaf is healthy or contains powdery mildew.


## Hypothesis and how to validate?
* We suspect leaves of plants that are infected with powdery mildew have clear signs distinguishing them from uninfected plants.
  *  An average image study can help to investigate it and if there are clear differences then we will know.


## Rationale to map the business requirements to the Data Visualizations and ML tasks
* **Business Requirement 1**: Data Visualization 
	* We will display the "mean" and "standard deviation" images for infected and healthy leaves.
 	* We will display the difference between an average infected leaf and an average healthy cell.
	* We will display a image montage for either infected or healthy leaves.
	
	

* **Business Requirement 2**:  Classification
	* We want to predict if a given leaf is healthy or not. 
	* We want to build a binary classifier and generate reports.


## ML Business Case
### Mildew detection binary classifier
* We want an Ml model to predict if a leaf is infected with powdery mildew or not, based on the dataset provided. It is a supervised, 2 class, single label, binary classification model
* Our ideal outcome is provide an algorithm that can speed up the detection of powdery mildew in cherry plants.
* The model success metrics are
	* Accuracy of 97% or above on the test set.
* The model output is defined as a flag, indicating if the plant is healthy or not and the associated probability of being infected or not. A picture can be uploaded to the app and the model will make a prediciton. The prediction is made on the fly (not in batches).
* Heuristics: The current diagnostic involves an employee spending around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If it has powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute.  The company has thousands of cherry trees located in multiple farms across the country. As a result, this manual process is not scalable due to time spent in the manual process inspection.
* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves).
	* contains +4 thousand images taken from client's crop fields. The images show cherry leaves that are healthy and cherry leaves that contain powdery mildew, which is     a fungal disease that affects a wide range of plants


## Dashboard Design

### Page 1: Quick Project Summary
* Quick project summary
	* General Information
		* Powdery mildew, which is a fungal disease that affects a wide range of plant
		* Currently, the process is to manually verify if a given cherry tree contains powdery mildew. An employee spends around 30 minutes 
      in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. 
      If it has powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute. 
      The company has thousands of cherry trees located in multiple farms across the country. As a result, this manual process is not scalable 
      due to time spent in the manual process inspection 
		* To save time in this process, the IT team suggested an ML system that is capable of detecting instantly, using a tree leaf image, 
      if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative 
      is successful, there is a realistic chance to replicate this project to all other crops. The dataset is a collection of cherry leaf 
      images provided by Farmy & Foods, taken from their crops
	* Project Dataset
		* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves).
	  * contains +4 thousand images taken from client's crop fields. The images show cherry leaves that are healthy and cherry leaves that contain powdery mildew, which       is a fungal disease that affects a wide range of plants
	* Link to addition ainformation
	* Business requirements
		*  The client is interested in conducting a study to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew.
    *  The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

### Page 2: leaves Visualizer
* It will answer business requirement 1
	* Checkbox 1 - Difference between average and variability image
	* Checkbox 2 - Differences between average infected and average healthy leaves
	* Checkbox 3 - Image Montage

### Page 3: Mildew Detector
* Business requirement 2 information - "The client is interested to tell whether a given leaf contains powdery mildew or not."
* Link to download a set of healthy and infected leaf images for live prediction.
* User Interface with a file uploader widget. The user should upload multiple leaves. It will display the image and a prediction statement, indicating if the leaf is infected or not with powdery mildew and the probability associated with this statement. 
* Table with image name and prediction results.
* Download button to download table.

### Page 4: Project Hypothesis and Validation
* Block for each project hypothesis, describe the conclusion and how you validated.

### Page 5: ML Performance Metrics
* Label Frequencies for Train, Validation and Test Sets
* Model History - Accuracy and Losses
* Model evaluation result



## Unfixed Bugs
* You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a big variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

## Deployment
### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly in case all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.


## Main Data Analysis and Machine Learning Libraries
* Tensorflow. Used to make the convolutional neural network that classifies the leaves as either infected or uninfected


## Credits 

* In this section you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign up page are from This Open Source site
- The images used for the gallery page were taken from this other open source site



## Acknowledgements (optional)
* In case you would like to thank the people that provided support through this project.
