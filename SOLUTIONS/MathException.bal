import ballerina/io;
function getAgeCategory(int age) returns string|error {
    if (age < 0) {
        error e = { message: "Invalid" };
        return e;
    } else if (age <= 18) {
        return "Child";
    } else {
        return "Adult";
    }
}

public function main() {

    string ageCategory = getAgeCategory(25) but {
        string s => s,
        error e => e.message
    };
    io:println(ageCategory);

    ageCategory = getAgeCategory(-5) but {
        string s => s,
        error e => e.message
    };
    io:println(ageCategory);
    ageCategory = getAgeCategory(25) but {
        error e => e.message
    };
    io:println(ageCategory);
}

