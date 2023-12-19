import pandas as pd
import matplotlib.pyplot as plt

# 데이터 정의
data = {
    'Month': ['Sep', 'Oct', 'Nov', 'Dec', 'Jan', 'Feb'],
    'Total Sales': [5280000, 5501000, 5469000, 5480000, 5533000, 5554000],
    'Sales Target': [5280000, 5500000, 5729000, 5968000, 6217000, 6476000],
    'Advertising Cost': [1056000, 950400, 739200, 528000, 316800, 316800],
    'Social Network Cost': [0, 105600, 316800, 528000, 739200, 739200],
    'Price per Ounce': [2.00, 2.00, 2.00, 1.90, 1.90, 1.90]
};

# DataFrame 생성
dtframe = pd.DataFrame(data);

# 그래프 그리기
plt.figure(figsize=(10, 6));

# 매출, 목표 매출, 광고비용, 소셜네트워크비용 그래프
for column in dtframe.columns[1:5]:
    plt.plot(dtframe['Month'], dtframe[column], marker='o', label=column)

plt.title('Sales, Targets, and Costs Over Time')
plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.legend()

plt.twinx()

# 1 온스별 단가 그래프
plt.plot(dtframe['Month'], dtframe['Price per Ounce'], marker='o', color='purple', label='Price per Ounce')
plt.ylabel('Price ($)')
plt.legend(loc='upper right')

plt.show();
