import java.lang.reflect.*;

public class Reflection {

	public static void main(String[] args) {
		
		Field[] fields = Math.class.getDeclaredFields();
		for (int i = 0 ;  i < fields.length ; i++){
			System.out.println("Field :" + fields[i].getName());;
		}
	}

}
