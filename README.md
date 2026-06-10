# Car Price Prediction App

This project predicts the selling price of used cars.  
I compared several machine learning models during training, including  LinearRegression, Ridge, Lasso, DecisionTreeRegressor, RandomForestRegressor, XGBRegressor, LGBMRegressor, aur CatBoostRegressor  
After evaluating their performance, CatBoost showed the best accuracy, so I used it as the final model.

The app is built with Streamlit and provides an interactive interface where users can input car details such as Car Name year, kilometers driven, fuel type, seller type, transmission, and number of owners,present price  
Based on these inputs, the trained CatBoost model predicts the expected selling price of the car.

## Files
- `app.py` → Streamlit application
- `car_price_model.cbm` → Trained CatBoost model
- `requirements.txt` → Dependencies
- `carData.csv` → Dataset (optional)

## How to Run
1. Clone the repository
2. Install dependencies:
pip install -r requirements.txt

Code
3. Run the app:
streamlit run app.py

Code

## Deployment
The app can be deployed on Streamlit Cloud.
