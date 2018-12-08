/**Recursive Function for Fibonacci Series**/

import java.util.*;
class RecursiveFibbonaci {
	
	static Scanner sc = new Scanner(System.in);
	
	public static void main(String[] args) {
		System.out.print("Number of terms: ");
		int limit = sc.nextInt();
		if (limit == 0) {
			System.exit(0);
		}
		else if (limit == 1) {
			System.out.println("1 ");
			System.exit(0);
		}
		else if (limit == 2) {
			System.out.println("1 1 ");
			System.exit(0);
		}
		limit -= 2;
		fibonacci(1, 1, 1, limit);
	}

	public static int fibonacci(int a, int b, int count, int limit) {
		int c;
		if (count <= limit) {
			c = a + b;
			System.out.print(c + " ");
			a = b;
			b = c;
			count++;
			return fibonacci(a, b, count, limit);
		}
		else {
			System.exit(0);
		}
		return -1;
	}	
}