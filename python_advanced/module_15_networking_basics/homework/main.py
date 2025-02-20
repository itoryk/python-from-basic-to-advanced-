from flask import make_response, Flask, request, jsonify
import sqlite3


app = Flask(__name__)


@app.route('/room', methods=['get', ])
def get_room():

    try:
        with sqlite3.connect('rooms.sqlite3') as conn:
            cursor: sqlite3.Cursor = conn.cursor()

            rooms = cursor.execute("SELECT * FROM rooms").fetchall()
            data = [
                {'roomId': room[0], 'floor': room[1], 'beds': room[2], 'guestNum': room[3], 'price': room[4]}
                for room in rooms]
            return jsonify({'rooms': data}), 200

    except Exception as err:
        return jsonify(error=str(err)), 500


@app.route('/add-room', methods=['post', ])
def add_room():
    try:

        data = request.json

        with sqlite3.connect('rooms.sqlite3') as conn:
            cursor: sqlite3.Cursor = conn.cursor()

            cursor.execute("INSERT INTO rooms (floor, beds, guestNum, price) VALUES (?,?,?,?)",
                           (data['floor'], data['beds'], data['guestNum'], data['price']))

            return 'OK', 200
    except Exception as err:
        print(err)
        return str(err), 500


@app.route('/create_booking', methods=['get'],)
def create_booking():
    with sqlite3.connect('rooms.sqlite3') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS booking(
            roomId INTEGER PRIMARY KEY,
            floor INTEGER,
            beds INTEGER,
            guestNum INTEGER,
            price INTEGER
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS rooms(    
            roomId INTEGER PRIMARY KEY,
            floor INTEGER,
            beds INTEGER,
            guestNum INTEGER,
            price INTEGER
        )
        """)
        cursor.execute("INSERT INTO rooms (floor, beds, guestNum, price) VALUES (1,2,2,100000000)")

    return 'OK', 200


@app.route('/booking', methods=['post', ])
def booking():
    try:
        data = request.json
        room_id = data.get('roomId')
        with sqlite3.connect('rooms.sqlite3') as conn:
            cursor: sqlite3.Cursor = conn.cursor()

            room = cursor.execute("SELECT * FROM rooms WHERE roomId = ?", (room_id,)).fetchone()
            if room is None:
                return jsonify(error='Room not found'), 409

            cursor.execute("INSERT INTO booking select * from rooms WHERE roomId = ?", (room_id,))

            cursor.execute("DELETE FROM rooms WHERE roomId = ?", (room_id,))
            response = make_response(
                jsonify(susses=True, bookedRoom={
                    'floor': room[1], 'beds': room[2], 'guestNum': room[3], 'price': room[4]
                }), 200
            )
            return response
    except Exception as err:
        return jsonify(error=str(err)), 500


if __name__ == "__main__":
    app.run(debug=True)