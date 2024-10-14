# Done By Adeeb Imam
# Student Number 23033904
# Module Web Development And Databases



from flask import Flask, request, render_template, redirect, flash, session, url_for, Response, send_file
from datetime import datetime
from decimal import Decimal
from database import getConnection
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.secret_key = "12345678"


def calculate_new_total_price(checkin_date, checkout_date, location, num_of_guests, room_type):
    # Connect to the database
    conn = getConnection()
    cursor = conn.cursor()

    # Calculate the duration of stay in days
    checkin_date = datetime.strptime(checkin_date, '%Y-%m-%d')
    checkout_date = datetime.strptime(checkout_date, '%Y-%m-%d')
    stay_duration = (checkout_date - checkin_date).days

    # Get the base price for the room type and location
    cursor.execute('''
        SELECT CASE
                WHEN %s IN ('4', '5', '6', '7', '8') THEN Hotel_peakseasonprice
                ELSE Hotel_notpeakseasonprice
            END AS base_price
        FROM Hotels
        WHERE Hotel_City = %s
    ''', (checkin_date.month, location))

    base_price = cursor.fetchone()[0]
    base_price = float(base_price)

    # Calculate room price based on room type
    if room_type == 'Standard':
        room_price = base_price
    elif room_type == 'Double':
        room_price = base_price * (1.2)
    elif room_type == 'Family':
        room_price = base_price * (1.5)
    else:
        flash('Invalid room type selected.', 'danger')
        return None  # Return None to handle invalid room type

    # Calculate total price based on the duration of stay, room price, and number of guests
    total_price = room_price * stay_duration * num_of_guests

    # Close the cursor and connection
    cursor.close()
    conn.close()

    # Return the calculated total price
    return round(total_price, 2)  # Round the price to 2 decimal places


def check_room_availability(hotel_id, room_type, rooms_requested):
    # Establish a connection to the database
    conn = getConnection()
    cursor = conn.cursor()

    # Determine the column to query based on room type
    room_type_column = {
        'Standard': 'Hotel_StandardRoomsAvailable',
        'Double': 'Hotel_DoubleRoomsAvailable',
        'Family': 'Hotel_FamilyRoomsAvailable'
    }.get(room_type)

    # Query the availability of the requested room type in the specified hotel
    cursor.execute(f'''
        SELECT {room_type_column}
        FROM Hotels
        WHERE Hotel_ID = %s
    ''', (hotel_id,))
    
    available_rooms = cursor.fetchone()[0]

    # Close the cursor and connection
    cursor.close()
    conn.close()

    # Return whether there are enough rooms available
    return available_rooms >= rooms_requested


# Helper function to verify admin session
def is_admin():
    return 'user_id' in session and session['user_id'] == 101  # Assuming admin user_id is 101

# Helper function to fetch hotel prices
def fetch_hotel_prices():
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute("SELECT Hotel_City, Hotel_peakseasonprice, Hotel_notpeakseasonprice FROM Hotels")
    hotels = cursor.fetchall()
    cursor.close()
    conn.close()
    
    # Create a dictionary with hotel prices
    hotel_prices = {}
    for hotel in hotels:
        city, peak_price, off_peak_price = hotel
        # Store the off-peak price as it is the lower of the two prices
        hotel_prices[city] = off_peak_price
    
    return hotel_prices

# Retrieve the list of hotel locations
def get_hotel_locations():
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('SELECT DISTINCT Hotel_City FROM Hotels')
    locations = cursor.fetchall()
    cursor.close()
    conn.close()
    return [location[0] for location in locations]

# Retrieve the list of room types
def get_room_types():
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute('SELECT Room_Type FROM Room_Types')
    room_types = cursor.fetchall()
    cursor.close()
    conn.close()
    return [room_type[0] for room_type in room_types]


# Function to retrieve hotel locations
def get_hotel_locations():
    # Establish a connection to the database
    conn = getConnection()
    cursor = conn.cursor()
    
    # Query the database for hotel locations
    cursor.execute('SELECT DISTINCT Hotel_City FROM Hotels')
    locations = cursor.fetchall()
    
    # Close the cursor and connection
    cursor.close()
    conn.close()
    
    # Return a list of locations
    return [location[0] for location in locations]

# Function to retrieve room types
def get_room_types():
    # Establish a connection to the database
    conn = getConnection()
    cursor = conn.cursor()
    
    # Query the database for room types
    cursor.execute('SELECT Room_Type FROM Room_Types')
    room_types = cursor.fetchall()
    
    # Close the cursor and connection
    cursor.close()
    conn.close()
    
    # Return a list of room types
    return [room_type[0] for room_type in room_types]


def check_user_has_bookings(user_id):
    # Connect to the database
    conn = getConnection()
    cursor = conn.cursor()

    # Query the database to check if the user has any bookings
    cursor.execute('''
        SELECT COUNT(*)
        FROM Bookings
        WHERE Guest_ID = %s
    ''', (user_id,))

    # Fetch the count
    count = cursor.fetchone()[0]

    # Close the cursor and connection
    cursor.close()
    conn.close()

    # Return True if the user has bookings (count > 0), otherwise False
    return count > 0


