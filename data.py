import csv
import random
from datetime import datetime, timedelta

def generate_user_data():
    users = [
        ("Aarav Patel", "Navrangpura"),
        ("Aisha Sharma", "Bodakdev"),
        ("Arjun Mehta", "Vastrapur"),
        ("Diya Desai", "Satellite"),
        ("Esha Gupta", "Paldi"),
        ("Kabir Singh", "Maninagar"),
        ("Kavya Joshi", "Thaltej"),
        ("Mira Shah", "Ghatlodia"),
        ("Neel Patel", "Chandkheda"),
        ("Priya Verma", "Jodhpur"),
        ("Rahul Kapoor", "Bopal"),
        ("Riya Trivedi", "Ambawadi"),
        ("Rohan Desai", "Gurukul"),
        ("Saanvi Mehta", "Naranpura"),
        ("Veer Sharma", "Sabarmati"),
        ("Zara Khan", "Ashram Road"),
        ("Advait Choudhury", "Prahlad Nagar"),
        ("Ananya Reddy", "Shilaj"),
        ("Dev Malhotra", "Vatva"),
        ("Ishaan Jain", "Gota"),
        ("Ravi Joshi", "Gota"),
        ("Sophie Patel", "Vastrapur"),
        ("Tanvi Verma", "Maninagar"),
        ("Karan Mehta", "Bodakdev"),
        ("Siddharth Sharma", "Thaltej"),
        ("Nisha Desai", "Ghatlodia"),
        ("Pooja Singh", "Naranpura"),
        ("Kartik Shah", "Chandkheda"),
        ("Rupal Gupta", "Sabarmati"),
        ("Himanshu Patel", "Ambawadi"),
        ("Anjali Reddy", "Jodhpur"),
        ("Nirav Joshi", "Prahlad Nagar"),
        ("Ritika Verma", "Shilaj"),
        ("Vikram Choudhury", "Ellis Bridge"),
        ("Sneha Mehta", "Paldi"),
        ("Amit Desai", "Vejalpur"),
        ("Arnav Gupta", "Bopal"),
        ("Maya Shah", "Gurukul"),
        ("Raghav Kapoor", "Naroda"),
        ("Ruchi Sharma", "Odhav"),
        ("Aditi Singh", "Sarkhej"),
        ("Manan Joshi", "Santej"),
        ("Deepak Sharma", "Maninagar"),
        ("Komal Patel", "Ghatlodia"),
        ("Nikita Desai", "Vastrapur"),
        ("Kunal Joshi", "Thaltej"),
        ("Isha Mehta", "Bodakdev"),
        ("Rahul Singh", "Chandkheda"),
        ("Riya Jain", "Ellis Bridge"),
        ("Sahil Kapoor", "Gota"),
        ("Geeta Reddy", "Ambawadi"),
        ("Yash Gupta", "Prahlad Nagar"),
        ("Shweta Verma", "Bopal"),
        ("Punit Mehta", "Odhav"),
        ("Anita Shah", "Naroda"),
        ("Vivek Desai", "Sarkhej"),
        ("Neha Patel", "Kankaria"),
        ("Tushar Choudhury", "Ellis Bridge"),
        ("Kriti Singh", "Gurukul"),
        ("Simran Reddy", "Ashram Road"),
        ("Saurabh Joshi", "Gandhinagar"),
        ("Rishika Bhatt", "Navrangpura"),
        ("Neelam Joshi", "Bodakdev"),
        ("Rohan Patel", "Vastrapur"),
        ("Simran Verma", "Satellite"),
        ("Kartik Iyer", "Paldi"),
        ("Naina Kapoor", "Maninagar"),
        ("Kashish Joshi", "Thaltej"),
        ("Riya Desai", "Ghatlodia"),
        ("Tanay Shah", "Chandkheda"),
        ("Disha Soni", "Jodhpur"),
        ("Siddharth Desai", "Bopal"),
        ("Himani Agarwal", "Ambawadi"),
        ("Ansh Mehta", "Gurukul"),
        ("Lavanya Singh", "Naranpura"),
        ("Viraj Khanna", "Sabarmati"),
        ("Alisha Singh", "Ashram Road"),
        ("Dhruv Choudhury", "Prahlad Nagar"),
        ("Trisha Reddy", "Shilaj"),
        ("Parth Sharma", "Vatva"),
        ("Saanvi Desai", "Gota"),
        ("Ritesh Joshi", "Gota"),
        ("Lavisha Patel", "Vastrapur"),
        ("Aarvi Shah", "Maninagar"),
        ("Yogesh Bansal", "Bodakdev"),
        ("Vani Kapoor", "Thaltej"),
        ("Nishant Mehta", "Ghatlodia"),
        ("Kavya Jain", "Naranpura"),
        ("Jay Patel", "Chandkheda"),
        ("Mitali Desai", "Sabarmati"),
        ("Vivek Singh", "Ambawadi"),
        ("Niharika Verma", "Jodhpur"),
        ("Amar Khanna", "Prahlad Nagar"),
        ("Deepa Shah", "Shilaj"),
        ("Rajesh Reddy", "Ellis Bridge"),
        ("Kunal Agarwal", "Paldi"),
        ("Snehal Joshi", "Vejalpur"),
        ("Gaurav Iyer", "Bopal"),
        ("Shruti Verma", "Gurukul"),
        ("Vikas Patel", "Naroda"),
        ("Rupal Shah", "Odhav"),
        ("Aditi Reddy", "Sarkhej"),
        ("Parul Joshi", "Santej"),
        ("Diksha Mehta", "Vatva"),
        ("Rahul Verma", "Ghatlodia"),
        ("Meenal Patel", "Sarkhej"),
        ("Siddhi Desai", "Kankaria"),
        ("Tanisha Sharma", "Gurukul"),
        ("Aman Gupta", "Gandhinagar")
    ]
    return [(i + 1, name, location) for i, (name, location) in enumerate(users)]

def generate_csv_data(filename, num_entries=1000):
    users = generate_user_data()
    
    if num_entries > len(users):
        raise ValueError("Number of entries exceeds available unique users.")

    
    random.shuffle(users)
    
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['user_id', 'user_name', 'location', 'complaints', 'approved_complaints', 'resolved_complaints', 'likes', 'timestamp']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        start_date = datetime(2023, 1, 1)
        for i in range(num_entries):
            user = users[i]
            complaints = random.randint(1, 5)
            approved_complaints = random.randint(0, complaints)
            resolved_complaints = random.randint(0, approved_complaints)
            likes = random.randint(0, 100)
            timestamp = start_date + timedelta(minutes=random.randint(0, 60 * 24 * 365)) 
            
            writer.writerow({
                'user_id': int(user[0]),  
                'user_name': user[1],
                'location': user[2],
                'complaints': complaints,
                'approved_complaints': approved_complaints,
                'resolved_complaints': resolved_complaints,
                'likes': likes,
                'timestamp': timestamp.strftime('%Y-%m-%d %H:%M:%S')  
            })

if __name__ == "__main__":
    
    generate_csv_data('urban_snap_data.csv', num_entries=len(generate_user_data()))
