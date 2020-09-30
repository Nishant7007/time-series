import pickle

dict = {
'commodity':{"Garlic":['MadhyaPradesh','UttarPradesh'],
"Ginger(Green)":['NCTofDelhi','WestBengal'],
"Lentil(Masur)(Whole)":['MadhyaPradesh','UttarPradesh','WestBengal'],
"Onion":['Karnataka','Maharashtra','NCTofDelhi','UttarPradesh'],
"Potato":['HimachalPradesh','MadhyaPradesh','NCTofDelhi','Punjab','UttarPradesh','WestBengal'],
"Tomato":['Karnataka','Maharashtra','NCTofDelhi','UttarPradesh'],
"Wheat":['Rajasthan','UttarPradesh']},

'commodityFiles' : {"Garlic":['Madhya Pradesh','Uttar Pradesh'],
"Ginger(Green)":['NCT of Delhi','West Bengal'],
"Lentil (Masur)(Whole)":['Madhya Pradesh','Uttar Pradesh','West Bengal'],
"Onion":['Karnataka','Maharashtra','NCT of Delhi','Uttar Pradesh'],
"Potato":['Himachal Pradesh','Madhya Pradesh','NCT of Delhi','Punjab','Uttar Pradesh','West Bengal'],
"Tomato":['Karnataka','Maharashtra','NCT of Delhi','Uttar Pradesh'],
"Wheat":['Rajasthan','Uttar Pradesh']},

'Onion_Mandis' : { "Karnataka" : ["Bangalore", "Belgaum", "Davangere", "Hubli (Amaragol)"],
                "Maharashtra" : ["Kolhapur", "Solapur", "Pune", "Sangamner", "Karad", "Pimpalgaon", "Lasalgaon"],
                "NCT of Delhi" : ["Azadpur", "Shahdara"], "Uttar Pradesh" : ["Bareilly", "Basti", "Gonda", "Muradabad", "Rampur", "Lakhimpur", "Pilibhit", "Lucknow"]},


'Potato_Mandis' : { "Himachal Pradesh" : ["Bhuntar", "Kullu"],
                "Madhya Pradesh": ["Haatpipliya", "Burhanpur(F&V)", "Dewas(F&V)", "Jabalpur(F&V)", "Bhopal(F&V)", "Lashkar(F&V)", "Sagar(F&V)", "Sanwer", "Dhamnod"],
                "NCT of Delhi" : ["Azadpur", "Shahdara"],
                "Uttar Pradesh" : ["Bareilly", "Basti", "Faizabad", "Muradabad", "Rampur", "Lakhimpur", "Pilibhit"],
                "Punjab" : ["Dasuya", "Dera Bassi", "Kharar", "Zira", "Malerkotla", "Ajnala"],
                "West Bengal" : ["Bishnupur(Bankura)", "Ramkrishanpur(Howrah)", "Sheoraphuly", "Durgapur", "Katwa", "Jangipur", "Asansol", "Uluberia", "Islampur"]},

'Ginger(Green)_Mandis' : {"NCT of Delhi" : ["Azadpur"],
                        "West Bengal" : ["Siliguri"]},

'Garlic_Mandis' : { "Madhya Pradesh" : ["Badnawar(F&V)", "Bhopal(F&V)", "Piplya"],
                "Uttar Pradesh" : ["Allahabad", "Basti", "Etawah", "Saharanpur"]},

'Wheat_Mandis' : {"Rajasthan" : ["Bijay Nagar", "Bayana", "Kherli", "Tonk", "Alwar", "Kota"],
                "Uttar Pradesh" : ["Azamgarh", "Bahraich", "Basti", "Etawah", "Faizabad", "Fatehpur", "Gazipur", "Muradabad", "Saharanpur", "Unnao", "Kannauj", "Pilibhit"]},

'Lentil(Masur)(Whole)_Mandis' : { "Madhya Pradesh" : ["Katni", "Kalapipal"],
                                "Uttar Pradesh" : ["Faizabad", "Muradabad", "Tamkuhi Road", "Lakhimpur", "Pilibhit", "Madhoganj", "Atarra"],
                                "West Bengal" : ["English Bazar", "Durgapur", "Asansol", "Siliguri", "Balarampur"]},


'Tomato_Mandis' : {"Karnataka" : ["Chikkamagalore", "Mysore (Bandipalya)", "Chickkaballapura", "Kolar", "Doddaballa Pur", "Srinivasapur", "Mulabagilu", "Channapatana", "Chintamani", "Ramanagara"],
                "Maharashtra" : ["Kolhapur", "Mumbai", "Solapur", "Khed(Chakan)", "Pandharpur", "Pune", "Satara", "Karad", "Shrirampur", "Kamthi", "Navapur", "Vai"],
                "NCT of Delhi" : ["Azadpur", "Shahdara"],
                "Uttar Pradesh" : ["Faizabad", "Muradabad", "Pilibhit"]},

'MonthsDict' : {
'Garlic': {'Madhya Pradesh': ['June', '2020'], 'Uttar Pradesh': ['June', '2020']},
'Ginger(Green)': {'NCT of Delhi': ['June', '2020'], 'West Bengal': ['June', '2020']},
'Lentil (Masur)(Whole)': {'Madhya Pradesh': ['June', '2020'], 'Uttar Pradesh': ['June', '2020'], 'West Bengal': ['June', '2020']},
'Onion': {'Karnataka': ['June', '2020'], 'Maharashtra': ['June', '2020'], 'NCT of Delhi': ['June', '2020'], 'Uttar Pradesh': ['June', '2020']},
'Potato': {'Himachal Pradesh': ['June', '2020'], 'Madhya Pradesh': ['June', '2020'], 'NCT of Delhi': ['June', '2020'], 'Punjab': ['June', '2020'], 'Uttar Pradesh': ['June', '2020'], 'West Bengal': ['June', '2020']},
'Tomato': {'Karnataka': ['June', '2020'], 'Maharashtra': ['June', '2020'], 'NCT of Delhi': ['June', '2020'], 'Uttar Pradesh': ['June', '2020']},
'Wheat': {'Rajasthan': ['June', '2020'], 'Uttar Pradesh': ['June', '2020']}}

}

file = open('myDicts.p', 'wb')
pickle.dump(dict,file)
