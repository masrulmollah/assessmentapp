import streamlit as st
import pandas as pd

# Define the discount table
discount_data = {
    'Financial support required': ['Least', 'Little', 'Neutral', 'Moderate', 'High'],
    'Data analysis enthusiast': ['Least', 'Little', 'Neutral', 'Moderate', 'High'],
    'Relevant Experience': ['Least', 'Little', 'Neutral', 'Moderate', 'High'],
    'Relevant Education': ['Least', 'Little', 'Neutral', 'Moderate', 'High'],
    'Relevance to job': ['Least', 'Little', 'Neutral', 'Moderate', 'High'],
    'Skill improvement need': ['Least', 'Little', 'Neutral', 'Moderate', 'High']
}
discount_df_levels = pd.DataFrame(discount_data)
criteria_list = discount_df_levels.columns.tolist()
level_options = ['Least', 'Little', 'Neutral', 'Moderate', 'High']

discount_percentage_data = {
    'Financial support required': [2, 3, 3, 5, 10],
    'Data analysis enthusiast': [2, 3, 3, 5, 10],
    'Relevant Experience': [2, 3, 3, 5, 10],
    'Relevant Education': [2, 3, 3, 5, 10],
    'Relevance to job': [2, 3, 3, 5, 10],
    'Skill improvement need': [2, 3, 3, 5, 10],
    }
discount_df_percentages = pd.DataFrame(discount_percentage_data)

st.subheader("Discount Eligibility Survey")
#st.write("Please select the appropriate level for each criterion to see your potential discount.")

responses = {}

cols = st.columns(3)  # Create 3 columns for layout

for i, criteria in enumerate(criteria_list):
    with cols[i % 3]:  # Cycle through the columns
        response = st.selectbox(f"**{criteria}**", level_options)
        responses[criteria] = response

#st.write("---")
#st.subheader("Your Selections:")
#selection_data = [{'Criteria': c, 'Your Level': r} for c, r in responses.items()]
#selection_df = pd.DataFrame(selection_data).set_index('Criteria')
#st.dataframe(selection_df)

st.write("---")
st.subheader("Potential Discount:")

total_discount = 0
for criteria, response in responses.items():
    try:
        level_index = discount_df_levels[criteria].tolist().index(response)
        discount = discount_df_percentages[criteria].iloc[level_index]
        total_discount += discount
    except ValueError:
        st.error(f"Invalid level selected for {criteria}")
        st.stop()

st.metric("Total Discount", f"{total_discount}%")

st.write("---")
st.subheader("Discount Structure:")
combined_df = pd.DataFrame({
    'Criteria': criteria_list,
    'Level 1': [f"{discount_df_levels[col][0]} ({discount_df_percentages[col][0]}%)" for col in criteria_list],
    'Level 2': [f"{discount_df_levels[col][1]} ({discount_df_percentages[col][1]}%)" for col in criteria_list],
    'Level 3': [f"{discount_df_levels[col][2]} ({discount_df_percentages[col][2]}%)" for col in criteria_list],
    'Level 4': [f"{discount_df_levels[col][3]} ({discount_df_percentages[col][3]}%)" for col in criteria_list],
    'Level 5': [f"{discount_df_levels[col][4]} ({discount_df_percentages[col][4]}%)" for col in criteria_list],
})
st.dataframe(combined_df.set_index('Criteria'))