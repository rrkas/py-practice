import java.util.*;
import java.lang.*;
import java.io.*;

class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		String s = "ahbkbk";
        // for loop
    	for(int i =0; i<s.length();i++){
		    System.out.println(s.charAt(i));
		}

		System.out.println();
		
        // for each loop
        for(char c:s.toCharArray()){
		    System.out.println(c);
		}
	}
}
