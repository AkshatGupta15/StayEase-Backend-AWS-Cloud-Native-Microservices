# StayEase Property API Documentation

## Overview

The Property Service in the StayEase platform allows authenticated users (typically admins or hosts) to manage properties and their rooms. It supports CRUD operations for properties and rooms, and handles image uploads with pre-signed S3 URLs.

Base URL: `https://06bje10q2d.execute-api.us-east-1.amazonaws.com`

Authentication: All routes require a valid Bearer JWT token in the `Authorization` header.

---

## Endpoints

### 1. Create Property

* **URL**: `POST /api/properties`
* **Description**: Creates a new property.
* **Request Headers**: `Authorization: Bearer <token>`
* **Body** (JSON):

```json
{
  "id": "P01",
  "name": "StayEase",
  "location": "Goa",
  "description": "Beachside hotel"
}
```

* **Success Response**:

  * Code: `201 Created`
  * Body: `{ "message": "Property created successfully" }`

### 2. Get Property by ID

* **URL**: `GET /api/properties/{property_id}`
* **Description**: Fetch a single property by ID.
* **Success Response**:

  * Code: `200 OK`
  * Body: Property object

### 3. Update Property

* **URL**: `PUT /api/properties/{property_id}`
* **Description**: Update property details.
* **Request Headers**: `Authorization`
* **Body**:

```json
{
  "name": "StayEase Deluxe",
  "location": "Goa",
  "description": "Upgraded amenities"
}
```

* **Success Response**: `200 OK`

### 4. Delete Property

* **URL**: `DELETE /api/properties/{property_id}`
* **Description**: Deletes a property.
* **Request Headers**: `Authorization`
* **Success Response**: `200 OK`

---

## Room Endpoints

### 5. Create Room under Property

* **URL**: `POST /api/properties/{property_id}/rooms`
* **Description**: Adds a room to a property.
* **Body**:

```json
{
  "room_type": "Deluxe",
  "price_per_night": 300,
  "available": true,
  "max_guests": 4
}
```

* **Response**: `201 Created`

### 6. List Rooms for a Property

* **URL**: `GET /api/properties/{property_id}/rooms`
* **Response**: Array of room objects

### 7. Get Room by ID

* **URL**: `GET /api/properties/{property_id}/rooms/{room_id}`
* **Response**: Room object

### 8. Update Room

* **URL**: `PUT /api/properties/{property_id}/rooms/{room_id}`
* **Body**:

```json
{
  "room_type": "Executive Suite",
  "price_per_night": 350,
  "available": false,
  "max_guests": 3
}
```

* **Response**: `200 OK`

### 9. Delete Room

* **URL**: `DELETE /api/properties/{property_id}/rooms/{room_id}`
* **Response**: `200 OK`

---

## Image Upload for Rooms

### 10. Generate Upload URL

* **URL**: `POST /api/properties/{property_id}/rooms/{room_id}/image-url`
* **Body**:

```json
{
  "filename": "room1.jpg"
}
```

* **Response**:

```json
{
  "upload_url": "<signed_s3_url>",
  "public_url": "https://..."
}
```


###  Upload using Postman



### 11. Upload Image on that Upload URL


1. Open a new **`PUT`** request tab in Postman.
2. Paste the entire `upload_url` you received in the URL field.
3. Go to the **Body** tab.
4. Choose **binary**.
5. Click "Select File" and choose your `.jpg` or `.png` image.
6. In **Headers**, add:

   ```
   Content-Type: image/jpeg
   ```
7. Click **Send**.

If successful, S3 will return a `200 OK` response and the image will be publicly accessible at the `public_url` returned from prevoius api call to get signed url

```bash

 {
  "upload_url": "<signed_s3_url>",
  "public_url": "https://..."
}
```

* **Response**: `200 OK`

---

## Examples

### Create Property

```bash
curl -X POST $BASE_URL/api/properties \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
        "id": "P01",
        "name": "StayEase",
        "location": "Goa",
        "description": "Beachside hotel"
      }'
```

### Get All Rooms in Property

```bash
curl $BASE_URL/api/properties/P01/rooms
```

---

## Glossary

* `property_id`: Unique identifier for a property (e.g., P01)
* `room_id`: Room ID like R01 (usually auto-incremented or UUID)
* `available`: Boolean indicating if room is bookable
* `max_guests`: Maximum number of guests supported

---

