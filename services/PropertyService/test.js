{
  "test_events" = [
    {
      "name": "Create Property",
      "event": {
        "routeKey": "POST /api/properties",
        "body": "{\"id\": \"P01\", \"name\": \"Hotel Sunshine\", \"location\": \"Goa\", \"description\": \"Sea-facing deluxe hotel\"}"
      }
    },
    {
      "name": "Get Property",
      "event": {
        "routeKey": "GET /api/properties/P01",
        "pathParameters": { "id": "P01" }
      }
    },
    {
      "name": "Update Property",
      "event": {
        "routeKey": "PUT /api/properties/P01",
        "pathParameters": { "id": "P01" },
        "body": "{\"name\": \"Hotel Paradise\", \"location\": \"Mumbai\", \"description\": \"Newly renovated beach hotel\"}"
      }
    },
    {
      "name": "Delete Property",
      "event": {
        "routeKey": "DELETE /api/properties/P01",
        "pathParameters": { "id": "P01" }
      }
    },

    {
      "name": "Create Room",
      "event": {
        "routeKey": "POST /api/properties/P01/rooms",
        "pathParameters": { "property_id": "P01" },
        "body": "{\"room_type\": \"Deluxe King\", \"price_per_night\": 200, \"available\": true, \"max_guests\": 3}"
      }
    },
    {
      "name": "List Rooms",
      "event": {
        "routeKey": "GET /api/properties/P01/rooms",
        "pathParameters": { "property_id": "P01" }
      }
    },
    {
      "name": "Get Room",
      "event": {
        "routeKey": "GET /api/properties/P01/rooms/1",
        "pathParameters": { "property_id": "P01", "id": "1" }
      }
    },
    {
      "name": "Update Room",
      "event": {
        "routeKey": "PUT /api/properties/P01/rooms/1",
        "pathParameters": { "property_id": "P01", "id": "1" },
        "body": "{\"room_type\": \"Executive Suite\", \"price_per_night\": 250, \"available\": false, \"max_guests\": 4}"
      }
    },
    {
      "name": "Delete Room",
      "event": {
        "routeKey": "DELETE /api/properties/P01/rooms/1",
        "pathParameters": { "property_id": "P01", "id": "1" }
      }
    },

    {
      "name": "Get Image Upload URL",
      "event": {
        "routeKey": "POST /api/properties/P01/rooms/1/image-url",
        "pathParameters": {
          "property_id": "P01",
          "id": "1"
        },
        "body": "{\"filename\": \"room1.jpg\"}"
      }
    },
    {
      "name": "Update Image URL",
      "event": {
        "routeKey": "PUT /api/properties/P01/rooms/1/image",
        "pathParameters": { "property_id": "P01", "id": "1" },
        "body": "{\"image_url\": \"https://stayease-room-images.s3.amazonaws.com/rooms/1/room1.jpg\"}"
      }
    }
  ]
}
