import streamlit as st
import pandas as pd
from point_allocation_algorithm import calculate_points
import random

st.set_page_config(page_title="Urban Snap Leaderboard", layout="wide")
logo_path = 'LOGO.jpg' 
st.image(logo_path, width=200) 

def load_data():
    df = pd.read_csv('urban_snap_data.csv')
    return df

def save_data(df):
    df.to_csv('urban_snap_data.csv', index=False)

def generate_user_id(df):
    if df['user_id'].empty:
        return 1
    else:
        return df['user_id'].max() + 1

st.markdown(
    """
    <style>
    body {
        background-color: #f0f8ff;
        font-family: 'Arial', sans-serif;
    }
    .title {
        color: #1e90ff;
        font-size: 48px;
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 30px;
    }
    .subheader {
        color: #ff4500;
        font-size: 28px;
        margin-top: 20px;
        margin-bottom: 15px;
    }
    .stButton > button {
        background-color: #1e90ff;
        color: white;
        padding: 10px 20px;
        border-radius: 5px;
        border: none;
        transition: all 0.3s;
    }
    .stButton > button:hover {
        background-color: #4169e1;
        transform: scale(1.05);
    }
    .dataframe {
        max-height: 300px;
        overflow-y: auto;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .section {
        background-color: #a8d2f7;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    }
    </style>
    """, unsafe_allow_html=True
)

