import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Hardcoded dictionary for comparison
hardcoded_dict = data = {
    'Qatar': 12.75,
    'Saudi Arabia': 8.84,
    'United Kingdom': 7.4,
    'Israel': 16.62,
    'Oman': 8.61,
    'Bahrain': 2.17,
    'Kuwait': 7.6,
    'Ireland': 4.03,
    'United Arab Emirates': 6.81,
    'United States': 0.46,
    'Madagascar': 23,
    'Mozambique': 18,
    'Burundi': 18,
    'Laos': 13,
    'Mali': 18,
    'Guinea-Bissau': 13,
    'Maldives': 13,
    'Bhutan': 23,
    'Ethiopia': 23,
    'Jordan': 23,
    'Libya': 23,
    'Malawi': 23,
    'Nigeria': 23,
    'Syria': 23,
    'Trinidad & Tobago': 13,
    'El Salvador': 13,
    'Grenadines': 9,
    'Aruba': 13,
    'Guatemala': 13,
    'Liberia': 13,
    'Egypt': 18,
    'Nepal': 18,
    'Papua New Guinea': 18,
    'Philippines': 18,
    'Togo': 18,
    'Tunisia': 18,
    'Turkmenistan': 18,
    'Niger': 13,
    'Somalia': 13,
    'Afghanistan': 23,
    'Bangladesh': 23,
    'Sri Lanka': 23,
    'Uganda': 23,
    'Suriname': 7.25,
    'Cote dIvoire': 13,
    'Antigua & Barbuda': 13,
    'Chad': 13,
    'Fiji': 13,
    'Kenya': 13,
    'Mongolia': 13,
    'Morocco': 13,
    'South Sudan': 13,
    'Congo': 18,
    'Jamaica': 18,
    'Kazakhstan': 18,
    'Myanmar': 18,
    'Rwanda': 18,
    'Tanzania': 18,
    'Yemen': 18,
    'Zambia': 18,
    'Lebanon': 6,
    'Guinea': 9,
    'Sierra Leone': 9,
    'St Kitts & Nevis': 9,
    'Paraguay': 7.25,
    'Malaysia': 8,
    'Moldova': 5,
    'Netherlands Antilles': 6,
    'Peru': 5,
    'Seychelles': 5,
    'Republic': 3.25,
    'Anguilla': 6,
    'Albania': 5,
    'Algeria': 13,
    'Benin': 13,
    'Bermuda': 13,
    'Cambodia': 13,
    'Cayman Islands': 13,
    'Comoros': 13,
    'Congo D.R.': 13,
    'Gabon': 13,
    'Ghana': 13,
    'Mauritania': 13,
    'Turks & Caicos Islands': 13,
    'Ukraine': 13,
    'Bulgaria': 7.25,
    'Djibouti': 6,
    'Netherlands': 7.25,
    'Argentina': 6,
    'Swaziland': 6,
    'Vietnam': 9,
    'Andorra': 5,
    'Bosnia & Herzegovina': 5,
    'Uruguay': 5,
    'Iraq': 18,
    'Kyrgyzstan': 18,
    'Palestinian Territory': 18,
    'Sudan': 18,
     'Armenia': 9,
    'Burkina Faso': 9,
    'Cameroon': 9,
    'Czech Republic': 5,
    'Ecuador': 9,
    'Georgia': 9,
    'Grenada': 9,
    'Guadeloupe': 5,
    'Guernsey': 5,
    'Haiti': 9,
    'Iceland': 5,
    'Iran': 9,
    'Lesotho': 9,
    'Norway': 5,
    'St Vincent & the Grenadines': 9,
    'Barbados': 6,
    'Belgium': 6,
    'Bolivia': 6,
    'Cape Verde': 6,
    'Croatia': 6,
    'Finland': 6,
    'Gibraltar': 6,
    'Luxembourg': 6,
    'Panama': 6,
    'Serbia': 6,
    'American Samoa': 1.25,
    'Bahamas': 3.25,
    'France': 5,
    'French Guiana': 3.25,
    'Honduras': 3.25,
    'Hong Kong': 5,
    'Hungary': 5,
    'Isle of Man': 5,
    'Latvia': 3.25,
    'St Lucia': 1.25,
    'Tokelau': 1.25,
    'Zimbabwe': 5,
    'Indonesia': 26,
    'Brazil': 1.25,
    'Brunei Darussalam': 1.25,
     'China': 1.25,
    'Colombia': 1.25,
    'Cuba': 1.25,
    'Equatorial Guinea': 5,
    'Guyana': 5,
    'Liechtenstein': 1.25,
    'Malta': 5,
    'Namibia': 1.25,
    'New Caledonia': 5,
    'New Zealand': 4.79,
    'South Africa': 1.25,
    'South Korea': 1.25,
    'Thailand': 1.25,
    'Turkey': 1.25,
    'Denmark': 3.25,
    'Greece': 3.25,
    'Lithuania': 3.25,
    'Nicaragua': 3.25,
    'Romania': 3.25,
    'Singapore': 3.25,
    'Slovakia': 3.25,
    'Spain': 3.25,
    'Sweden': 3.25,
    'Switzerland': 3.25,
    'Canada': 0.85,
    'Cyprus': 1.25,
    'Mexico': 1.25,
    'Portugal': 1.25,
    'Angola': 1.25,
    'Australia': 1.25,
    'Botswana': 1.25,
    'Central African Republic': 3.25,
    'Costa Rica': 1.25,
    'Dominican Republic': 1.25,
    'Gambia': 7.25,
    'Germany': 7.25,
    'Italy': 3.25,
    'Japan': 3.25,
    'Macau': 1.25,
    'Poland': 1.25,
    'Reunion': 3.25,
    'Senegal': 13,
    'Slovenia': 7.25,
    'Venezuela': 3.25,
    'Mauritius': 9,
    'Jersey': 3.25,
    'Puerto Rico': 1.25,
    'Pakistan': 23,
    'Russia': 23,
    'Tajikistan': 23,
    'Uzbekistan': 23,
    'Taiwan': 3.25,
    'Belize': 9,
    'Eritrea': 3.25,
    'Azerbaijan': 18
}



