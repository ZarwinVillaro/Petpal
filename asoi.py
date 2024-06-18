from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
import mysql.connector

app = Flask(__name__)

# Function to connect to the database
def get_db_connection():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='asoi'
    )
    return conn

# Route for the login page
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check if username and password are valid
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        
        if user:
            session['logged_in'] = True
            session['username'] = username
            flash('Logged in successfully!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password. Please try again.', 'error')

    return render_template('login.html')

# Route for the home page
@app.route('/home')
def home():
    if 'logged_in' in session:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT id, name, description FROM organizations')
        organizations = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template('organizations.html', organizations=organizations)
    else:
        return redirect(url_for('login'))



# Route for the admin dashboard
@app.route('/admin_dashboard')
def admin_dashboard():
    if 'logged_in' in session:
        username = session['username']
        # Check if the user is an admin based on the database
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM admin WHERE username = %s', (username,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        if user:
            # Add code to fetch admin dashboard data if needed
            return render_template('admin_dashboard.html')
        else:
            flash('Unauthorized access!', 'error')
            return redirect(url_for('AS'))
    else:
        return redirect(url_for('AS'))




# Route for the staff dashboard
@app.route('/staff_dashboard')
def staff_dashboard():
    if 'logged_in' in session:
        username = session['username']
        # Check if the user is a staff member based on the database
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM staff WHERE username = %s', (username,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        if user:
            # Add code to fetch staff dashboard data if needed
            return render_template('staff_dashboard.html')
        else:
            flash('Unauthorized access!', 'error')
            return redirect(url_for('AS'))
    else:
        return redirect(url_for('AS'))




# Route for the login page
@app.route('/AS', methods=['GET', 'POST'])
def AS():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user_type = request.form['user_type']
        
        # Check if username and password are valid for the selected user type
        conn = get_db_connection()
        cursor = conn.cursor()
        if user_type == 'admin':
            cursor.execute('SELECT * FROM admin WHERE username = %s AND password = %s', (username, password))
        elif user_type == 'staff':
            cursor.execute('SELECT * FROM staff WHERE username = %s AND password = %s', (username, password))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        
        if user:
            session['logged_in'] = True
            session['username'] = username
            flash('Logged in successfully!', 'success')
            if user_type == 'admin':
                return redirect(url_for('admin_dashboard'))
            elif user_type == 'staff':
                return redirect(url_for('staff_dashboard'))
        else:
            flash('Invalid username or password. Please try again.', 'error')

    return render_template('AS.html')




# Update the Flask route to fetch image data along with other organization details
@app.route('/organizations')
def organizations():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT id, name, description FROM organizations')
    organizations = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('organizations.html', organizations=organizations)




# Route for displaying organization details including members, leaders, and achievements
@app.route('/organization_details/<int:organization_id>')
def organization_details(organization_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    # Fetch organization details
    cursor.execute('SELECT * FROM organizations WHERE id = %s', (organization_id,))
    organization = cursor.fetchone()
    
    # Fetch leaders for the organization
    cursor.execute('SELECT name FROM leaders WHERE organization_id = %s', (organization_id,))
    leaders = [leader['name'] for leader in cursor.fetchall()]
    
    # Fetch members for the organization
    cursor.execute('SELECT name FROM members WHERE organization_id = %s', (organization_id,))
    members = [member['name'] for member in cursor.fetchall()]
    
    # Fetch achievements for the organization
    cursor.execute('SELECT description FROM achievements WHERE organization_id = %s', (organization_id,))
    achievements = [achievement['description'] for achievement in cursor.fetchall()]
    
    cursor.close()
    conn.close()

    # Pass fetched data to the template
    return render_template('organization_details.html', organization=organization, leaders=leaders, members=members, achievements=achievements)


# Route for displaying organization members
@app.route('/organization_members/<int:organization_id>')
def organization_members(organization_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    # Fetch organization details
    cursor.execute('SELECT * FROM organizations WHERE id = %s', (organization_id,))
    organization = cursor.fetchone()
    
    # Fetch members for the organization
    cursor.execute('SELECT name FROM members WHERE organization_id = %s', (organization_id,))
    members = [member['name'] for member in cursor.fetchall()]
    
    cursor.close()
    conn.close()

    return render_template('members.html', organization=organization, members=members)


# Route for displaying organization leaders
@app.route('/organization_leaders/<int:organization_id>')
def organization_leaders(organization_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    # Fetch organization details
    cursor.execute('SELECT * FROM organizations WHERE id = %s', (organization_id,))
    organization = cursor.fetchone()
    
    # Fetch leaders for the organization
    cursor.execute('SELECT name FROM leaders WHERE organization_id = %s', (organization_id,))
    leaders = [leader['name'] for leader in cursor.fetchall()]
    
    cursor.close()
    conn.close()

    return render_template('leaders.html', organization=organization, leaders=leaders)


# Route for displaying organization achievements
@app.route('/organization_achievements/<int:organization_id>')
def organization_achievements(organization_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    # Fetch organization details
    cursor.execute('SELECT * FROM organizations WHERE id = %s', (organization_id,))
    organization = cursor.fetchone()
    
    # Fetch achievements for the organization
    cursor.execute('SELECT description FROM achievements WHERE organization_id = %s', (organization_id,))
    achievements = [achievement['description'] for achievement in cursor.fetchall()]
    
    cursor.close()
    conn.close()

    return render_template('achievement.html', organization=organization, achievements=achievements)


 
# Route for displaying the student application form
@app.route('/student_apply', methods=['GET', 'POST'])
def student_apply():
    if request.method == 'POST':
        # Extract form data
        fullName = request.form['fullName']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']
        
        try:
            # Connect to the database
            conn = get_db_connection()
            cursor = conn.cursor()
            
            # Execute SQL query to insert data into the database
            cursor.execute('INSERT INTO student_applications (fullName, email, phone, address) VALUES (%s, %s, %s, %s)', (fullName, email, phone, address))
            conn.commit()  # Commit the transaction
            
            # Close cursor and connection
            cursor.close()
            conn.close()

            # Flash success message and redirect to the same page
            flash('Your application has been submitted successfully!', 'success')
            return redirect(url_for('student_apply'))  # Redirect back to the student application form page
        
        except Exception as e:
            # Handle any exceptions that occur during database operation
            flash('An error occurred while submitting your application. Please try again later.', 'error')
            print("Database error:", e)  # Print the database error for debugging

    return render_template('student_apply.html')  # Render the student application form template

@app.route('/view_applications', methods=['GET'])
def view_applications():
    try:
        # Connect to the database
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        # Execute SQL query to fetch student applications
        cursor.execute('SELECT * FROM student_applications')
        applications = cursor.fetchall()
        
        # Close cursor and connection
        cursor.close()
        conn.close()

        return render_template('view_applications.html', applications=applications)

    except Exception as e:
        print("Database error:", e)
        flash('An error occurred while fetching applications.', 'error')
        return redirect(url_for('student_apply'))
    


    # Route for deleting an application
@app.route('/delete_application/<int:id>', methods=['DELETE'])
def delete_application(id):
    try:
        # Connect to the database
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Execute SQL query to delete application
        cursor.execute('DELETE FROM student_applications WHERE id = %s', (id,))
        conn.commit()
        
        # Close cursor and connection
        cursor.close()
        conn.close()

        return jsonify({'success': True}), 200

    except Exception as e:
        print("Database error:", e)
        return jsonify({'success': False}), 500




# Route for logging out
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    flash('Logged out successfully!', 'success')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
