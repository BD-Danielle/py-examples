# ch29_1.py
import pandas as pd
import numpy as np

# 定義數據
data = {
    'Sex': ['M', 'F', 'F', 'M', 'M', 'F', 'F', 'M', 'F', 'M'],
    'Age': ['18-24', '25-34', '45+', '35-44', '18-24',
            '35-44', '25-34', '45+', '18-24', '25-34'],
    'Type': ['Sci', 'Drama', 'Sci', 'Drama', 'Sci',
             'Drama', 'Sci', 'Sci', 'Drama', 'Sci'],
    'Like': ['Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'No', 'Yes', 'No', 'Yes']
}

# 創建 DataFrame
df = pd.DataFrame(data)

# 計算先驗機率
prob_like = df[df['Like'] == 'Yes'].shape[0] / df.shape[0]
prob_dislike = 1 - prob_like

# 計算條件機率
prob_F_like = df[(df['Sex'] == 'F') & (df['Like'] == 'Yes')].shape[0]\
              / df[df['Like'] == 'Yes'].shape[0]
prob_25_34_like = df[(df['Age'] == '25-34') & (df['Like'] == 'Yes')].shape[0]\
                  / df[df['Like'] == 'Yes'].shape[0]
prob_drama_like = df[(df['Type'] == 'Drama') & (df['Like'] == 'Yes')].shape[0]\
                  / df[df['Like'] == 'Yes'].shape[0]
prob_F_dislike = df[(df['Sex'] == 'F') & (df['Like'] == 'No')].shape[0]\
                 / df[df['Like'] == 'No'].shape[0]
prob_25_34_dislike = df[(df['Age'] == '25-34') & (df['Like'] == 'No')].shape[0]\
                     / df[df['Like'] == 'No'].shape[0]
prob_drama_dislike = df[(df['Type'] == 'Drama') & (df['Like'] == 'No')].shape[0]\
                     / df[df['Like'] == 'No'].shape[0]

# 計算 P(x)
p_x_like = prob_F_like * prob_25_34_like * prob_drama_like
p_x_dislike = prob_F_dislike * prob_25_34_dislike * prob_drama_dislike
p_x = p_x_like * prob_like + p_x_dislike * prob_dislike

# 計算後驗機率
prob_like_F_25_34_drama = p_x_like * prob_like / p_x
prob_dislike_F_25_34_drama = p_x_dislike * prob_dislike / p_x

# 印出結果
print('女性(25-34歲)喜歡劇情片的機率   :', prob_like_F_25_34_drama)
print('女性(25-34歲)不喜歡劇情片的機率 :', prob_dislike_F_25_34_drama)

# 最終結果
if prob_like_F_25_34_drama > prob_dislike_F_25_34_drama:
    print('結果 : 女性(25-34歲)喜歡劇情片')
else:
    print('結果 : 女性(25-34歲)不喜歡劇情片')


