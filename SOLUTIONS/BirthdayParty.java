import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;

class BirthdayParty {
    public static void main(String[] args) {
        List<BirthdayGuest> birthdayGuestList = new ArrayList<>();
        birthdayGuestList.add(new BirthdayGuest(1, 2));
        birthdayGuestList.add(new BirthdayGuest(2, 2));
        birthdayGuestList.add(new BirthdayGuest(2, 3));

        System.out.println(Integer.toString(query(birthdayGuestList, 1)));
        System.out.println(Integer.toString(query(birthdayGuestList, 2)));
        System.out.println(Integer.toString(query(birthdayGuestList, 3)));
    }

    public static int query(List<BirthdayGuest> birthdayGuestList, int time) {
        int count = 0;
        for (BirthdayGuest guest : birthdayGuestList) {
            if (time >= guest.getArrivalTime() && time <= guest.getDepartureTime()) {
                count ++;
            }
        }
        return count;
    }
}

class BirthdayGuest {
    private int arrivalTime, departureTime;

    BirthdayGuest(int arrivalTime, int departureTime) {
        this.arrivalTime = arrivalTime;
        this.departureTime = departureTime;
    }

    public int getArrivalTime() {
        return this.arrivalTime;
    }

    public int getDepartureTime() {
        return this.departureTime;
    }

    public String toString() {
        String out = "BirthdayGuest(%d, %d)";
        return String.format(out, this.getArrivalTime(), this.getDepartureTime());
    }
}

