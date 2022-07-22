package b.b16;

import java.util.ArrayList;

public class Taille {

	int octets;

	public Taille(int t) {
		this.octets = t;
	}
	
	public Taille(String s) {
		if (s.endsWith("Ko")) {
			this.octets = Integer.parseInt(s.substring(0, s.length()-2))*1024;
		} else if (s.endsWith("Mo")) {
			this.octets = Integer.parseInt(s.substring(0, s.length()-2))*1024*1024;
		}
	}
	
	public String toString() {
		return String.valueOf(this.octets)+" octets";
	}
	
	public static void main(String[] args) {

		ArrayList<Taille> tailles = new ArrayList<>();
		
		tailles.add(new Taille(1440000));
		tailles.add(new Taille("440Ko"));
		tailles.add(new Taille("20Mo"));
		
		System.out.println(tailles);
		
	}

}