# Define the function to fetch booking details from the database
def get_booking_details(booking_id):
    # Establish a connection to the database
    conn = getConnection()
    cursor = conn.cursor()

    # Query the database for booking details based on the booking ID
    cursor.execute('''
        SELECT b.Booking_ID, h.Hotel_City, b.Booking_CheckIn_Date, b.Booking_CheckOut_Date, b.Booking_TotalPrice,
               b.Booking_NoOfGuest, b.Room_Type
        FROM Bookings b
        JOIN Hotels h ON b.Hotel_ID = h.Hotel_ID
        WHERE b.Booking_ID = %s
    ''', (booking_id,))

    # Fetch the booking details
    booking_details = cursor.fetchone()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    # If booking details are found, create a dictionary to return
    if booking_details:
        booking_data = {
            'Booking_ID': booking_details[0],
            'Hotel_City': booking_details[1],
            'CheckIn_Date': booking_details[2],
            'CheckOut_Date': booking_details[3],
            'TotalPrice': booking_details[4],
            'NumOfGuests': booking_details[5],
            'Room_Type': booking_details[6]
             # Assume this is the transaction ID from the left join
        }
        return booking_data
    else:
        return None  # Return None if no booking details are found

# Function to generate PDF receipt with QR code

# Route for the homepage
@app.route('/')
@app.route('/welcome')
@app.route('/home')
def homepage():
    # Retrieve the list of hotel locations and room types
    locations = get_hotel_locations()
    room_types = get_room_types()
    # Establish a connection to the database
    conn = getConnection()
    cursor = conn.cursor()
    
    # Fetch hotel prices
    cursor.execute('SELECT Hotel_City, Hotel_peakseasonprice FROM Hotels')
    hotel_prices_data = cursor.fetchall()

    # Create a dictionary mapping hotel names to prices
    hotel_prices = {city: price for city, price in hotel_prices_data}

    # Close the cursor and connection
    cursor.close()
    conn.close()
    # Render the homepage with locations and room types
    return render_template('index.html', locations=locations, room_types=room_types, hotel_prices=hotel_prices)

# Route for hotels page
@app.route('/hotels')
def hotels():
    # Establish a connection to the database
    conn = getConnection()
    cursor = conn.cursor()
    
    # Fetch hotel prices
    cursor.execute('SELECT Hotel_City, Hotel_peakseasonprice FROM Hotels')
    hotel_prices_data = cursor.fetchall()

    # Create a dictionary mapping hotel names to prices
    hotel_prices = {city: price for city, price in hotel_prices_data}

    # Close the cursor and connection
    cursor.close()
    conn.close()

    # Render the hotels listing template, passing hotel prices
    return render_template('hotels.html', hotel_prices=hotel_prices)
# Route for accounts page
@app.route('/accounts')
def accounts():
    return render_template('accounts.html')



@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        # Retrieve form data
        email = request.form['email']
        password = request.form['password']

        # Connect to the database
        conn = getConnection()
        cursor = conn.cursor()

        # Check admin credentials
        cursor.execute('SELECT Guest_ID, Guest_Password FROM Guests WHERE Guest_Email = %s AND Guest_ID = 101', (email,))
        result = cursor.fetchone()

        cursor.close()
        conn.close()

        if result:
            user_id, hashed_password = result
            if check_password_hash(hashed_password, password):
                # Login successful
                session['user_id'] = user_id
                flash('Welcome, Admin!', 'success')
                return redirect(url_for('homepage'))
            else:
                flash('Incorrect password. Please try again.', 'fail')
        else:
            flash('RESTRICTED AREA ONLY FOR ADMINS', 'fail')

    # Render the login page
    return render_template('admin.html')

# Assuming you have the necessary imports and Flask setup

@app.route('/manage_outline')
def manage_outline():
    return render_template('manage_outline.html')

# Route to view all customers
@app.route('/view_customers')
def view_customers():
    if not is_admin():
        flash('You are not authorized to access this page.', 'danger')
        return redirect(url_for('homepage'))
    
    # Connect to the database
    conn = getConnection()
    if conn is None:
        flash('Database connection error.', 'danger')
        return redirect(url_for('homepage'))
    
    cursor = conn.cursor()
    
    # Retrieve all customers from the database
    cursor.execute('SELECT Guest_ID, Guest_FirstName, Guest_LastName, Guest_Email FROM Guests')
    customers = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    # Render the admin view of customers
    return render_template('admin_view_customers.html', customers=customers)

