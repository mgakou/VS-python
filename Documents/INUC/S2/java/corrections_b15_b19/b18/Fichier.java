package b.b18;

import java.util.ArrayList;

public class Fichier {

	String nom, extension;
	int taille;

	public Fichier(String n, String e, int t) {
		this.nom = n;
		this.extension = e;
		this.taille = t;
	}
	
	public String toString() {
		String out = this.nom+"."+this.extension;
		if (this.taille >= Math.pow(10, 6)) {
			out += " ("+(this.taille / Math.pow(10,6)) + "Mo)";
		} else if (this.taille >= Math.pow(10,3)) {
			out += " ("+(this.taille / Math.pow(10,3)) + "Ko)";
		} else {
			out += " ("+this.taille + " octets)";
		}
		return out;
	}
	
	public boolean equals(Object o) {
		Fichier f = (Fichier)o;
		return this.nom.equals(f.nom) && this.extension.equals(f.extension) && this.taille==f.taille;
	}
	
	public static void main(String[] args) {
		
		ArrayList<Fichier> fichiers = new ArrayList<Fichier>();
		fichiers.add(new Fichier("data","csv", 1440000));
		fichiers.add(new Fichier("readme","txt", 4056));
		fichiers.add(new Fichier("cookie","txt", 24));
		fichiers.add(new Fichier("data","exe",55480000));
		fichiers.add(new Fichier("resultats","csv", 120000));
		
		System.out.println(fichiers);

		Fichier nouveau = new Fichier("data","csv", 1440000);
		boolean doublon = false;
		for (int i=0; i<fichiers.size(); i++) {
			if (fichiers.get(i).equals(nouveau)) {
				doublon = true;
			}
		}
		System.out.println(doublon);
		
		System.out.println(fichiers.contains(nouveau));
		
	}

}
