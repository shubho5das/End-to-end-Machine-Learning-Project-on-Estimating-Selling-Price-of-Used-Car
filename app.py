import streamlit as st
import pickle
model = pickle.load(open('RF_price_predicting_model.pkl','rb'))

def main():
    string = "Car Price Predictor"
    st.set_page_config(page_title=string) 
    st.title("Car Price Predictor")
    st.markdown("##### Planning to sell your car, but don't know the price you'll get for it?\n##### Don't worry, you are at the right place. Answer the questions below, and know the current valuation of your car.")
    st.image(
            "https://imgd.aeplcdn.com/664x374/cw/cars/discontinued/maruti-suzuki/800-1986-1997.jpg",
            width=400, # Manually Adjust the width of the image as per requirement
        )
    st.write('')
    st.write('')
    years = st.number_input('In which year did you purchase the car?',1990, 2021, step=1, key ='year')
    Years_old = 2021-years
    
    Present_Price = st.number_input('What was the showroom price of the car at the time of purchase ?(in ₹lakhs)', 0.00, 50.00, step=0.5, key ='present_price')

    Kms_Driven = st.number_input('How many kilometers has the car run?', 0.00, 500000.00, step=500.00, key ='drived')

    Owner = st.radio("How many owners did the car have?", (0, 1, 3), key='owner')

    Fuel_Type_Petrol = st.selectbox('What is the fuel type of the car ?',('Petrol','Diesel', 'CNG'), key='fuel')
    if(Fuel_Type_Petrol=='Petrol'):
        Fuel_Type_Petrol=1
        Fuel_Type_Diesel=0
    elif(Fuel_Type_Petrol=='Diesel'):
        Fuel_Type_Petrol=0
        Fuel_Type_Diesel=1
    else:
        Fuel_Type_Petrol=0
        Fuel_Type_Diesel=0

    Seller_Type_Individual = st.selectbox('Are you a dealer or an individual ?', ('Dealer','Individual'), key='dealer')
    if(Seller_Type_Individual=='Individual'):
        Seller_Type_Individual=1
    else:
        Seller_Type_Individual=0	

    Transmission_Mannual = st.selectbox('What is the transmission type ?', ('Manual','Automatic'), key='manual')
    if(Transmission_Mannual=='Mannual'):
        Transmission_Mannual=1
    else:
        Transmission_Mannual=0

    if st.button("Estimate Price", key='predict'):
        try:
            Model = model  #get_model()
            prediction = Model.predict([[Present_Price, Kms_Driven, Owner, Years_old, Fuel_Type_Diesel, Fuel_Type_Petrol, Seller_Type_Individual, Transmission_Mannual]])
            output = round(prediction[0],2)
            if output<0:
                st.warning("You will be not able to sell this car !!")
            else:
                st.success("Estimated Selling Price: {} lakhs".format(output))
        except:
            st.warning("Opps!! Something went wrong\nTry again")

if __name__ == '__main__':
    main()