# Route to view and edit a specific customer's details
@app.route('/admin/customer/<int:customer_id>', methods=['GET', 'POST'])
def view_customer_details(customer_id):
    if not is_admin():
        flash('You are not authorized to access this page.', 'danger')
        return redirect(url_for('homepage'))

    # Connect to the database
    conn = getConnection()
    if conn is None:
        flash('Database connection error.', 'danger')
        return redirect(url_for('homepage'))

    cursor = conn.cursor()

    if request.method == 'POST':
        if request.form.get('delete_customer'):
            # Delete all associated bookings first
            cursor.execute('DELETE FROM Bookings WHERE Guest_ID = %s', (customer_id,))
            conn.commit()

            # Now delete the customer
            cursor.execute('DELETE FROM Guests WHERE Guest_ID = %s', (customer_id,))
            conn.commit()
            
            flash('Customer deleted successfully.', 'success')
            return redirect(url_for('view_customers'))  # Redirect to the appropriate admin page
        
        # Process form submission to edit customer details
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')

        # Update the customer's details in the database
        cursor.execute('''
            UPDATE Guests
            SET Guest_FirstName = %s, Guest_LastName = %s, Guest_Email = %s
            WHERE Guest_ID = %s
        ''', (first_name, last_name, email, customer_id))

        conn.commit()
        flash('Customer details updated successfully.', 'success')

    # Retrieve the specific customer's details from the database
    cursor.execute('SELECT Guest_FirstName, Guest_LastName, Guest_Email FROM Guests WHERE Guest_ID = %s', (customer_id,))
    customer_details = cursor.fetchone()

    # Retrieve the customer's bookings with additional details: location, room type, and number of guests
    cursor.execute('''
        SELECT Booking_ID, Booking_CheckIn_Date, Booking_CheckOut_Date, Booking_TotalPrice,
               Hotel_City, Room_Type, Booking_NoOfGuest
        FROM Bookings
        JOIN Hotels ON Bookings.Hotel_ID = Hotels.Hotel_ID
        WHERE Guest_ID = %s
    ''', (customer_id,))
    customer_bookings = cursor.fetchall()

    cursor.close()
    conn.close()

    # Render the admin view of the customer's details and bookings with additional details
    return render_template('admin_customer_details.html', customer_id=customer_id, customer_details=customer_details, customer_bookings=customer_bookings)

@app.route('/admin/bookings', methods=['GET', 'POST'])
def view_all_bookings():
    # Connect to the database
    conn = getConnection()
    cursor = conn.cursor()

    if request.method == 'POST':
        # Handle delete action
        booking_id = request.form.get('booking_id')
        if booking_id:
            try:
                # Delete the booking from the database
                cursor.execute('DELETE FROM Bookings WHERE Booking_ID = %s', (booking_id,))
                conn.commit()
                flash('Booking deleted successfully.', 'success')
            except Exception as e:
                conn.rollback()
                flash(f'Error deleting booking: {e}', 'fail')
        else:
            flash('Booking ID not provided.', 'danger')
            return redirect(url_for('view_all_bookings'))

    # Fetch all bookings from the database
    cursor.execute('''
        SELECT b.Booking_ID, g.Guest_FirstName, g.Guest_LastName, h.Hotel_City,
               b.Booking_CheckIn_Date, b.Booking_CheckOut_Date, b.Room_Type,
               b.Booking_NoOfGuest, b.Booking_TotalPrice
        FROM Bookings b
        JOIN Guests g ON b.Guest_ID = g.Guest_ID
        JOIN Hotels h ON b.Hotel_ID = h.Hotel_ID
    ''')
    bookings = cursor.fetchall()

    # Close the database connection
    cursor.close()
    conn.close()

    # Render the HTML template with all bookings
    return render_template('admin_view_bookings.html', bookings=bookings)


# Route to view and edit a specific booking for a customer
@app.route('/admin/booking/<int:booking_id>', methods=['GET', 'POST'])
def edit_booking(booking_id):
    # Ensure the user is authorized
    if not is_admin():
        flash('You are not authorized to access this page.', 'fail')
        return redirect(url_for('homepage'))

    # Connect to the database
    conn = getConnection()
    if conn is None:
        flash('Database connection error.', 'fail')
        return redirect(url_for('homepage'))

    cursor = conn.cursor()

    # Fetch booking details for the specific booking ID and join with Hotels table to get hotel city
    cursor.execute('''
        SELECT b.Booking_CheckIn_Date, b.Booking_CheckOut_Date, b.Booking_TotalPrice,
               b.Booking_NoOfGuest, b.Room_Type, h.Hotel_City, b.Guest_ID
        FROM Bookings b
        JOIN Hotels h ON b.Hotel_ID = h.Hotel_ID
        WHERE b.Booking_ID = %s
    ''', (booking_id,))
    booking_details = cursor.fetchone()

    # If booking details were not found, redirect to an appropriate page
    if booking_details is None:
        flash('Booking not found.', 'fail')
        return redirect(url_for('homepage'))

    # Split booking details into individual variables
    (checkin_date, checkout_date, total_price, num_of_guests, room_type, hotel_city, guest_id) = booking_details

    # Fetch available locations and room types for the form
    locations = get_hotel_locations()
    room_types = get_room_types()

    # Handle form submission to update booking details
    if request.method == 'POST':
        # Get form data
        new_checkin_date = request.form.get('checkin_date')
        new_checkout_date = request.form.get('checkout_date')
        new_location = request.form.get('location')
        new_room_type = request.form.get('room_type')

        # Get the number of guests from the form, handling potential errors
        new_num_of_guests_str = request.form.get('number_of_guests')
        
        try:
            new_num_of_guests = int(new_num_of_guests_str)
        except ValueError:
            flash('Invalid number of guests. Please provide a valid number.', 'danger')
            return render_template('admin_edit_booking.html', booking_id=booking_id,
                                   checkin_date=checkin_date, checkout_date=checkout_date,
                                   total_price=total_price, num_of_guests=num_of_guests,
                                   room_type=room_type, hotel_city=hotel_city,
                                   locations=locations, room_types=room_types)

        # Calculate the new total price based on the updated details from the database
        new_total_price = calculate_new_total_price(new_checkin_date, new_checkout_date, new_location, new_num_of_guests, new_room_type)

        # Update the booking details in the database
        cursor.execute('''
            UPDATE Bookings
            SET Booking_CheckIn_Date = %s, Booking_CheckOut_Date = %s, Booking_NoOfGuest = %s,
                Room_Type = %s, Hotel_ID = (SELECT Hotel_ID FROM Hotels WHERE Hotel_City = %s),
                Booking_TotalPrice = %s
            WHERE Booking_ID = %s
        ''', (new_checkin_date, new_checkout_date, new_num_of_guests, new_room_type, new_location, new_total_price, booking_id))

        conn.commit()
        flash('Booking details updated successfully.', 'success')

        # Redirect to view_customer_details page after updating booking details
        return redirect(url_for('view_customer_details', customer_id=guest_id))

    # Close the database connection
    cursor.close()
    conn.close()

    # Render the edit booking page with booking details and available options
    return render_template('admin_edit_booking.html', booking_id=booking_id, checkin_date=checkin_date,
                           checkout_date=checkout_date, total_price=total_price, num_of_guests=num_of_guests,
                           room_type=room_type, hotel_city=hotel_city, locations=locations, room_types=room_types)


    
