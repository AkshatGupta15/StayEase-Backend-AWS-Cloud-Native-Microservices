# StayEase Reservation Service API Documentation

## Overview

The StayEase Reservation Service API enables users to create, fetch, modify, and cancel reservations for hotel properties and rooms. It supports interactions via HTTP and uses AWS Cognito JWT-based authentication. This API is built for scalability using AWS Lambda and DynamoDB, and supports integration with email notifications via AWS SES.

### Key Features

* Reserve a room for a specific property and date range
* Check existing reservations
* Modify booking details
* Cancel a reservation
* JWT-based authorization
* DynamoDB-powered scalability

---

## Authentication

All endpoints require a valid Bearer token in the `Authorization` header obtained from the User Service login.

```http
Authorization: Bearer <JWT>
```

---

## Endpoints

### 1. Create Reservation

**POST** `/api/reservations`

Creates a new reservation if the room is available.

#### Request Body

```json
{
  "property_id": "P01",
  "room_id": "R01",
  "check_in": "2025-07-01",
  "check_out": "2025-07-05",
  "user_email": "user@example.com"
}
```

#### Response (Success)

```json
{
  "message": "Reservation created",
  "reservation_id": "uuid"
}
```

#### Response (Errors)

* `409` Room already booked
* `400` Missing fields
* `500` Internal server error

---

### 2. Get Reservation

**GET** `/api/reservations/{id}`

Fetches reservation details by `reservation_id`.

#### Response (Success)

```json
{
  "reservation_id": "uuid",
  "room_id": "R01",
  "check_in": "2025-07-01",
  "check_out": "2025-07-05",
  "status": "confirmed"
}
```

#### Response (Errors)

* `404` Reservation not found
* `403` Unauthorized

---

### 3. Modify Reservation

**PATCH** `/api/modifications/{id}`

Allows users to change their check-in, check-out, or room ID.

#### Request Body

```json
{
  "check_in": "2025-07-10",
  "check_out": "2025-07-12"
}
```

#### Response (Success)

```json
{
  "message": "Reservation modified",
  "reservation_id": "uuid"
}
```

#### Response (Errors)

* `409` Conflict with existing booking
* `403` Not user's reservation
* `404` Reservation not found

---

### 4. Cancel Reservation

**POST** `/api/cancellations`

Cancels a reservation by setting its status to `cancelled`.

#### Request Body

```json
{
  "reservation_id": "uuid",
  "user_email": "user@example.com"
}
```

#### Response (Success)

```json
{
  "message": "Reservation cancelled"
}
```

#### Response (Errors)

* `403` Unauthorized
* `404` Reservation not found

---

## Tutorials

1. **Login and fetch JWT:**

   * Use `/api/users/login` with your email and password
   * Copy the `access_token` from the response

2. **Create a reservation:**

   * Send a `POST` to `/api/reservations` with token and payload

3. **Get reservation details:**

   * Send a `GET` to `/api/reservations/{id}`

4. **Modify or cancel the reservation:**

   * Use `PATCH` or `POST` to `/api/modifications/{id}` or `/api/cancellations`

---

## Examples

### Request Example

```bash
curl -X POST https://.../api/reservations \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{
    "property_id": "P01",
    "room_id": "R01",
    "check_in": "2025-07-01",
    "check_out": "2025-07-05",
    "user_email": "test@example.com"
  }'
```

---

## Glossary

* **JWT (JSON Web Token):** A secure token used for verifying identity.
* **DynamoDB:** AWS's managed NoSQL database.
* **SES (Simple Email Service):** AWS's email service used for sending confirmation emails.
* **reservation\_id:** Unique identifier for each reservation (UUID).

