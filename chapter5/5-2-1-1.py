#順序特徴量のマッピング
import pandas as pd
size2int = {'S':0,'M':1,'L':2}
df['size'] = df['size'].map(size2int)
df.head