@app.route('/manage_hotels', methods=['GET', 'POST'])
def manage_hotels():
    # Ensure the user is authorized
    if not is_admin():
        flash('You are not authorized to access this page.', 'danger')
        return redirect(url_for('homepage'))

    # Connect to the database
    conn = getConnection()
    cursor = conn.cursor()

    if request.method == 'POST':
        action = request.form.get('action')
        hotel_id = request.form.get('hotel_id')

        if action == 'delete' and hotel_id:
            # Handle delete action
            try:
                cursor.execute('DELETE FROM Hotels WHERE Hotel_ID = %s', (hotel_id,))
                conn.commit()
                flash('Hotel deleted successfully.', 'success')
            except Exception as e:
                conn.rollback()
                flash(f'Error deleting hotel: {e}', 'danger')
        else:
            # Retrieve form data for updating or inserting a hotel
            hotel_city = request.form.get('hotel_city')
            hotel_rooms_str = request.form.get('hotel_rooms')
            peak_price_str = request.form.get('peak_price')
            off_peak_price_str = request.form.get('off_peak_price')

            # Convert strings to appropriate types
            try:
                hotel_rooms = int(hotel_rooms_str)
                peak_price = float(peak_price_str)
                off_peak_price = float(off_peak_price_str)
            except ValueError:
                flash('Invalid data. Please check your form.', 'danger')
                return redirect(url_for('manage_hotels'))

            # Calculate room types availability
            standard_rooms_available = int(hotel_rooms * 0.30)
            double_rooms_available = int(hotel_rooms * 0.50)
            family_rooms_available = int(hotel_rooms * 0.20)
            available_rooms = hotel_rooms

            # Determine whether to insert a new hotel or update an existing one
            if hotel_id:
                # Update existing hotel
                cursor.execute('''
                    UPDATE Hotels
                    SET Hotel_City = %s, Hotel_Rooms = %s, Hotel_peakseasonprice = %s, Hotel_notpeakseasonprice = %s,
                        Hotel_StandardRoomsAvailable = %s, Hotel_DoubleRoomsAvailable = %s, Hotel_FamilyRoomsAvailable = %s,
                        Available_Rooms = %s
                    WHERE Hotel_ID = %s
                ''', (
                    hotel_city, hotel_rooms, peak_price, off_peak_price, standard_rooms_available,
                    double_rooms_available, family_rooms_available, available_rooms, hotel_id
                ))
            else:
                # Insert a new hotel
                cursor.execute('''
                    INSERT INTO Hotels (Hotel_City, Hotel_Rooms, Hotel_peakseasonprice, Hotel_notpeakseasonprice,
                                        Hotel_StandardRoomsAvailable, Hotel_DoubleRoomsAvailable, Hotel_FamilyRoomsAvailable, Available_Rooms)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                ''', (
                    hotel_city, hotel_rooms, peak_price, off_peak_price, standard_rooms_available,
                    double_rooms_available, family_rooms_available, available_rooms
                ))

            # Commit the changes and flash a success message
            conn.commit()
            flash('Hotel information updated successfully.', 'success')

    # Fetch all hotel data for display in the form
    cursor.execute('''
        SELECT Hotel_ID, Hotel_City, Hotel_Rooms, Hotel_notpeakseasonprice, Hotel_peakseasonprice,
               Hotel_StandardRoomsAvailable, Hotel_DoubleRoomsAvailable, Hotel_FamilyRoomsAvailable,
               Available_Rooms
        FROM Hotels
    ''')
    hotels = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    # Render the 'admin_manage_hotels.html' template and pass the hotels data
    return render_template('admin_manage_hotels.html', hotels=hotels)


