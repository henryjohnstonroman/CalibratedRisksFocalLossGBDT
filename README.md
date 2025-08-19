# CalibratedRisksFocalLossGBDT
Jupyter notebook with Python code for the paper "Estimating Calibrated Risks Using Focal Loss and Gradient-Boosted Trees for Clinical Risk Prediction": https://www.mdpi.com/2079-9292/14/9/1838

All_Model_Comparisons_Paper_Loop_10Y.ipynb: shows code for comparing GBDT models and all benchmark models. The task is to predict the 10-year risk (probability) of PTLD.

All_Model_Comparisons_Paper_Loop_Diabetes_JBI.ipynb: shows code for comparing GBDT models and all benchmark models. The task is to predict the risk (probability) of diabetes based on the following dataset: https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset

focal_transformation_binary.py: relates the focal loss minimizer to the true class-posterior probability. This transformation of the confidence scores was originally proposed in: https://openaccess.thecvf.com/content/CVPR2021/html/Charoenphakdee_On_Focal_Loss_for_Class-Posterior_Probability_Estimation_A_Theoretical_Perspective_CVPR_2021_paper.html
