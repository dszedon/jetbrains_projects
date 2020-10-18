"""
Easy Riders Bus Company

About
You've just been hired by a bus company that started actively using the Internet for business. 
Before you came, their database had been updated a few times by various employees with various levels of skill. 
Your task is to find all the mistakes they made in the database. 
Good news: you have documentation, but bad news: it's incomplete. This promises to be quite an investigation!

Learning outcomes
In addition to writing your own programs to test data consistency and correctness, 
you will practice reading documentation, working with data in JSON format, and creating lists and dictionaries. 
You will also learn how to work with set methods and regular expression library.

Stage 1
Check that the types of variables match and all the required fields are filled.

Stage 2
Check if the syntax is correct. This is a good opportunity to use the ''re'' library.

Stage 3
Make sure that the information about the bus lines and the number of stops is correct.

Stage 4
Find all departure stations, final stops, and transfer stops to fill in the missing specifications.

Stage 5
Make sure that the stops follow each other and their estimated arrival times make sense.

Stage 6
Check that there are no wrongly marked on-demand stops.

"""

# Write your awesome code here
import json, copy
from re import match
from datetime import datetime
from bustop import files


file = files()


def start(file):
    json_file = json.loads(file)

    #  stage_2(json_file)

    # stage_3(json_file)

    #  stage_4(json_file)

    # stage_5(json_file)

    stage_6(json_file)


def stage_2(json_file):
    total_errors = 0
    errors_field = {
        "bus_id": 0,
        "stop_id": 0,
        "stop_name": 0,
        "next_stop": 0,
        "stop_type": 0,
        "a_time": 0,
    }

    errors_field = check_errors(json_file, errors_field)

    for error in errors_field:
        total_errors = total_errors + errors_field[error]

    print(f"Type and required field validation: {total_errors} errors")
    errr_lst = ["stop_name", "stop_type", "a_time"]
    for error in errors_field:
        if error in errr_lst:
            print(f"{error}: {errors_field[error]}")


def check_errors(json_file, errors_field):

    stop_type = ["S", "O", "F", ""]

    for bus in json_file:
        if type(bus["bus_id"]) != int:
            errors_field["bus_id"] += 1
            # print(bus["bus_id"], "bus_id")

        if type(bus["stop_id"]) != int:
            errors_field["stop_id"] += 1
            # print(bus["stop_id"], "stop_id")

        if type(bus["stop_name"]) != str or not bus["stop_name"]:
            errors_field["stop_name"] += 1
            # print(bus["stop_name"], "stop_name")

        elif bus["stop_name"]:
            if "Boullevard" in bus["stop_name"]:
                errors_field["stop_name"] += 1

            if not bool(
                match(
                    "[A-Z]\w+\s?\w+?\s[AvenueStreetRoadBoulevard]\w+$", bus["stop_name"]
                )
            ):
                errors_field["stop_name"] += 1
                # print(bus["stop_name"], "stop_name")

        if type(bus["next_stop"]) != int:
            errors_field["next_stop"] += 1
            #  print(bus["next_stop"], "next_stop")

        if bus["stop_type"]:
            if type(bus["stop_type"]) != str or bus["stop_type"] not in stop_type:
                errors_field["stop_type"] += 1
                #  print(bus["stop_type"], "stop_type")

        if type(bus["a_time"]) != str or not bus["a_time"]:
            errors_field["a_time"] += 1
            #  print(bus["a_time"], "a_time")
        elif bus["a_time"]:
            if not bool(match("[0-2][0-9]:[0-5][0-9]\Z", bus["a_time"])):
                errors_field["a_time"] += 1
                # print(bus["a_time"], "a_time")

    return errors_field


def stage_3(json_file):
    bus_lines = {}

    for bus in json_file:
        try:
            if bus_lines[bus["bus_id"]]:
                pass
        except KeyError:
            bus_lines[bus["bus_id"]] = 0

        if bus["stop_id"]:
            bus_lines[bus["bus_id"]] += 1

    print("Line names and number of stops:")
    for x in bus_lines:
        print(f"bus_id: {x}, stops: {bus_lines[x]}")