@app.route('/admin/reports', methods=['GET'])
def admin_reports():
    # Ensure the user is authorized
    if not is_admin():  # Implement your authorization check function
        flash('You are not authorized to access this page.', 'danger')
        return redirect(url_for('homepage'))

    # Connect to the database
    conn = getConnection()
    cursor = conn.cursor()

    try:
        # Monthly sales report
        cursor.execute('''
            SELECT DATE_FORMAT(Booking_CheckIn_Date, '%Y-%m') AS month, SUM(Booking_TotalPrice) AS total_sales
            FROM Bookings
            GROUP BY month
        ''')
        monthly_sales = cursor.fetchall()

        # Sales for each hotel report
        cursor.execute('''
            SELECT h.Hotel_City, SUM(b.Booking_TotalPrice) AS total_sales
            FROM Bookings b
            JOIN Hotels h ON b.Hotel_ID = h.Hotel_ID
            GROUP BY h.Hotel_City
        ''')
        sales_per_hotel = cursor.fetchall()

        # Top customers report
        cursor.execute('''
            SELECT g.Guest_ID, g.Guest_FirstName, g.Guest_LastName, SUM(b.Booking_TotalPrice) AS total_spending
            FROM Bookings b
            JOIN Guests g ON b.Guest_ID = g.Guest_ID
            GROUP BY g.Guest_ID, g.Guest_FirstName, g.Guest_LastName
            ORDER BY total_spending DESC
            LIMIT 10
        ''')
        top_customers = cursor.fetchall()

        # Close the cursor and connection
        cursor.close()
        conn.close()

        # Render the HTML template with the reports data
        return render_template('admin_reports.html', monthly_sales=monthly_sales, sales_per_hotel=sales_per_hotel, top_customers=top_customers)
    
    except Exception as e:
        flash(f'An error occurred while fetching reports: {e}', 'danger')
        return redirect(url_for('homepage'))

    
  


# Route for contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Route for about page
@app.route('/about')
def about():
    return render_template('about.html')

# Route for booking_form
@app.route('/booking_form')
def booking_form():
    locations = get_hotel_locations()
    room_types = get_room_types()
    # Establish a connection to the database
    conn = getConnection()
    cursor = conn.cursor()
    
    # Fetch hotel prices
    cursor.execute('SELECT Hotel_City, Hotel_peakseasonprice FROM Hotels')
    hotel_prices_data = cursor.fetchall()

    # Create a dictionary mapping hotel names to prices
    hotel_prices = {city: price for city, price in hotel_prices_data}

    # Close the cursor and connection
    cursor.close()
    conn.close()
    # Render the homepage with locations and room types
    return render_template('booking_form.html', locations=locations, room_types=room_types, hotel_prices=hotel_prices)



# Route for booking page
@app.route('/booking', methods=['POST'])
def booking():
    if 'user_id' not in session:
        flash('You must be logged in to make a booking.', 'fail')
        return redirect(url_for('accounts'))

    location = request.form.get('location')
    checkin_date_str = request.form.get('checkin')
    checkout_date_str = request.form.get('checkout')
    guests_str = request.form.get('guests')
    room_type = request.form.get('room')
    rooms_requested = 1  # Assuming each booking is for one room

    if not location or not checkin_date_str or not checkout_date_str or not guests_str or not room_type:
        flash('All fields are required.', 'fail')
        return redirect(url_for('homepage'))

    try:
        guests = int(guests_str)
        checkin_date = datetime.strptime(checkin_date_str, '%Y-%m-%d')
        checkout_date = datetime.strptime(checkout_date_str, '%Y-%m-%d')
    except ValueError:
        flash('Invalid data.', 'fail')
        return redirect(url_for('homepage'))

    current_date = datetime.now().date()
    days_in_advance = (checkin_date.date() - current_date).days

    if days_in_advance > 90:
        flash('Booking can only be made up to 3 months in advance.', 'fail')
        return redirect(url_for('homepage'))

    if checkin_date.date() < current_date:
        flash('Booking cannot be made for a date in the past.', 'fail')
        return redirect(url_for('homepage'))

    stay_duration = (checkout_date - checkin_date).days

    if stay_duration > 30:
        flash('Bookings can be made for a stay of up to 30 days.', 'fail')
        return redirect(url_for('homepage'))

    discount_percent = 0
    if 80 <= days_in_advance <= 90:
        discount_percent = 30
    elif 60 <= days_in_advance <= 79:
        discount_percent = 20
    elif 45 <= days_in_advance <= 59:
        discount_percent = 10

    conn = getConnection() 
    cursor = conn.cursor()
    cursor.execute('SELECT Hotel_ID, Hotel_City, Hotel_peakseasonprice, Hotel_notpeakseasonprice FROM Hotels WHERE Hotel_City = %s', (location,))
    hotel_info = cursor.fetchone()

    if not hotel_info:
        flash('Invalid location selected.', 'fail')
        return redirect(url_for('homepage'))

    hotel_id, hotel_city, peak_season_price, off_peak_season_price = hotel_info

    # Check room availability
    if not check_room_availability(hotel_id, room_type, rooms_requested):
        flash('Not enough rooms available for the requested room type.', 'fail')
        return redirect(url_for('homepage'))

    month = checkin_date.month
    is_peak_season = month in [4, 5, 6, 7, 8, 11, 12]
    base_price = peak_season_price if is_peak_season else off_peak_season_price

    if room_type == 'Standard':
        room_price = base_price
        max_guests = 1
    elif room_type == 'Double':
        room_price = base_price * Decimal(1.2)
        max_guests = 2
    elif room_type == 'Family':
        room_price = base_price * Decimal(1.5)
        max_guests = 4
    else:
        flash('Invalid room type selected.', 'fail')
        return redirect(url_for('homepage'))

    if guests > max_guests:
        flash('The selected room type does not accommodate the number of guests.', 'fail')
        return redirect(url_for('homepage'))

    if room_type == 'Double' and guests == 2:
        room_price += room_price * Decimal(0.1)  # Add 10% for the second guest

    total_price = room_price * stay_duration
    discount_amount = Decimal(discount_percent / 100) * total_price
    total_price -= discount_amount
    total_price = round(total_price, 2)

    return render_template(
        'booking_overview.html',
        location=hotel_city,
        stay_duration=stay_duration,
        total_price=total_price,
        room_type=room_type,
        hotel_id=hotel_id,
        checkin_date=checkin_date.strftime('%Y-%m-%d'),
        checkout_date=checkout_date.strftime('%Y-%m-%d'),
        guests=guests
    )

