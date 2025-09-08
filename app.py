
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import koreanize_matplotlib

# Set page title and icon
st.set_page_config(page_title="HR Data Analysis", page_icon=":bar_chart:")

# Load data with caching
@st.cache_data
def load_data():
    df = pd.read_csv('/content/drive/MyDrive/2025_python/HR_Data.csv')
    df['퇴직'] = df['퇴직여부'].map({'Yes': 1, 'No': 0}).astype('int8')
    return df

df = load_data()

st.title("HR 데이터 분석 대시보드")

# 1. Overall Attrition Rate KPI
st.header("주요 성과 지표 (KPI)")
total_attrition_rate = df['퇴직'].mean() * 100
st.metric("전체 퇴직율", f"{total_attrition_rate:.2f}%")

# 2. Attrition Distribution (Pie Chart)
st.header("퇴직 여부 분포")
attrition_counts = df['퇴직여부'].value_counts(normalize=True)
fig1, ax1 = plt.subplots()
ax1.pie(attrition_counts, labels=attrition_counts.index, autopct='%.1f%%', startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig1)

# 3. Attrition Rate by Department
st.header("부서별 퇴직율")
dept_rate = df.groupby('부서')['퇴직'].mean().sort_values(ascending=False)
fig2, ax2 = plt.subplots()
sns.barplot(x=dept_rate.index, y=dept_rate.values, ax=ax2)
ax2.set_title("부서별 퇴직율")
ax2.set_ylabel("퇴직율")
st.pyplot(fig2)

# 4. Attrition Rate by Age Group
st.header("연령대별 퇴직율")
df['연령대'] = pd.cut(df['나이'], bins=[18, 29, 39, 49, 59, 69], labels=['20대', '30대', '40대', '50대', '60대'], right=False)
age_rate = df.groupby('연령대')['퇴직'].mean()
fig3, ax3 = plt.subplots()
sns.barplot(x=age_rate.index, y=age_rate.values, ax=ax3)
ax3.set_title("연령대별 퇴직율")
ax3.set_ylabel("퇴직율")
st.pyplot(fig3)

# 5. Attrition Rate by Gender
st.header("성별 퇴직율")
gender_rate = df.groupby('성별')['퇴직'].mean()
fig4, ax4 = plt.subplots()
sns.barplot(x=gender_rate.index, y=gender_rate.values, ax=ax4)
ax4.set_title("성별 퇴직율")
ax4.set_ylabel("퇴직율")
st.pyplot(fig4)

# 6. Attrition Rate by Marital Status
st.header("결혼 여부별 퇴직율")
marital_rate = df.groupby('결혼여부')['퇴직'].mean()
fig5, ax5 = plt.subplots()
sns.barplot(x=marital_rate.index, y=marital_rate.values, ax=ax5)
ax5.set_title("결혼 여부별 퇴직율")
ax5.set_ylabel("퇴직율")
st.pyplot(fig5)

# 7. Attrition Rate by Business Travel
st.header("출장 빈도별 퇴직율")
travel_rate = df.groupby('출장빈도')['퇴직'].mean()
fig6, ax6 = plt.subplots()
sns.barplot(x=travel_rate.index, y=travel_rate.values, ax=ax6)
ax6.set_title("출장 빈도별 퇴직율")
ax6.set_ylabel("퇴직율")
st.pyplot(fig6)

# 8. Attrition Rate by Overtime
st.header("야근 여부별 퇴직율")
overtime_rate = df.groupby('야근정도')['퇴직'].mean()
fig7, ax7 = plt.subplots()
sns.barplot(x=overtime_rate.index, y=overtime_rate.values, ax=ax7)
ax7.set_title("야근 여부별 퇴직율")
ax7.set_ylabel("퇴직율")
st.pyplot(fig7)

