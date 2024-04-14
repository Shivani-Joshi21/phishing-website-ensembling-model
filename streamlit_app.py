import pickle
import streamlit as st
from sklearn.ensemble import RandomForestClassifier

# loading the trained model
pickle_in = open('phishing_classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)

#@st.cache()
@st.cache_data()
# defining the function which will make the prediction using the data which the user inputs
def prediction(index,having_IPhaving_IP_Address,URLURL_Length,Shortining_Service,having_At_Symbol,double_slash_redirecting,Prefix_Suffix,having_Sub_Domain,SSLfinal_State,Domain_registeration_length,popUpWidnow,Iframe,age_of_domain,DNSRecord,web_traffic,Page_Rank,Google_Index,Links_pointing_to_page,Statistical_report):
    
    # Making predictions
    prediction = classifier.predict(
        [[index,having_IPhaving_IP_Address,URLURL_Length,Shortining_Service,having_At_Symbol,double_slash_redirecting,Prefix_Suffix,having_Sub_Domain,SSLfinal_State,Domain_registeration_length,popUpWidnow,Iframe,age_of_domain,DNSRecord,web_traffic,Page_Rank,Google_Index,Links_pointing_to_page,Statistical_report]])

    if prediction == 1:
        pred = 'Phishing'
    else:
        pred = 'Legitimate'
    return pred

# this is the main function in which we define our webpage
def main():
    # front end elements of the web page
    html_temp = """
    <div style ="background-color:yellow;padding:13px">
    <h1 style ="color:black;text-align:center;">Streamlit Phishing Domain Detection ML App</h1>
    </div>
    """

    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True)
    st.title('Pragyan AI Case Study @ Fuel')
    st.image("""https://altcont.fibe.in/wp-content/uploads/2020/06/rendered.png""")
    st.header('Enter the URL Details for Phishing Detection:')
    # following lines create boxes in which user can enter data required to make prediction
    index = st.number_input("Enter Index:")
    having_IPhaving_IP_Address = st.number_input("Enter having_IPhaving_IP_Address:")
    URLURL_Length = st.number_input("Enter URLURL_Length:")
    Shortining_Service = st.number_input("Enter Shortining_Service:")
    having_At_Symbol = st.number_input("Enter having_At_Symbol:")
    double_slash_redirecting = st.number_input("Enter double_slash_redirecting:")
    Prefix_Suffix = st.number_input("Enter Prefix_Suffix:")
    having_Sub_Domain = st.number_input("Enter having_Sub_Domain:")
    SSLfinal_State = st.number_input("Enter SSLfinal_State:")
    Domain_registeration_length = st.number_input("Enter Domain_registeration_length:")
    popUpWidnow = st.number_input("Enter popUpWidnow:")
    Iframe = st.number_input("Enter Iframe:")
    age_of_domain = st.number_input("Enter age_of_domain:")
    DNSRecord = st.number_input("Enter DNSRecord:")
    web_traffic = st.number_input("Enter web_traffic:")
    Page_Rank = st.number_input("Enter Page_Rank:")
    Google_Index = st.number_input("Enter Google_Index:")
    Links_pointing_to_page = st.number_input("Enter Links_pointing_to_page:")
    Statistical_report = st.number_input("Enter Statistical_report:")

    result = ""

    # when 'Predict' is clicked, make the prediction and store it
    if st.button("Predict"):
        result = prediction(index,having_IPhaving_IP_Address,URLURL_Length,Shortining_Service,having_At_Symbol,double_slash_redirecting,Prefix_Suffix,having_Sub_Domain,SSLfinal_State,Domain_registeration_length,popUpWidnow,Iframe,age_of_domain,DNSRecord,web_traffic,Page_Rank,Google_Index,Links_pointing_to_page,Statistical_report)
        st.success('The URL is {}'.format(result))

if _name=='main_':
    main()
import pickle
import streamlit as st
from sklearn.ensemble import RandomForestClassifier

# loading the trained model
pickle_in = open('phishing_classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)

#@st.cache()
@st.cache_data()
# defining the function which will make the prediction using the data which the user inputs
def prediction(index,having_IPhaving_IP_Address,URLURL_Length,Shortining_Service,having_At_Symbol,double_slash_redirecting,Prefix_Suffix,having_Sub_Domain,SSLfinal_State,Domain_registeration_length,popUpWidnow,Iframe,age_of_domain,DNSRecord,web_traffic,Page_Rank,Google_Index,Links_pointing_to_page,Statistical_report):
    
    # Making predictions
    prediction = classifier.predict(
        [[index,having_IPhaving_IP_Address,URLURL_Length,Shortining_Service,having_At_Symbol,double_slash_redirecting,Prefix_Suffix,having_Sub_Domain,SSLfinal_State,Domain_registeration_length,popUpWidnow,Iframe,age_of_domain,DNSRecord,web_traffic,Page_Rank,Google_Index,Links_pointing_to_page,Statistical_report]])

    if prediction == 1:
        pred = 'Phishing'
    else:
        pred = 'Legitimate'
    return pred

# this is the main function in which we define our webpage
def main():
    # front end elements of the web page
    html_temp = """
    <div style ="background-color:yellow;padding:13px">
    <h1 style ="color:black;text-align:center;">Streamlit Phishing Domain Detection ML App</h1>
    </div>
    """

    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True)
    st.title('Pragyan AI Case Study @ Fuel')
    st.image("""https://altcont.fibe.in/wp-content/uploads/2020/06/rendered.png""")
    st.header('Enter the URL Details for Phishing Detection:')
    # following lines create boxes in which user can enter data required to make prediction
    index = st.number_input("Enter Index:")
    having_IPhaving_IP_Address = st.number_input("Enter having_IPhaving_IP_Address:")
    URLURL_Length = st.number_input("Enter URLURL_Length:")
    Shortining_Service = st.number_input("Enter Shortining_Service:")
    having_At_Symbol = st.number_input("Enter having_At_Symbol:")
    double_slash_redirecting = st.number_input("Enter double_slash_redirecting:")
    Prefix_Suffix = st.number_input("Enter Prefix_Suffix:")
    having_Sub_Domain = st.number_input("Enter having_Sub_Domain:")
    SSLfinal_State = st.number_input("Enter SSLfinal_State:")
    Domain_registeration_length = st.number_input("Enter Domain_registeration_length:")
    popUpWidnow = st.number_input("Enter popUpWidnow:")
    Iframe = st.number_input("Enter Iframe:")
    age_of_domain = st.number_input("Enter age_of_domain:")
    DNSRecord = st.number_input("Enter DNSRecord:")
    web_traffic = st.number_input("Enter web_traffic:")
    Page_Rank = st.number_input("Enter Page_Rank:")
    Google_Index = st.number_input("Enter Google_Index:")
    Links_pointing_to_page = st.number_input("Enter Links_pointing_to_page:")
    Statistical_report = st.number_input("Enter Statistical_report:")

    result = ""

    # when 'Predict' is clicked, make the prediction and store it
    if st.button("Predict"):
        result = prediction(index,having_IPhaving_IP_Address,URLURL_Length,Shortining_Service,having_At_Symbol,double_slash_redirecting,Prefix_Suffix,having_Sub_Domain,SSLfinal_State,Domain_registeration_length,popUpWidnow,Iframe,age_of_domain,DNSRecord,web_traffic,Page_Rank,Google_Index,Links_pointing_to_page,Statistical_report)
        st.success('The URL is {}'.format(result))

if _name=='main_':
    main()