@app.route('/confirm_booking', methods=['POST'])
def confirm_booking():
    # Retrieve form data
    hotel_id = request.form.get('hotel_id')
    guests = request.form.get('guests')
    room_type = request.form.get('room_type')
    checkin_date = request.form.get('checkin_date')
    checkout_date = request.form.get('checkout_date')
    stay_duration = request.form.get('stay_duration')
    total_price = request.form.get('total_price')
    confirm = request.form.get('confirm')

    if confirm == 'no':
        flash('Booking canceled.', 'fail')
        return redirect(url_for('homepage'))

    if not (hotel_id and guests and room_type and checkin_date and checkout_date and stay_duration and total_price):
        flash('All fields are required.', 'fail')
        return redirect(url_for('homepage'))

    try:
        guests = int(guests)
        stay_duration = int(stay_duration)
        total_price = float(total_price)
        checkin_date = datetime.strptime(checkin_date, '%Y-%m-%d')
        checkout_date = datetime.strptime(checkout_date, '%Y-%m-%d')
    except ValueError:
        flash('Invalid form data.', 'fail')
        return redirect(url_for('homepage'))

    month = checkin_date.month
    is_peak_season = month in [4, 5, 6, 7, 8, 11, 12]

    conn = getConnection()
    cursor = conn.cursor()

    # Insert booking data
    cursor.execute('''
        INSERT INTO Bookings (
            Guest_ID, Hotel_ID, Booking_NoOfGuest, Booking_RoomsBooked, Booking_DateOfReservation,
            Booking_CheckIn_Date, Booking_CheckOut_Date, Booking_Total_nights, Booking_TotalPrice,
            Booking_currency, Booking_DiscountPrice, Booking_Peak_Season, Room_Type
        ) VALUES (
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
        )
    ''', (
        session['user_id'], hotel_id, guests, 1, datetime.today().strftime('%Y-%m-%d'),
        checkin_date.strftime('%Y-%m-%d'), checkout_date.strftime('%Y-%m-%d'), stay_duration,
        total_price, 'GBP', 'none', 'Y' if is_peak_season else 'N', room_type
    ))

    conn.commit()
    booking_id = cursor.lastrowid

    # Update available rooms
    rooms_booked = 1
    if room_type == 'Standard':
        cursor.execute('''
            UPDATE Hotels
            SET Hotel_StandardRoomsAvailable = Hotel_StandardRoomsAvailable - %s
            WHERE Hotel_ID = %s
        ''', (rooms_booked, hotel_id))

        cursor.execute('''
            UPDATE Hotels
            SET Available_Rooms = Available_Rooms - %s
            WHERE Hotel_ID = %s
        ''', (rooms_booked, hotel_id))

    elif room_type == 'Double':
        cursor.execute('''
            UPDATE Hotels
            SET Hotel_DoubleRoomsAvailable = Hotel_DoubleRoomsAvailable - %s
            WHERE Hotel_ID = %s
        ''', (rooms_booked, hotel_id))

        cursor.execute('''
            UPDATE Hotels
            SET Available_Rooms = Available_Rooms - %s
            WHERE Hotel_ID = %s
        ''', (rooms_booked, hotel_id))

    elif room_type == 'Family':
        cursor.execute('''
            UPDATE Hotels
            SET Hotel_FamilyRoomsAvailable = Hotel_FamilyRoomsAvailable - %s
            WHERE Hotel_ID = %s
        ''', (rooms_booked, hotel_id))

        cursor.execute('''
            UPDATE Hotels
            SET Available_Rooms = Available_Rooms - %s
            WHERE Hotel_ID = %s
        ''', (rooms_booked, hotel_id))

    conn.commit()

    cursor.close()
    conn.close()

    # Redirect to payment
    return redirect(url_for('payment', total_price=total_price, booking_id=booking_id))

@app.route('/payment', methods=['GET', 'POST'])
def payment():
    # Retrieve the booking ID from the URL arguments
    total_price = request.args.get('total_price')
    booking_id = request.args.get('booking_id')

    # Render the payment portal page and pass total_price and booking_id to the template
    return render_template('payment.html', total_price=total_price, booking_id = booking_id)

