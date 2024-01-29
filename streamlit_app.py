import streamlit as st


def set_background(url):
    page_bg_img = f'''
        <style>
            body {{
                background-image: url("{url}");
                background-size: cover;
            }}
        </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Corrected URL of your background image hosted online
background_image_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSw8QoP4kp_b6R-aU0cKVt7uj3cIR7YWE_CVg&usqp=CAU'

# Call the function to set background image from the URL
set_background(background_image_url)

# Rest of your Streamlit app content goes here
# st.title('Streamlit App with Background Image')
# st.write('This is your Streamlit app content.')



# Function to predict the winner based on selected teams
def predict_winner(team1, team2):
    winners = {
        ('New Zealand', 'England'): 'England',
        ('Netherlands', 'Pakistan'): 'Pakistan',
        ('Afghanistan', 'Bangladesh'): 'Bangladesh',
        ('Sri Lanka', 'South Africa'): 'South Africa',
        ('India', 'Australia'): 'Australia',
        ('Netherlands', 'New Zealand'): 'New Zealand',
        ('Bangladesh', 'England'): 'England',
        ('Afghanistan', 'India'): 'India',
        ('Sri Lanka', 'Pakistan'): 'Pakistan',
        ('South Africa', 'Australia'): 'Australia',
        ('Bangladesh', 'New Zealand'): 'New Zealand',
        ('Afghanistan', 'England'): 'England',
        ('India', 'Pakistan'): 'India',
        ('Sri Lanka', 'Australia'): 'Australia',
        ('Netherlands', 'South Africa'): 'South Africa',
        ('Afghanistan', 'New Zealand'): 'New Zealand',
        ('Bangladesh', 'India'): 'India',
        ('Pakistan', 'Australia'): 'Australia',
        ('Netherlands', 'Sri Lanka'): 'Sri Lanka',
        ('South Africa', 'England'): 'England',
        ('New Zealand', 'India'): 'India',
        ('Afghanistan', 'Pakistan'): 'Pakistan',
        ('Bangladesh', 'South Africa'): 'South Africa',
        ('Netherlands', 'Australia'): 'Australia',
        ('Sri Lanka', 'England'): 'England',
        ('South Africa', 'Pakistan'): 'Pakistan',
        ('New Zealand', 'Australia'): 'Australia',
        ('Netherlands', 'Bangladesh'): 'Bangladesh',
        ('England', 'India'): 'India',
        ('Sri Lanka', 'Afghanistan'): 'Afghanistan',
        ('Bangladesh', 'Pakistan'): 'Pakistan',
        ('South Africa', 'New Zealand'): 'New Zealand',
        ('Sri Lanka', 'India'): 'India',
        ('Netherlands', 'Afghanistan'): 'Afghanistan',
        ('New Zealand', 'Pakistan'): 'Pakistan',
        ('England', 'Australia'): 'Australia',
        ('South Africa', 'India'): 'India',
        ('Sri Lanka', 'Bangladesh'): 'Bangladesh',
        ('Afghanistan', 'Australia'): 'Australia',
        ('Netherlands', 'England'): 'England',
        ('Sri Lanka', 'New Zealand'): 'New Zealand',
        ('Afghanistan', 'South Africa'): 'South Africa',
        ('Netherlands', 'India'): 'India',
        ('Bangladesh', 'Australia'): 'Australia',
        ('England', 'Pakistan'): 'Pakistan'
    }

    # Check if the matchup is in the dictionary
    if (team1, team2) in winners:
        return winners[(team1, team2)]
    elif (team2, team1) in winners:
        return winners[(team2, team1)]
    else:
        return "Matchup not found"


# Streamlit app
st.title('Cricket Match Winner Predictor')

# Input form - Dropdown menus for team selection
st.sidebar.header('Select Teams')

# List of teams participating in the match
teams_list = ['New Zealand', 'England', 'Netherlands', 'Pakistan', 'Afghanistan', 'Bangladesh', 'Sri Lanka',
              'South Africa', 'India', 'Australia']

# Dropdown for Team 1 selection
team1 = st.sidebar.selectbox('Select Team 1', teams_list)

# Dropdown for Team 2 selection
team2 = st.sidebar.selectbox('Select Team 2', teams_list)

# Make prediction when the button is clicked
if st.sidebar.button('Predict Winner'):
    winner = predict_winner(team1, team2)
    st.title(f'Winner: {winner}')

# Add any other content or visualizations you want to display


# Display an image from a URL
image_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSw8QoP4kp_b6R-aU0cKVt7uj3cIR7YWE_CVg&usqp=CAU'
st.image(image_url,  use_column_width=True)