# 9. Attrition Rate by Distance from Home
st.header("집과의 거리별 퇴직율")
distance_rate = df.groupby('집과의거리')['퇴직'].mean()
fig8, ax8 = plt.subplots(figsize=(10, 6))
sns.barplot(x=distance_rate.index, y=distance_rate.values, ax=ax8)
ax8.set_title("집과의 거리별 퇴직율")
ax8.set_ylabel("퇴직율")
ax8.set_xlabel("집과의 거리")
plt.xticks(rotation=90)
st.pyplot(fig8)

# 10. Attrition Rate by Monthly Income Quartile
st.header("월급여 구간별 퇴직율")
df['월급여_구간'] = pd.qcut(df['월급여'], 4, duplicates='drop')
income_rate = df.groupby('월급여_구간')['퇴직'].mean()
fig9, ax9 = plt.subplots()
sns.barplot(x=income_rate.index, y=income_rate.values, ax=ax9)
ax9.set_title("월급여 구간별 퇴직율")
ax9.set_ylabel("퇴직율")
plt.xticks(rotation=45)
st.pyplot(fig9)

# 11. Attrition Rate by Percent Salary Hike Quartile
st.header("급여 증가분 백분율 구간별 퇴직율")
df['급여증가분백분율_구간'] = pd.qcut(df['급여증가분백분율'], 4, duplicates='drop')
hike_rate = df.groupby('급여증가분백분율_구간')['퇴직'].mean()
fig10, ax10 = plt.subplots()
sns.barplot(x=hike_rate.index, y=hike_rate.values, ax=ax10)
ax10.set_title("급여 증가분 백분율 구간별 퇴직율")
ax10.set_ylabel("퇴직율")
plt.xticks(rotation=45)
st.pyplot(fig10)

# 12. Attrition Rate by Stock Option Level
st.header("스톡옵션 정도별 퇴직율")
stock_rate = df.groupby('스톡옵션정도')['퇴직'].mean()
fig11, ax11 = plt.subplots()
sns.barplot(x=stock_rate.index, y=stock_rate.values, ax=ax11)
ax11.set_title("스톡옵션 정도별 퇴직율")
ax11.set_ylabel("퇴직율")
st.pyplot(fig11)

# 13. Attrition Rate by Total Working Years Quartile
st.header("근속 연수 구간별 퇴직율")
df['근속연수_구간'] = pd.qcut(df['근속연수'], 4, duplicates='drop')
years_rate = df.groupby('근속연수_구간')['퇴직'].mean()
fig12, ax12 = plt.subplots()
sns.barplot(x=years_rate.index, y=years_rate.values, ax=ax12)
ax12.set_title("근속 연수 구간별 퇴직율")
ax12.set_ylabel("퇴직율")
plt.xticks(rotation=45)
st.pyplot(fig12)

# 14. Attrition Rate by Years in Current Role Quartile
st.header("현재 역할 연수 구간별 퇴직율")
df['현재역할년수_구간'] = pd.qcut(df['현재역할년수'], 4, duplicates='drop')
role_years_rate = df.groupby('현재역할년수_구간')['퇴직'].mean()
fig13, ax13 = plt.subplots()
sns.barplot(x=role_years_rate.index, y=role_years_rate.values, ax=ax13)
ax13.set_title("현재 역할 연수 구간별 퇴직율")
ax13.set_ylabel("퇴직율")
plt.xticks(rotation=45)
st.pyplot(fig13)

# 15. Attrition Rate by Years Since Last Promotion Quartile
st.header("마지막 승진 연수 구간별 퇴직율")
df['마지막승진년수_구간'] = pd.qcut(df['마지막승진년수'], 4, duplicates='drop')
promotion_years_rate = df.groupby('마지막승진년수_구간')['퇴직'].mean()
fig14, ax14 = plt.subplots()
sns.barplot(x=promotion_years_rate.index, y=promotion_years_rate.values, ax=ax14)
ax14.set_title("마지막 승진 연수 구간별 퇴직율")
ax14.set_ylabel("퇴직율")
plt.xticks(rotation=45)
st.pyplot(fig14)
