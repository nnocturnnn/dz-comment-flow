# SPA Commenting Application

## Slow-load
Time load page with sqlite 0.2s
Time load page with free postgress 16.1s

## Overview
This Single Page Application (SPA) allows users to leave comments, similar to a forum or a comment section on a blog post. The application is built using Django and a front-end framework of your choice (Vue, React, Angular). Users can post comments, reply to them, and sort comments based on various criteria.

## Features
- **User Comments**: Users can post comments and view them in real-time.
- **Nested Comments**: Support for nested comments or replies, allowing for detailed discussions.
- **Comment Sorting**: Ability to sort comments by User Name, E-mail, and Date Added in both ascending and descending order.
- **Pagination**: Comments are paginated to enhance performance and user experience.
- **File Attachments**: Users can attach images and text files to their comments.
- **CAPTCHA Integration**: A CAPTCHA system is integrated to prevent spam.
- **XSS and SQL Injection Protection**: The application is designed with security in mind, protecting against common web vulnerabilities.
- **User Authentication**: Users can sign up, log in, and manage their profiles.
- **Real-time Updates**: Utilizing WebSocket for real-time comment updates.

## Technology Stack
- **Back-end**: Django, Django ORM
- **Front-end**: HTML/CSS/React/Bootsrap
- **Database**: MySQL/PostgreSQL/SQLite
- **Additional Tools**: Docker, Git, WebSocket
- **Security**: Implementations for protection against XSS and SQL Injection.
