# StayEase - AWS Cloud-Native Microservices Hotel Booking Platform

A comprehensive hotel and vacation rental booking platform built with serverless microservices architecture on AWS. StayEase enables travelers to discover budget-friendly hotels, luxury resorts, and unique Airbnb-style accommodations with a seamless booking experience.


##  Architecture Overview

StayEase is designed using a microservices architecture where each service is independently deployable and scalable. The platform leverages AWS managed services to ensure high availability, performance, and cost efficiency.

![Detailed Microservices Architecture](/images/Microservices%20Architectural%20Design.png)

##  Features

- **Real-time Booking**: Instant reservation system with availability verification
- **Dynamic Pricing**: Real-time price updates and special offers
- **Multi-platform Support**: Responsive web application compatible across devices
- **Secure Payments**: Integrated payment processing with multiple payment methods
- **Review System**: User reviews and ratings for properties
- **Property Management**: Comprehensive dashboard for hotel owners and hosts

## Tech Stack

### Backend Services
- **AWS Lambda**: Serverless compute for all microservices
- **Amazon API Gateway**: RESTful API management and routing
- **Amazon DynamoDB**: High-performance NoSQL database for bookings
- **Amazon RDS (MySQL)**: Relational database for structured data
- **Amazon S3**: Object storage for images and documents
- **Amazon SES**: Email service for notifications
- **Amazon SQS**: Message queuing for asynchronous processing
- **Amazon Cognito**: User authentication and authorization
- **Amazon CloudWatch**: Monitoring and logging

### Development & Deployment
- **Serverless Framework**: Infrastructure as Code
- **Python**: Primary programming language
- **Node.js**: API Gateway integration

##  Database Schema

![ER diagram](/images/ER-diagram.png)

The application uses a hybrid database approach:
- **DynamoDB**: Fast operations for bookings and real-time data
- **RDS MySQL**: Complex queries and relational data integrity
- **S3**: Static assets and property images

##  Microservices Architecture

### Core Services

#### 1. Search Service
- **Database**: Amazon RDS (MySQL)
- **Purpose**: Handles accommodation search with complex filtering
- **Endpoints**: 
  - `GET /api/search` - Search accommodations
- **Features**: Location-based search, price filtering, availability checking

#### 2. Reservation Service  
- **Database**: Amazon DynamoDB
- **Purpose**: Manages booking lifecycle and reservations
- **Endpoints**:
  - `POST /api/reservations` - Create new reservation
  - `GET /api/reservations/{id}` - Get reservation details
- **Features**: Real-time availability, booking confirmation, email notifications

#### 3. Modification Service
- **Database**: Amazon RDS (MySQL) 
- **Purpose**: Handles booking modifications and history tracking
- **Endpoints**:
  - `PUT /api/reservations/{id}` - Update reservation details
- **Features**: Date changes, room upgrades, guest modifications

#### 4. Cancellation Service
- **Database**: Amazon DynamoDB + SQS
- **Purpose**: Processes booking cancellations and refunds
- **Endpoints**:
  - `DELETE /api/reservations/{id}` - Cancel reservation
- **Features**: Policy validation, refund processing, queue management

#### 5. User Service
- **Database**: Amazon Cognito + RDS
- **Purpose**: User management and authentication
- **Endpoints**:
  - `POST /api/users` - Register new user
  - `GET /api/users/{id}` - Get user profile
- **Features**: Social login, profile management, preferences

#### 6. Property Service
- **Database**: Amazon RDS + S3
- **Purpose**: Property and room management for hosts
- **Endpoints**:
  - `POST /api/properties` - Add new property
  - `GET /api/properties/{id}` - Get property details
- **Features**: Property listings, image management, availability control

## Project Structure

```bash
StayEase-Backend-AWS-Cloud-Native-Microservices/
├── API_Gateway.json      # API Gateway configuration
├── docs/                             # Documentation
│   ├── Property_Rooms.md
│   └── Reservation.md
├── images/                   # Architecture diagrams
│   ├── ER-diagram.png
│   ├── microservice.png
│   ├── Microservices Architectural Design.png
│   └── use-case-diagram.png
├── PostmanApiTesting/      # API testing collections
│   ├── Production.postman_environment.json
│   ├── Property And Room.postman_collection.json
│   ├── Reservation.postman_collection.json
│   └── User.postman_collection.json
├── reservation_dynamodb.csv           # Sample data
├── services/                        # Microservices
│   ├── CancellationService/
│   ├── ModificationService/
│   ├── PropertyService/
│   ├── ReservationService/
│   └── SearchService/
│   └── UserService/
└── stayease.sql                    # Database schema
```


##  License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


### **Documentation**: [docs](docs/)
