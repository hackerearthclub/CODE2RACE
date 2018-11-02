function convertTimeTo24Hr(time_12hr) {
    var time = time_12hr.split(':');
    var time_24hr = '';
    if (time_12hr.substr(-2) === 'AM' && time[0] === '12') {
        time_24hr = '00';
    }
    else if (time_12hr.substr(-2) == 'PM' && time[0] < 12) {
        time_24hr = parseInt(time[0]) + 12;
    }
    else {
        time_24hr = time[0];
    }
    time_24hr += time_12hr.substr(2,6);
    return time_24hr;
}
console.log(convertTimeTo24Hr('07:05:45PM'));
