#質的変数の処理
import pandas as pd
df = pd.DataFrame([
    ['Cola' ,'S'],
    ['Cola' ,'M'],
    ['Grean Tea' ,'L'],
    ['Milk' ,'M'],
],columns=['drink', 'size'])
print(df.head())
print('\n')

#順序特徴量のマッピング
size2int = {'S':0,'M':1,'L':2}
df['size'] = df['size'].map(size2int)
print(df.head())
print('\n')

#名義特徴量の変換
# モジュールが見つからないエラー
#from sklearn.preprosessing import LabelEncoder
from sklearn import preprocessing

encoder = preprocessing.LabelEncoder()
df['drinkLabel'] = encoder.fit_transform(df['drink'])
print(df.head())
print('\n')

#one-hotエンコーディング
print(pd.get_dummies(df))