@app.route('/complete_payment', methods=['GET','POST'])
def complete_payment():

    flash('Booking completed successfully!', 'success')

    # Redirect the user to the homepage after a successful payment
    return redirect(url_for('homepage'))


# Define the login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Retrieve email and password from the form
        email = request.form['email']
        password = request.form['password']
        
        # Connect to the database
        conn = getConnection()
        cursor = conn.cursor()
        
        # Query the database for the user's email and password
        query = 'SELECT Guest_ID, Guest_FirstName, Guest_Password FROM Guests WHERE Guest_Email = %s'
        cursor.execute(query, (email,))
        user = cursor.fetchone()

        cursor.execute('SELECT Guest_ID, Guest_Password FROM Guests WHERE Guest_Email = %s AND Guest_ID = 101', (email,))
        result = cursor.fetchone()

        # Close the cursor and connection

        cursor.close()
        conn.close()

        if result:
            user_id, hashed_password = result
            if check_password_hash(hashed_password, password):
                # Login successful
                
                flash('UNAUTHORIZED PAGE', 'fail')
                return redirect(url_for('accounts'))

        if user:
            user_id, first_name, stored_password = user
            
            # Check the provided password against the stored hashed password
            if check_password_hash(stored_password, password):
                # If the password is correct, log the user in
                session['user_id'] = user_id
                session['email'] = email
                flash(f'Welcome, {first_name}!', 'success')
                return redirect(url_for('homepage'))
            else:
                flash('Incorrect password. Please try again.', 'fail')
        else:
            flash('Email not found. Please try again.', 'fail')

    # Render the login page
    return render_template('loginpage.html')


@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form['email']

        # Connect to the database
        conn = getConnection()
        cursor = conn.cursor()

        # Check if the email exists in the database
        cursor.execute('SELECT Guest_ID FROM Guests WHERE Guest_Email = %s', (email,))
        user = cursor.fetchone()

        if user:
            user_id = user[0]
            # Redirect to the reset password page with the user's ID
            return redirect(url_for('reset_password', user_id=user_id))
        else:
            flash('Email not found. Please try again.', 'fail')
        
        # Close the cursor and connection
        cursor.close()
        conn.close()

    return render_template('forgot_password.html')

@app.route('/reset_password/<int:user_id>', methods=['GET', 'POST'])
def reset_password(user_id):
    if request.method == 'POST':
        # Retrieve new password and confirmation
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']

        if new_password != confirm_password:
            flash('Passwords do not match. Please try again.', 'fail')
            return redirect(url_for('reset_password', user_id=user_id))

        # Hash the new password
        hashed_password = generate_password_hash(new_password)

        # Update the user's password in the database
        conn = getConnection()
        cursor = conn.cursor()
        cursor.execute('UPDATE Guests SET Guest_Password = %s WHERE Guest_ID = %s', (hashed_password, user_id))
        
        # Commit the transaction and close the cursor and connection
        conn.commit()
        cursor.close()
        conn.close()

        flash('Password updated successfully. Please log in with your new password.', 'success')
        return redirect(url_for('login'))

    return render_template('reset_password.html', user_id=user_id)

# Define the logout route
@app.route('/logout')
def logout():

    
    # Clear the user's session and redirect to the accounts page
    session.clear()
    flash('Logged out successfully.', 'success')    
    return redirect(url_for('accounts'))

# Define the signup route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Retrieve form data from the signup page
        first_name = request.form['firstName']
        last_name = request.form['lastName']
        email = request.form['userName']
        password = request.form['newPassword']
        confirm_password = request.form['reenterPassword']

        # Validate form data
        if not (first_name and last_name and email and password and confirm_password):
            flash('All fields are required.', 'fail')
            return redirect(url_for('signup'))

        if password != confirm_password:
            flash('Passwords do not match.', 'fail')
            return redirect(url_for('signup'))

        # Connect to the database
        conn = getConnection()
        cursor = conn.cursor()

        # Check if the email already exists in the database
        cursor.execute('SELECT COUNT(*) FROM Guests WHERE Guest_Email = %s', (email,))
        count = cursor.fetchone()[0]

        if count > 0:
            flash('An account with this email already exists.', 'fail')
            return redirect(url_for('signup'))

        # Hash the password before storing it in the database
        hashed_password = generate_password_hash(password)

        # Store new user data in the database
        cursor.execute('INSERT INTO Guests (Guest_FirstName, Guest_LastName, Guest_Email, Guest_Password) VALUES (%s, %s, %s, %s)',
                       (first_name, last_name, email, hashed_password))

        # Commit the transaction and close the cursor and connection
        conn.commit()
        cursor.close()
        conn.close()
        
        # Flash success message and redirect to login page
        flash('Account created successfully. Please log in.', 'success')
        return redirect(url_for('login'))

    # Render the signup page
    return render_template('signuppage.html')