def compare_dicts(input_dict, hardcoded_dict):
    keys = set(input_dict.keys()).union(set(hardcoded_dict.keys()))
    comparison = []
    changes = []
    
    for key in keys:
        input_value = input_dict.get(key, 'NA')
        hardcoded_value = hardcoded_dict.get(key, 'NA')
        match = input_value == hardcoded_value
        
        # Format numbers to 3 decimal places if they are floats
        if isinstance(input_value, float):
            input_value = f"{input_value:.2f}"
        if isinstance(hardcoded_value, float):
            hardcoded_value = f"{hardcoded_value:.2f}"
            
        comparison.append((key, input_value, hardcoded_value, match))
        
        if not match:
            changes.append((key, input_value, hardcoded_value))
    
    df_comparison = pd.DataFrame(comparison, columns=['Key', 'Input Value', 'Hardcoded Value', 'Match'])
    df_changes = pd.DataFrame(changes, columns=['Key', 'Input Value', 'Hardcoded Value'])
    
    return df_comparison, df_changes

# Streamlit app
st.title("Rate comparison App")

st.write("Enter a dictionary in the format: `{'key1': 'value1', 'key2': 'value2', ...}`")

input_text = st.text_area("Input Dictionary", height=200)

if 'input_dict' not in st.session_state:
    st.session_state.input_dict = {}
if 'df_comparison' not in st.session_state:
    st.session_state.df_comparison = pd.DataFrame()
if 'df_changes' not in st.session_state:
    st.session_state.df_changes = pd.DataFrame()

if st.button("Compare"):
    try:
        input_dict = eval(input_text)
        if isinstance(input_dict, dict):
            st.session_state.input_dict = input_dict
            st.session_state.df_comparison, st.session_state.df_changes = compare_dicts(input_dict, hardcoded_dict)
        else:
            st.error("Please enter a valid dictionary.")
    except Exception as e:
        st.error(f"Error parsing input dictionary: {e}")

if not st.session_state.df_comparison.empty:
    # Display the full comparison table
    st.write("### Full Comparison Table")
    def highlight_differences(row):
        if row['Input Value'] == 'NA' or row['Hardcoded Value'] == 'NA':
            return ['background-color: red' for _ in row]
        elif not row['Match']:
            return ['background-color: yellow' for _ in row]
        else:
            return ['' for _ in row]

    st.write(st.session_state.df_comparison.style.apply(highlight_differences, axis=1))
    
    # Display the changes table or a message if no changes
    if not st.session_state.df_changes.empty:
        st.write("### Changes Table")

        # Radio buttons for selecting the view
        view_option = st.radio(
            "Select view option:",
            ('All', 'Non-Available data only', 'Input changes only'),
            horizontal=True
        )

        if view_option == 'Non-Available data only':
            df_display = st.session_state.df_changes[(st.session_state.df_changes['Input Value'] == 'NA') | (st.session_state.df_changes['Hardcoded Value'] == 'NA')]
        elif view_option == 'Input changes only':
            df_display = st.session_state.df_changes[(st.session_state.df_changes['Input Value'] != 'NA') & (st.session_state.df_changes['Hardcoded Value'] != 'NA')]
        else:
            df_display = st.session_state.df_changes

        st.write(df_display)
        
        # Visualizations
        st.write("### Data Visualizations")
        
        # Bar chart for numeric changes
        numeric_changes = df_display[pd.to_numeric(df_display['Input Value'], errors='coerce').notnull() & pd.to_numeric(df_display['Hardcoded Value'], errors='coerce').notnull()]
        if not numeric_changes.empty:
            numeric_changes['Input Value'] = pd.to_numeric(numeric_changes['Input Value'])
            numeric_changes['Hardcoded Value'] = pd.to_numeric(numeric_changes['Hardcoded Value'])
            
            chart_data = numeric_changes.melt(id_vars='Key', value_vars=['Input Value', 'Hardcoded Value'], var_name='Type', value_name='Value')
            st.bar_chart(chart_data, x='Key', y='Value', color='Type', use_container_width=True)
        
        # Add more visualizations as needed
        
    else:
        st.write("No changes found.")