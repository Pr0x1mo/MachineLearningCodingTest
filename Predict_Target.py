
import pandas as pd


train_data = pd.read_csv('C:\\Users\\xavie\\OneDrive\\Desktop\\MachineLearning\\train.csv')
test_data = pd.read_csv('C:\\Users\\xavie\\OneDrive\\Desktop\\MachineLearning\\test.csv')


test_ids = test_data['ID']


predictions = [0] * len(test_data)


submission_df = pd.DataFrame({'ID': test_ids, 'Target': predictions})

submission_df.to_csv('C:\\Users\\xavie\\OneDrive\\Desktop\\MachineLearning\\submission.csv', index=False)