@app.route('/invoice')
def invoice():
    # Get the booking ID from the URL parameters
    booking_id = request.args.get('booking_id')

    # Connect to the database
    conn = getConnection()
    cursor = conn.cursor()

    # Fetch booking details from the database
    cursor.execute('''
        SELECT b.Booking_ID, g.Guest_FirstName, g.Guest_LastName, g.Guest_Email, b.Booking_TotalPrice,
               b.Booking_CheckIn_Date, b.Booking_CheckOut_Date, b.Booking_NoOfGuest, b.Room_Type,
               b.Booking_DateOfReservation, b.Booking_Total_nights, h.Hotel_City
        FROM Bookings b
        JOIN Guests g ON b.Guest_ID = g.Guest_ID
        JOIN Hotels h ON b.Hotel_ID = h.Hotel_ID
        WHERE b.Booking_ID = %s
    ''', (booking_id,))
    booking_details = cursor.fetchone()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    # Check if booking details were found
    if not booking_details:
        flash('Booking details not found.', 'fail')
        return redirect(url_for('my_bookings'))
    
    # Combine the first name and last name to create the full name
    full_name = f"{booking_details[1]} {booking_details[2]}"

    # Pass booking details to the template
    return render_template(
        'invoice.html',
        booking_id=booking_details[0],
        full_name=full_name,
        guest_email=booking_details[3],
        amount=booking_details[4],
        checkin_date=booking_details[5],
        checkout_date=booking_details[6],
        number_of_guests=booking_details[7],
        room_type=booking_details[8],
        date_of_reservation=booking_details[9],
        days_of_stay=booking_details[10],
        location = booking_details[11]
        
    )


@app.route('/my_bookings')
def my_bookings():
    # Check if the user is logged in
    if 'user_id' not in session:
        flash('You must be logged in to view your bookings.', 'danger')
        return redirect(url_for('login'))

    # Connect to the database
    conn = getConnection()
    cursor = conn.cursor()

    # Retrieve the logged-in user's ID from the session
    user_id = session['user_id']

    # Query the database to retrieve the bookings specific to the logged-in user
    cursor.execute('''
        SELECT b.Booking_ID, h.Hotel_City, b.Booking_CheckIn_Date, b.Booking_CheckOut_Date, b.Booking_TotalPrice
        FROM Bookings b
        JOIN Hotels h ON b.Hotel_ID = h.Hotel_ID
        WHERE b.Guest_ID = %s
    ''', (user_id,))

    # Fetch the results from the query
    bookings = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    # Render the "My Bookings" page and pass the bookings data to the template
    return render_template('my_bookings.html', bookings=bookings)

@app.route('/cancel_booking/<int:booking_id>', methods=['POST'])
def cancel_booking(booking_id):
    if 'user_id' not in session:
        flash('You must be logged in to cancel a booking.', 'danger')
        return redirect(url_for('login'))

    conn = getConnection()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT Booking_CheckIn_Date, Room_Type, Booking_RoomsBooked, Hotel_ID, Booking_TotalPrice
        FROM Bookings
        WHERE Booking_ID = %s AND Guest_ID = %s
    ''', (booking_id, session['user_id']))

    booking_info = cursor.fetchone()

    if not booking_info:
        flash('Booking not found or you are not authorized to cancel this booking.', 'danger')
        cursor.close()
        conn.close()
        return redirect(url_for('my_bookings'))

    checkin_date, room_type, rooms_booked, hotel_id, total_price = booking_info
    current_date = datetime.now().date()
    days_to_checkin = (checkin_date - current_date).days

    if days_to_checkin > 60:
        cancellation_charge = Decimal(0)  # No charges before 60 days
    elif 30 <= days_to_checkin <= 60:
        cancellation_charge = total_price * Decimal(0.5)  # 50% charge between 30 and 60 days
    else:
        cancellation_charge = total_price  # 100% charge within 30 days

    if room_type == 'Standard':
        cursor.execute('''
            UPDATE Hotels
            SET Hotel_StandardRoomsAvailable = Hotel_StandardRoomsAvailable + %s
            WHERE Hotel_ID = %s
        ''', (rooms_booked, hotel_id))

        cursor.execute('''
            UPDATE Hotels
            SET Available_Rooms  = Available_Rooms + %s
            WHERE Hotel_ID = %s
        ''', (rooms_booked, hotel_id))

    elif room_type == 'Double':
        cursor.execute('''
            UPDATE Hotels
            SET Hotel_DoubleRoomsAvailable = Hotel_DoubleRoomsAvailable + %s
            WHERE Hotel_ID = %s
        ''', (rooms_booked, hotel_id))

        cursor.execute('''
            UPDATE Hotels
            SET Available_Rooms  = Available_Rooms + %s
            WHERE Hotel_ID = %s
        ''', (rooms_booked, hotel_id))

    elif room_type == 'Family':
        cursor.execute('''
            UPDATE Hotels
            SET Hotel_FamilyRoomsAvailable = Hotel_FamilyRoomsAvailable + %s
            WHERE Hotel_ID = %s
        ''', (rooms_booked, hotel_id))
        cursor.execute('''
            UPDATE Hotels
            SET Available_Rooms  = Available_Rooms + %s
            WHERE Hotel_ID = %s
        ''', (rooms_booked, hotel_id))

    cursor.execute('DELETE FROM Bookings WHERE Booking_ID = %s', (booking_id,))
    conn.commit()

    cursor.close()
    conn.close()

    flash(f'Booking canceled successfully. A charge of £{cancellation_charge:.2f} was incurred.', 'success')
    return redirect(url_for('my_bookings'))

# Define the route to generate the PDF receipt


if __name__ == '__main__':
    # Run the Flask application in debug mode
    app.run(debug=True)