def stage_4(json_file):
    stops_check = {}
    start_stops = set()
    double_stops = {}
    end_stops = set()
    stops_error = ""

    for bus in json_file:
        stops_check[bus["bus_id"]] = {}
        double_stops[bus["stop_name"]] = 0

    try:
        for bus in json_file:

            if bus["stop_name"]:
                double_stops[bus["stop_name"]] += 1

            if bus["stop_type"] == "S":
                start_stops.add(bus["stop_name"])
                stops_check[bus["bus_id"]].update({"start_stop": True})
            elif bus["stop_type"] == "F":
                end_stops.add(bus["stop_name"])
                stops_check[bus["bus_id"]].update({"end_stop": True})

        try:
            for buses in stops_check:
                if stops_check[buses]["start_stop"] and stops_check[buses]["end_stop"]:
                    continue
        except Exception:
            stops_error = str(buses)
            raise Exception

    except Exception:
        print(f"There is no start or end stop for the line: {stops_error}.")

    else:

        ds = copy.deepcopy(double_stops)
        for stop in ds:
            if double_stops[stop] < 2:
                double_stops.pop(stop)

        start_stops = list(start_stops)
        double_stops = list(double_stops)
        end_stops = list(end_stops)
        start_stops.sort()
        double_stops.sort()
        end_stops.sort()

        print(f"Start stops: {len(start_stops)} {start_stops}")
        print(f"Transfer stops: {len(double_stops)} {double_stops}")
        print(f"Finish stops: {len(end_stops)} {end_stops}")

    buses = {}
    prv_id = ""
    prev_stoptime = 0
    for bus in json_file:

        nxt_stoptime = int(bus["a_time"][3:])

        if prv_id != bus["bus_id"]:
            if prev_stoptime == nxt_stoptime or prev_stoptime > nxt_stoptime:
                buses[bus["bus_id"]] = bus["stop_name"]
                prv_id = bus["bus_id"]
                prev_stoptime = 0
                continue
            else:
                prev_stoptime = nxt_stoptime
        else:
            continue

    print("Arrival time test:")
    if len(buses) == 0:
        print("OK")
    else:
        for bus in buses:
            print(f"bus_id line {bus}: wrong time on station {buses[bus]}")


def stage_5(json_file):
    time_checker = {}
    prv_id = ""
    prev_stoptime = datetime.strptime("00:00", "%H:%M")

    for bus in json_file:
        nxt_stoptime = datetime.strptime(bus["a_time"], "%H:%M")
        nxt_time = bus["a_time"]

        if bool(prv_id) == False:
            prv_id = bus["bus_id"]

        if prv_id == bus["bus_id"]:
            if prev_stoptime == nxt_stoptime or prev_stoptime > nxt_stoptime:
                time_checker[bus["bus_id"]] = bus["stop_name"]
                prv_id = bus["bus_id"]
                prev_stoptime = datetime.strptime("00:00", "%H:%M")
                continue
            else:
                prev_stoptime = nxt_stoptime
        else:
            prev_stoptime = datetime.strptime("00:00", "%H:%M")
            prv_id = bus["bus_id"]
            if prev_stoptime == nxt_stoptime or prev_stoptime > nxt_stoptime:
                time_checker[bus["bus_id"]] = bus["stop_name"]
                prv_id = bus["bus_id"]
                prev_stoptime = datetime.strptime("00:00", "%H:%M")
                continue
            else:
                prev_stoptime = nxt_stoptime

    print("Arrival time test:")
    if len(time_checker) == 0:
        print("OK")
    else:
        for bus in time_checker:
            print(f"bus_id line {bus}: wrong time on station {time_checker[bus]}")


def stage_6(json_file):
    sandf_stops = ["Elm Street", "Abbey Road", "Sunset Boulevard"]

    wrong_stops = []

    for stops in json_file:
        if stops["stop_type"] == "S" or stops["stop_type"] == "F":
            sandf_stops.append(stops["stop_name"])

    for stops in json_file:
        if stops["stop_type"] == "O":
            if stops["stop_name"] in sandf_stops:
                wrong_stops.append(stops["stop_name"])

    print("On demand stops test:")
    print(*sandf_stops, sep="; ")
    if len(wrong_stops) == 0:
        print("OK")
    else:
        wrong_stops.sort()
        print(f"Wrong stop type: {wrong_stops}")


# file = input()

start(file)
