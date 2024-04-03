# Design
# databases(on
# paper, using
# draw.io or code
# comments, don't forget about constraints!) for the following scenarios. Afterwards, implement your designs via SQL commands
# (CREATE TABLE ... ) think about a few ways put data into these tables and interesting things to query from this table.
#
# Online
# Course
# Platform
# Tables:
# Users: (user_id, username, email, password)
# Courses: (course_id, title, description, instructor_id)
# Enrollments: (enrollment_id, user_id, course_id, completion_status)
# E - commerce
# Store
# Tables:
# Products: (product_id, name, description, price, stock_quantity)
# Categories: (category_id, name)(Optional - for product categorization)
# Orders: (order_id, user_id, order_date, total_price, status)
# Order_Items: (order_item_id, order_id, product_id, quantity, price)
#
# Social
# Media
# Platform
# Tables:
# Users(user_id, username, email, password)
# Posts(post_id, user_id, content, timestamp)
# Follows(follower_id, following_id)(Optional - for a follow
# relationship)
# Likes(user_id, post_id)(Optional - for likes on
# posts)
#
# Movie
# Database:
# Tables:
# Movies(movie_id, title, release_date, director, genre)
# Actors(actor_id, name, birth_date)
# Cast(movie_id, actor_id, character_name)(Many - to - Many
# relationship)
# Reviews(review_id, user_id, movie_id, rating, comment)(Optional - for user reviews)

# Online Course Platform
import sqlite3

# Create a connection to the database (or create a new one if there is none)
conn = sqlite3.connect('online_course_platform.db')

# Create a cursor to perform operations
c = conn.cursor()

# Create the Users table
c.execute('''CREATE TABLE IF NOT EXISTS Users (
             user_id INTEGER PRIMARY KEY,
             username TEXT NOT NULL,
             email TEXT NOT NULL UNIQUE,
             password TEXT NOT NULL)''')

# Create the Courses table
c.execute('''CREATE TABLE IF NOT EXISTS Courses (
             course_id INTEGER PRIMARY KEY,
             title TEXT NOT NULL,
             description TEXT,
             instructor_id INTEGER NOT NULL,
             FOREIGN KEY (instructor_id) REFERENCES Users(user_id))''')

# Create the Enrollments table
c.execute('''CREATE TABLE IF NOT EXISTS Enrollments (
             enrollment_id INTEGER PRIMARY KEY,
             user_id INTEGER NOT NULL,
             course_id INTEGER NOT NULL,
             completion_status TEXT NOT NULL,
             FOREIGN KEY (user_id) REFERENCES Users(user_id),
             FOREIGN KEY (course_id) REFERENCES Courses(course_id))''')

# Save changes
conn.commit()

# Closing the connection
conn.close()

# E-Commerce Store

import sqlite3

# Create a connection to the database (or create a new one if it doesn't exist)
conn = sqlite3.connect('e_commerce_store.db')

# Create a cursor to perform operations
c = conn.cursor()

# Create Products table
c.execute('''CREATE TABLE IF NOT EXISTS Products (
             product_id INTEGER PRIMARY KEY,
             name TEXT NOT NULL,
             description TEXT,
             price REAL NOT NULL,
             stock_quantity INTEGER NOT NULL)''')

# Create Categories table
c.execute('''CREATE TABLE IF NOT EXISTS Categories (
             category_id INTEGER PRIMARY KEY,
             name TEXT NOT NULL)''')

# Create Orders table
c.execute('''CREATE TABLE IF NOT EXISTS Orders (
             order_id INTEGER PRIMARY KEY,
             user_id INTEGER NOT NULL,
             order_date TEXT NOT NULL,
             total_price REAL NOT NULL,
             status TEXT NOT NULL,
             FOREIGN KEY (user_id) REFERENCES Users(user_id))''')

# Create Order_Items table
c.execute('''CREATE TABLE IF NOT EXISTS Order_Items (
             order_item_id INTEGER PRIMARY KEY,
             order_id INTEGER NOT NULL,
             product_id INTEGER NOT NULL,
             quantity INTEGER NOT NULL,
             price REAL NOT NULL,
             FOREIGN KEY (order_id) REFERENCES Orders(order_id),
             FOREIGN KEY (product_id) REFERENCES Products(product_id))''')

# Save changes
conn.commit()

# Close connection
conn.close()

# social media platform

import sqlite3

# Create a connection to the database (or create a new one if there is none)
conn = sqlite3.connect('social_media_platform.db')

# Create a cursor to perform operations
c = conn.cursor()

# Create the Users table
c.execute('''CREATE TABLE IF NOT EXISTS Users (
              user_id INTEGER PRIMARY KEY,
              username TEXT NOT NULL,
              email TEXT NOT NULL UNIQUE,
              password TEXT NOT NULL)''')

# Create the Posts table
c.execute('''CREATE TABLE IF NOT EXISTS Posts (
              post_id INTEGER PRIMARY KEY,
              user_id INTEGER NOT NULL,
              content TEXT NOT NULL,
              timestamp TEXT NOT NULL,
              FOREIGN KEY (user_id) REFERENCES Users(user_id))''')

# Create a Follows table
c.execute('''CREATE TABLE IF NOT EXISTS Follows (
              follower_id INTEGER NOT NULL,
              following_id INTEGER NOT NULL,
              PRIMARY KEY (follower_id, following_id),
              FOREIGN KEY (follower_id) REFERENCES Users(user_id),
              FOREIGN KEY (following_id) REFERENCES Users(user_id))''')

# Create a Likes table
c.execute('''CREATE TABLE IF NOT EXISTS Likes (
              user_id INTEGER NOT NULL,
              post_id INTEGER NOT NULL,
              PRIMARY KEY (user_id, post_id),
              FOREIGN KEY (user_id) REFERENCES Users(user_id),
              FOREIGN KEY (post_id) REFERENCES Posts(post_id))''')

# Save changes
conn.commit()

# Close the connection
conn.close()

# movie database

import sqlite3

# Create a connection to the database (or create a new one if there is none)
conn = sqlite3.connect('movie_database.db')

# Create a cursor to perform operations
c = conn.cursor()

# Create the Movies table
c.execute('''CREATE TABLE IF NOT EXISTS Movies (
              movie_id INTEGER PRIMARY KEY,
              title TEXT NOT NULL,
              release_date TEXT NOT NULL,
              director TEXT NOT NULL,
              genre TEXT NOT NULL)''')

# Create the Actors table
c.execute('''CREATE TABLE IF NOT EXISTS Actors (
              actor_id INTEGER PRIMARY KEY,
              name TEXT NOT NULL,
              birth_date TEXT NOT NULL)''')

# Create table Cast
c.execute('''CREATE TABLE IF NOT EXISTS Cast (
              movie_id INTEGER NOT NULL,
              actor_id INTEGER NOT NULL,
              character_name TEXT NOT NULL,
              PRIMARY KEY (movie_id, actor_id),
              FOREIGN KEY (movie_id) REFERENCES Movies(movie_id),
              FOREIGN KEY (actor_id) REFERENCES Actors(actor_id))''')

# Create the Reviews table
c.execute('''CREATE TABLE IF NOT EXISTS Reviews (
              review_id INTEGER PRIMARY KEY,
              user_id INTEGER NOT NULL,
              movie_id INTEGER NOT NULL,
              rating INTEGER NOT NULL,
              comment TEXT,
              FOREIGN KEY (user_id) REFERENCES Users(user_id),
              FOREIGN KEY (movie_id) REFERENCES Movies(movie_id))''')

# Save changes
conn.commit()

# Close the connection
conn.close()

