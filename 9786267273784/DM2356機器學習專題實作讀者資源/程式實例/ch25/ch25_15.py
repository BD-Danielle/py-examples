# ch25_15.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score

# 讀取數據
stores_df = pd.read_csv('stores.csv')
features_df = pd.read_csv('features.csv')
sales_df = pd.read_csv('sales.csv')

# 將 features_df 和 sales_df 在 Store 和 Date 進行欄位合併
merged_df = pd.merge(sales_df, features_df, on=['Store', 'Date'], how='left')

# 將 merged_df 和 stores_df 在 Store 進行欄位合併
final_df = pd.merge(merged_df, stores_df, on=['Store'], how='left')

# 將日期 "Date" 轉換為日期型數據
final_df['Date'] = pd.to_datetime(final_df['Date'], format='%d/%m/%Y')

# 從日期中提取年份和月份作為新的特徵
final_df['Year'] = final_df['Date'].dt.year
final_df['Month'] = final_df['Date'].dt.month

# 將商店類型 "Type" 轉換為類別型數據
final_df['Type'] = final_df['Type'].astype('category').cat.codes

# 處理缺失值
final_df.fillna(0, inplace=True)

# 刪除"IsHoliday_y"欄位, 將"IsHoliday_x"改為"IsHoliday"
final_df = final_df.drop('IsHoliday_y', axis=1)
final_df = final_df.rename(columns={'IsHoliday_x': 'IsHoliday'})

# 將結果存儲為"RetailDataAnalytics.csv"
final_df.to_csv('RetailDataAnalytics.csv', index=False)

# 定義特徵變量和目標變量
X = final_df.drop(['Weekly_Sales', 'Date'], axis=1)
y = final_df['Weekly_Sales']

# 劃分訓練集和測試集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
                                                    random_state=5)

# 創建並訓練決策樹回歸模型
model = DecisionTreeRegressor(random_state=5)
model.fit(X_train, y_train)

# 進行預測
y_pred = model.predict(X_test)

# 計算並輸出 R 平方（決定係數）
r2 = r2_score(y_test, y_pred)
print(f'R平方係數 : {r2:.3f}')



