
import ballerina/io;
import ballerina/time;
public function main() {
    time:Time time = time:currentTime();
    int currentTimeMills = time.time;
    io:println("Current system time in milliseconds: " + currentTimeMills);

    time:Time timeCreated = time:createTime(2017, 3, 28, 23, 42, 45, 554,
                                            "America/Panama");
    io:println("Created Time: " + timeCreated.toString());

    time:Time t1 = time:parse("2017-06-26T09:46:22.444-0500",
                              "yyyy-MM-dd'T'HH:mm:ss.SSSZ");
    io:println("Parsed Time: " + t1.toString());

    string standardTimeString = time.toString();
    io:println("Current system time in ISO format: " + standardTimeString);

    string customTimeString = time.format("yyyy-MM-dd-E");
    io:println("Current system time in custom format: " + customTimeString);

    int year = time.year();
    io:println("Year: " + year);

    int month = time.month();
    io:println("Month: " + month);

    int day = time.day();
    io:println("Day: " + day);

    int hour = time.hour();
    io:println("Hour: " + hour);

    int minute = time.minute();
    io:println("Minute: " + minute);

    int second = time.second();
    io:println("Second: " + second);

    int milliSecond = time.milliSecond();
    io:println("Millisecond: " + milliSecond);

    string weekday = time.weekday();
    io:println("Weekday: " + weekday);

    (year, month, day) = time.getDate();
    io:println("Date: " + year + ":" + month + ":" + day);

    (hour, minute, second, milliSecond) = time.getTime();
    io:println("Time:" + hour + ":" + minute + ":" + second + ":" + milliSecond);

    time:Time tmAdd = time.addDuration(1, 1, 0, 0, 0, 1, 0);
    io:println("After add duration: " + tmAdd.toString());

    time:Time tmSub = time.subtractDuration(1, 1, 0, 0, 0, 1, 0);
    io:println("After subtract duration: " + tmSub.toString());

    time:Time t2 = time:createTime(2017, 3, 28, 23, 42, 45, 554,
                                   "America/Panama");
    io:println("Before convert zone: " + t2.toString());
    time:Time t3 = t2.toTimezone("Asia/Colombo");
    io:println("After convert zone:" + t3.toString());
}

