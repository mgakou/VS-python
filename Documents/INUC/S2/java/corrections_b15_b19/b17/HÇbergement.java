package b.b17;

import java.util.ArrayList;

public class Hébergement {

	String nom, ville;
	int département;
	boolean wifi, parking; 
	
	public Hébergement(String n, int d, String v, boolean pi, boolean pa) {
		this.nom = n;
		this.ville = v;
		this.département = d;
		this.wifi = pi;
		this.parking = pa;
	}
	
	public String toString() {
		String out = this.nom + " à " + this.ville +" ("+ this.département +"). ";
		if (this.wifi) 
			if (this.parking)
				out += "Wifi et parking inclus dans la location";
			else 
				out += "Wifi gratuit";
		else 
			if (this.parking)
				out += "Parking gratuit";
		return out;	
	}
	
	public static void main(String[] args) {
		
		ArrayList<Hébergement> hébergements = new ArrayList();
		hébergements.add(new Hébergement("Les Lilas", 66, "Argelès-sur-mer", true, false));
		hébergements.add(new Hébergement("Les Dunes", 40, "Soorts-Hossegor", false, true));
		hébergements.add(new Hébergement("Les Cormorans", 29, "Saint-Renan", true, true));
		hébergements.add(new Hébergement("Le Pic", 31, "Bagnères-de-Luchon", false, false));
	
		for (int i=0; i<hébergements.size(); i++) {
			System.out.println(hébergements.get(i));
		}
	}

}