def main():
    st.markdown('<h1 class="title">🏙️ Urban Snap Leaderboard 📸</h1>', unsafe_allow_html=True)

    st.markdown("""
    <div style="background-color: #00008B; padding: 20px; border-radius: 10px; text-align: center; margin-bottom: 30px;">
        <h2 style="color: #1e90ff;">Welcome to Urban Snap!</h2>
        <p>Help improve your city by reporting issues and tracking their resolution.</p>
    </div>
    """, unsafe_allow_html=True)

    df = load_data()
    df_with_points = calculate_points(df)

    left_column, right_column = st.columns(2)

    with left_column:
        st.markdown('<div class="section">', unsafe_allow_html=True)
        st.subheader("🏆 Top 3 Urban Snappers")
        top_users = df_with_points[['user_id', 'user_name', 'points', 'timestamp']].sort_values(by='points', ascending=False).head(3)
        top_users['Rank'] = range(1, len(top_users) + 1)
        
        for _, user in top_users.iterrows():
            st.markdown(f"**{user['Rank']}.** {user['user_name']} - {user['points']} points 🌟")
        
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="section">', unsafe_allow_html=True)
        st.subheader("📊 Top 10 Leaderboard")
        top_10_users = df_with_points[['user_id', 'user_name', 'points', 'timestamp']].sort_values(by='points', ascending=False).head(10)
        top_10_users['Rank'] = range(1, len(top_10_users) + 1)
        st.dataframe(top_10_users.set_index('Rank'), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with right_column:
        st.markdown('<div class="section">', unsafe_allow_html=True)
        st.subheader("🌆 Region-wise Leaderboard")
        region_wise = df.groupby('location')['points'].sum().reset_index()
        region_wise = region_wise.sort_values(by='points', ascending=False)
        
        st.write("Total Points by Region (Bar Chart):")
        st.bar_chart(data=region_wise.set_index('location')['points'], use_container_width=True)

        selected_region = st.selectbox("Select a Region to See User Leaderboard", region_wise['location'].tolist())
        
        if selected_region and selected_region != 'Select':
            st.subheader(f"👥 User Leaderboard for {selected_region}")
            region_users = df_with_points[df_with_points['location'] == selected_region].copy()
            region_users = region_users[['user_id', 'user_name', 'points', 'timestamp']].sort_values(by='points', ascending=False)
            region_users['Area Rank'] = range(1, len(region_users) + 1)

            overall_rank = df_with_points[['user_id', 'user_name', 'points']].sort_values(by='points', ascending=False)
            overall_rank['Overall Rank'] = range(1, len(overall_rank) + 1)

            region_users = pd.merge(region_users, overall_rank[['user_name', 'Overall Rank']], on='user_name', how='left')
            region_users['Overall Rank'].fillna('N/A', inplace=True)

            st.dataframe(region_users.set_index('Area Rank'), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    
    input_col, modify_col = st.columns(2)

    with input_col:
        st.markdown('<h2 class="subheader">📝 Submit a New Complaint</h2>', unsafe_allow_html=True)

        st.markdown('<div class="section">', unsafe_allow_html=True)

        
        user_id = generate_user_id(df)
        st.text_input("Your User ID (Auto-generated)", value=user_id, disabled=True)

        user_name = st.text_input("Your Name", placeholder="Enter your Name")
        location_options = ['Ahmedabad City', 'Ambawadi', 'Ambli', 'Bhadra', 
                            'Bopal', 'Bodakdev', 'Dariyapur', 'Ellis Bridge', 
                            'Gandhinagar Highway Area', 'Ghodasar', 'Gota', 
                            'Gurukul', 'Isanpur', 'Jodhpur', 'Kalol', 'Kankaria', 
                            'Khadia', 'Lal Baug', 'Lal Darwaja', 'Maninagar', 
                            'Makarba', 'Mithakhali', 'Naroda', 'Naroda Industrial Estate', 
                            'Naranpura', 'Nikol', 'Odhav', 'Odhav Industrial Estate', 
                            'Paldi', 'Prahlad Nagar', 'Rakhiyal', 'Sabarmati', 
                            'Santej', 'Satellite', 'Shahibaug', 'Shilaj', 
                            'Thaltej', 'Vastral', 'Vastrapur', 'Vejalpur']

        location = st.selectbox("Select Your Location", location_options)
        complaints = st.number_input("Number of Complaints", min_value=0, value=0)
        approved_complaints = st.number_input("Number of Approved Complaints", min_value=0, value=0)
        resolved_complaints = st.number_input("Number of Resolved Complaints", min_value=0, value=0)
        likes = st.number_input("Number of Likes", min_value=0, value=0)

        if st.button("Submit", key="submit_button"):
            new_entry = pd.DataFrame({
                'user_id': [user_id],
                'user_name': [user_name],
                'location': [location],
                'complaints': [complaints],
                'approved_complaints': [approved_complaints],
                'resolved_complaints': [resolved_complaints],
                'likes': [likes],
                'timestamp': [pd.Timestamp.now()]
            })
            df = pd.concat([df, new_entry], ignore_index=True)
            save_data(df)
            df_with_points = calculate_points(df)
            new_user_points = df_with_points[df_with_points['user_name'] == user_name][['user_name', 'points']]
            if not new_user_points.empty:
                st.balloons()
                st.success(f"🎉 Complaint submitted successfully! Your points: {new_user_points.iloc[0]['points']}")
            else:
                st.warning("User not found. Please ensure you've entered your name correctly.")
        
        st.markdown('</div>', unsafe_allow_html=True)

    with modify_col:
        st.subheader("✏️ Modify Existing User Details")
        st.markdown('<div class="section">', unsafe_allow_html=True)
        modify_user_id = st.text_input("Enter User ID to Modify", placeholder="Enter User ID")

        if modify_user_id.isdigit() and int(modify_user_id) in df['user_id'].values:
            modify_user_id = int(modify_user_id)  
            selected_user = df[df['user_id'] == modify_user_id].iloc[0]
            st.write(f"Modifying User ID: {modify_user_id}")
            modify_user_name = selected_user['user_name']
            st.write(f"User Name: {modify_user_name}")

            modify_complaints = st.number_input("Modify Number of Complaints", min_value=0, value=int(selected_user['complaints']))
            modify_approved_complaints = st.number_input("Modify Number of Approved Complaints", min_value=0, value=int(selected_user['approved_complaints']))
            modify_resolved_complaints = st.number_input("Modify Number of Resolved Complaints", min_value=0, value=int(selected_user['resolved_complaints']))
            modify_likes = st.number_input("Modify Number of Likes", min_value=0, value=int(selected_user['likes']))

            if st.button("Update User", key="update_button"):
                df.loc[df['user_id'] == modify_user_id, ['complaints', 'approved_complaints', 'resolved_complaints', 'likes', 'timestamp']] = [
                    modify_complaints, modify_approved_complaints, modify_resolved_complaints, modify_likes, pd.Timestamp.now()]
                save_data(df)
                st.success(f"✅ User ID {modify_user_id} updated successfully!")
        elif modify_user_id and not modify_user_id.isdigit():
            st.warning("Please enter a valid User ID.")
        elif modify_user_id and int(modify_user_id) not in df['user_id'].values:
            st.warning("User ID not found. Please check and try again.")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.subheader("🎈 Fun Fact of the Day")
    fun_facts = [
        "Did you know? The average person takes about 20,000 steps a day in a city!",
        "Urban fact: Tokyo is the world's largest metropolitan area with over 37 million residents!",
        "City trivia: Singapore has the world's first night zoo, called the Night Safari!",
        "Urban planning fact: Barcelona's distinctive grid pattern was designed in the 19th century!",
        "Did you know? New York City has over 840 miles of subway tracks!"
    ]
    st.write(random.choice(fun_facts))
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
